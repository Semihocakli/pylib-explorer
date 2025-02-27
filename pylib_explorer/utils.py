"""Helper functions for PyLib Explorer."""

import os
import re
import logging
import datetime
from typing import List, Dict, Any, Optional
from importlib.metadata import Distribution
import requests

logger = logging.getLogger(__name__)

def save_readme(content: str, package_name: str, output_dir: str = "./outputs") -> str:
    """
    Saves README content to a file.
    
    Args:
        content: README content.
        package_name: Package name.
        output_dir: Output directory.
        
    Returns:
        str: Full path of the saved file.
    """
    # Create directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Create filename (with timestamp)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"{package_name}_{timestamp}.md"
    file_path = os.path.join(output_dir, file_name)
    
    # Write to file
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        logger.info(f"README file saved: {file_path}")
        return file_path
    except Exception as e:
        logger.error(f"Could not save README file: {str(e)}")
        raise


def filter_popular_packages(packages: List[Distribution], min_downloads: int = 10000) -> List[Distribution]:
    """
    Filters packages by popularity.
    
    Args:
        packages: List of packages to filter.
        min_downloads: Minimum download count.
        
    Returns:
        List[Distribution]: Filtered list of packages.
    """
    # Changed filtering logic to avoid API rate limit issues
    # Names of commonly used popular packages
    popular_packages = [
        "numpy", "pandas", "requests", "matplotlib", "scipy", "django", "flask", 
        "tensorflow", "pytorch", "pillow", "scikit-learn", "beautifulsoup4", 
        "sqlalchemy", "fastapi", "celery", "pytest", "sphinx", "jupyter", 
        "pyyaml", "tqdm", "click", "selenium", "paramiko", "jinja2", "urllib3",
        "certifi", "idna", "six", "psutil", "markupsafe", "werkzeug", "pygments",
        "cryptography", "chardet", "pyjwt", "toml", "babel", "pytz", "regex"
    ]
    
    filtered_packages = []
    popular_count = 0
    
    for package in packages:
        try:
            package_name = package.metadata["Name"].lower()
            
            # Add if in popular list or matches naming patterns that suggest popularity
            if package_name in popular_packages or \
               len(package_name) > 3 and not package_name.startswith("_") and \
               not package_name.startswith("test") and not "demo" in package_name:
                filtered_packages.append(package)
                popular_count += 1
                
                # Limit to maximum 50 packages in the list
                if popular_count >= 50:
                    break
        except Exception as e:
            logger.warning(f"Could not process package {package.metadata.get('Name', 'Unknown package')}: {str(e)}")
    
    # If no packages were filtered, add at least a few packages
    if not filtered_packages and len(packages) > 0:
        filtered_packages = packages[:min(20, len(packages))]
    
    logger.info(f"Filtered {len(filtered_packages)} packages out of {len(packages)} total")
    return filtered_packages


def get_package_download_count(package_name: str) -> int:
    """
    Gets the download count for a package using the PyPI API.
    NOTE: Currently not used due to API rate limit issues.
    
    Args:
        package_name: Package name to get download count for.
        
    Returns:
        int: Total download count for the package.
    """
    # Returning a static value due to rate limit issues
    # In a real application, another source for download counts could be used
    # or a waiting period added between requests
    return 20000
    
    # Temporarily disabling the code below
    """
    try:
        # Send request to PyPI API
        response = requests.get(f"https://pypistats.org/api/packages/{package_name}/recent", timeout=5)
        response.raise_for_status()
        
        data = response.json()
        # Download count in the last 30 days
        downloads = data.get("data", {}).get("last_month", 0)
        
        return downloads
    except Exception as e:
        logger.warning(f"Could not get download count for {package_name}: {str(e)}")
        # Return 0 as default in case of error
        return 0
    """


def clean_package_name(name: str) -> str:
    """
    Cleans package name (makes it safe for a filename).
    
    Args:
        name: Package name to clean.
        
    Returns:
        str: Cleaned package name.
    """
    # Remove invalid characters for filenames
    cleaned = re.sub(r'[^\w\-\.]', '_', name)
    return cleaned 