"""Script to install PyLib Explorer in development mode."""

import os
import subprocess
import sys
import platform

def main():
    """Installs PyLib Explorer in development mode."""
    print("Installing PyLib Explorer in development mode")
    
    # Check Python version
    python_version = sys.version_info
    if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 7):
        print("Error: Python 3.7 or newer is required.")
        sys.exit(1)
    
    # Check working directory
    if not os.path.exists("setup.py"):
        print("Error: Run this script from the PyLib Explorer root directory.")
        sys.exit(1)
    
    # Install with development dependencies
    try:
        print("Installing with development dependencies...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-e", ".[dev]"])
        print("\nPyLib Explorer installed successfully! 🎉")
        
        # Show basic usage information
        print("\n--- Basic Usage ---")
        print("To set your API keys:")
        
        if platform.system() == "Windows":
            print("  set OPENAI_API_KEY=your_openai_api_key")
            print("  set ANTHROPIC_API_KEY=your_anthropic_api_key")
        else:
            print("  export OPENAI_API_KEY=your_openai_api_key")
            print("  export ANTHROPIC_API_KEY=your_anthropic_api_key")
        
        print("\nExplore a random library:")
        print("  pylib-explorer")
        
        print("\nGet information about a specific library:")
        print("  pylib-explorer --package numpy")
        
        print("\nTo see all command line options:")
        print("  pylib-explorer --help")
        
    except subprocess.CalledProcessError as e:
        print(f"Error: Installation failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 