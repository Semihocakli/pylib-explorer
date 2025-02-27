"""PyLib Explorer packaging script."""

import os
import subprocess
import sys
import shutil

def main():
    """Builds and prepares the PyLib Explorer package for distribution."""
    print("Building PyLib Explorer package")
    
    # Check working directory
    if not os.path.exists("setup.py"):
        print("Error: Run this script from the PyLib Explorer root directory.")
        sys.exit(1)
    
    # Clean previous build files
    clean_dirs = ["build", "dist", "pylib_explorer.egg-info"]
    for dir_name in clean_dirs:
        if os.path.exists(dir_name):
            print(f"Cleaning {dir_name} directory...")
            shutil.rmtree(dir_name)
    
    # Build packages
    try:
        print("\nCreating package...")
        subprocess.check_call([sys.executable, "-m", "build"])
        
        print("\nPackage built successfully! 🎉")
        print("\nGenerated packages:")
        
        if os.path.exists("dist"):
            for file_name in os.listdir("dist"):
                print(f"  - dist/{file_name}")
        
        print("\nTo upload to PyPI:")
        print("  python -m twine upload dist/*")
        
        print("\nTo upload to Test PyPI:")
        print("  python -m twine upload --repository testpypi dist/*")
        
    except subprocess.CalledProcessError as e:
        print(f"Error: Package build failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 