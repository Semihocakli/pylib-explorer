"""Core module containing the main functions of PyLib Explorer."""

import os
import random
import importlib.metadata
import logging
from typing import List, Dict, Optional, Union, Tuple

from .llm import openai_client, claude_client
from .utils import save_readme, filter_popular_packages

# Logging settings
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class LibExplorer:
    """Main class for exploring Python libraries."""
    
    def __init__(
        self, 
        api_key: Optional[str] = None,
        provider: str = "openai",
        min_package_downloads: int = 10000,
        output_dir: str = "./outputs",
        language: str = "en",  # English as default language
    ):
        """
        Initialize the PyLib Explorer class.
        
        Args:
            api_key: API key for the LLM provider. If None, it will be searched in environment variables.
            provider: LLM provider to use. 'openai' or 'claude'.
            min_package_downloads: Minimum download count filter.
            output_dir: Directory where README files will be saved.
            language: Language for the README (ISO code or full name, e.g.: "en", "tr", "English", "Turkish").
        """
        self.provider = provider.lower()
        self.output_dir = output_dir
        self.min_package_downloads = min_package_downloads
        self.language = language
        
        # Create API clients
        if self.provider == "openai":
            self.client = openai_client.OpenAIClient(api_key)
        elif self.provider == "claude":
            self.client = claude_client.ClaudeClient(api_key)
        else:
            raise ValueError(f"Unsupported provider: {provider}. Use 'openai' or 'claude'.")
        
        # Create output directory
        os.makedirs(self.output_dir, exist_ok=True)
        
        logger.info(f"PyLib Explorer initialized. Provider: {provider}, Language: {language}")
    
    def get_random_package(self) -> Tuple[str, Dict]:
        """
        Selects a random package from Python packages.
        
        Returns:
            Tuple[str, Dict]: Package name and package information.
        """
        # List all Python packages
        all_packages = list(importlib.metadata.distributions())
        
        # Filter to popular packages (optional)
        filtered_packages = filter_popular_packages(all_packages, self.min_package_downloads)
        
        if not filtered_packages:
            logger.warning("No packages found after filtering, using all packages.")
            filtered_packages = all_packages
        
        # Select a random package
        try:
            package = random.choice(filtered_packages)
            package_name = package.metadata["Name"]
            
            # Collect basic information about the package
            package_info = {
                "name": package_name,
                "version": package.version,
                "summary": package.metadata.get("Summary", ""),
                "author": package.metadata.get("Author", ""),
                "license": package.metadata.get("License", ""),
                "requires": list(package.requires or []),
            }
            
            logger.info(f"Random package selected: {package_name}")
            return package_name, package_info
        except (IndexError, KeyError) as e:
            # If there's an issue with random package selection, use a safe alternative
            logger.warning(f"Error in random package selection: {str(e)}. Using 'requests' package.")
            
            try:
                package_metadata = importlib.metadata.metadata("requests")
                package_info = {
                    "name": "requests",
                    "version": importlib.metadata.version("requests"),
                    "summary": package_metadata.get("Summary", ""),
                    "author": package_metadata.get("Author", ""),
                    "license": package_metadata.get("License", ""),
                    "requires": list(importlib.metadata.requires("requests") or []),
                }
                return "requests", package_info
            except Exception:
                # As a last resort, continue with minimal information
                logger.error("Fallback package (requests) not found.")
                return "requests", {"name": "requests", "version": "N/A", "summary": ""}
    
    def generate_readme(self, package_name: Optional[str] = None) -> str:
        """
        Generates a README file for the specified package.
        
        Args:
            package_name: Package name for which to generate README. If None, a random one is selected.
            
        Returns:
            str: Generated README content.
        """
        if package_name is None:
            package_name, package_info = self.get_random_package()
        else:
            try:
                package_metadata = importlib.metadata.metadata(package_name)
                package_info = {
                    "name": package_name,
                    "version": importlib.metadata.version(package_name),
                    "summary": package_metadata.get("Summary", ""),
                    "author": package_metadata.get("Author", ""),
                    "license": package_metadata.get("License", ""),
                    "requires": list(importlib.metadata.requires(package_name) or []),
                }
            except importlib.metadata.PackageNotFoundError:
                logger.error(f"Package not found: {package_name}")
                raise ValueError(f"Package not found: {package_name}")
        
        # Generate README content with LLM
        prompt = self._create_readme_prompt(package_name, package_info)
        readme_content = self.client.generate_text(prompt)
        
        # Save README file
        file_path = save_readme(readme_content, package_name, self.output_dir)
        
        logger.info(f"README file created: {file_path}")
        return readme_content
    
    def _create_readme_prompt(self, package_name: str, package_info: Dict) -> str:
        """
        Prepares the prompt to be sent to the LLM for README generation.
        
        Args:
            package_name: Package name.
            package_info: Package information.
            
        Returns:
            str: Prompt text to be sent to the LLM.
        """
        # Convert language codes to full language names
        language_map = {
            "en": "English",
            "tr": "Turkish/Türkçe",
            "fr": "French/Français",
            "de": "German/Deutsch",
            "es": "Spanish/Español",
            "it": "Italian/Italiano",
            "nl": "Dutch/Nederlands",
            "pt": "Portuguese/Português",
            "ru": "Russian/Русский",
            "ja": "Japanese/日本語",
            "zh": "Chinese/中文",
        }
        
        # Convert language code to full language name (if possible)
        target_language = language_map.get(self.language.lower(), self.language)
        
        return f"""
        IMPORTANT: You must prepare this README in {target_language} language!
        
        Create a detailed README.md file for the Python library '{package_name}'.
        
        Package Information:
        - Version: {package_info.get('version', 'No information')}
        - Summary: {package_info.get('summary', 'No information')}
        - Author: {package_info.get('author', 'No information')}
        - License: {package_info.get('license', 'No information')}
        - Dependencies: {', '.join(package_info.get('requires', []) or ['No information'])}
        
        The README.md content should include the following sections:
        
        1. Title and brief description
        2. Installation instructions
        3. Simple "Getting Started" example
        4. Main use cases and core concepts
        5. Advanced usage examples and scenarios
        6. API reference (main classes, methods, functions)
        7. Project use cases
        8. Best practices and performance tips
        9. Comparison with alternative libraries
        
        Each section should include code examples, use cases, and detailed explanations.
        Make sure users fully understand why and how they should use this library.
        Answer in Markdown format with proper headings, lists, code blocks, and links.
        
        REMINDER: All content must be in {target_language} language! This is very important.
        """


