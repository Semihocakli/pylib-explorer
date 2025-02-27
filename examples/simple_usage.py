"""Simple usage example for PyLib Explorer."""

import os
import sys
import logging
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()

# Add parent directory to Python path (to find pylib_explorer if not installed)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pylib_explorer.core import LibExplorer, explore_random_package, explore_package

# Logging settings
logging.basicConfig(level=logging.INFO)

def example_1_random_package(language="en"):
    """Generate README for a random package."""
    print(f"\n=== Example 1: Random Package Exploration (in {language}) ===\n")
    
    # Initialize LibExplorer with API key from environment variables
    explorer = LibExplorer(
        provider="openai",  # or "claude"
        output_dir="./example_outputs",
        min_package_downloads=10000,  # This parameter is now optional but kept for reference
        language=language,  # Language option for README content
    )
    
    # Select a random package and generate README
    try:
        readme_content = explorer.generate_readme()
        
        print(f"\nOutput directory: {explorer.output_dir}")
        print(f"README preview ({language}):")
        print("-" * 50)
        # Show first 500 characters
        print(readme_content[:500] + "...\n")
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        print("Trying a specific package instead...")
        # In case of error, try a specific package
        readme_content = explorer.generate_readme(package_name="requests")
        print(f"\nOutput directory: {explorer.output_dir}")
        print(f"README preview (requests package, {language}):")
        print("-" * 50)
        print(readme_content[:500] + "...\n")

def example_2_specific_package(language="en"):
    """Generate README for a specific package."""
    package_name = "requests"  # or any other package name
    
    print(f"\n=== Example 2: '{package_name}' Package Exploration (in {language}) ===\n")
    
    # Use the convenience function
    readme_content = explore_package(
        package_name=package_name,
        provider="openai",  # or "claude"
        output_dir="./example_outputs",
        language=language,  # Language option for README content
    )
    
    print(f"\nOutput directory: ./example_outputs")
    print(f"README preview ({language}):")
    print("-" * 50)
    # Show first 500 characters
    print(readme_content[:500] + "...\n")

if __name__ == "__main__":
    # Create output directory
    os.makedirs("./example_outputs", exist_ok=True)
    
    # Check for API keys
    openai_key = os.environ.get("OPENAI_API_KEY")
    claude_key = os.environ.get("ANTHROPIC_API_KEY")
    
    if not openai_key and not claude_key:
        print("""
        Error: No API key found!
        
        Please set at least one of the following environment variables:
        - OPENAI_API_KEY
        - ANTHROPIC_API_KEY
        
        Example:
        export OPENAI_API_KEY=your_api_key_here
        or
        Create a .env file and add your API keys.
        """)
        sys.exit(1)
    
    try:
        # Ask user for language preference (default is English)
        default_language = "en"
        user_language = input(f"Select README language (default: {default_language}): ").strip() or default_language
        
        # Run examples
        example_1_random_package(user_language)
        example_2_specific_package(user_language)
        
        print("\nExamples completed successfully! 🎉")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1) 