def explore_random_package(
    api_key: Optional[str] = None,
    provider: str = "openai",
    min_package_downloads: int = 10000,
    output_dir: str = "./outputs",
    language: str = "en",
) -> str:
    """
    Convenience function for exploring a random Python package.
    
    Args:
        api_key: API key for the LLM provider. If None, it will be searched in environment variables.
        provider: LLM provider to use. 'openai' or 'claude'.
        min_package_downloads: Minimum download count filter.
        output_dir: Directory where README files will be saved.
        language: Language for the README (ISO code or full name, e.g.: "en", "tr").
        
    Returns:
        str: Generated README content.
    """
    explorer = LibExplorer(
        api_key=api_key,
        provider=provider,
        min_package_downloads=min_package_downloads,
        output_dir=output_dir,
        language=language,
    )
    return explorer.generate_readme()


def explore_package(
    package_name: str,
    api_key: Optional[str] = None,
    provider: str = "openai",
    output_dir: str = "./outputs",
    language: str = "en",
) -> str:
    """
    Convenience function for exploring a specific Python package.
    
    Args:
        package_name: Package name for which to generate README.
        api_key: API key for the LLM provider. If None, it will be searched in environment variables.
        provider: LLM provider to use. 'openai' or 'claude'.
        output_dir: Directory where README files will be saved.
        language: Language for the README (ISO code or full name, e.g.: "en", "tr").
        
    Returns:
        str: Generated README content.
    """
    explorer = LibExplorer(
        api_key=api_key,
        provider=provider,
        output_dir=output_dir,
        language=language,
    )
    return explorer.generate_readme(package_name) 