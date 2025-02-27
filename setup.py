"""PyLib Explorer setup file."""

from setuptools import setup, find_packages
import os

# Read README.md file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read dependencies from requirements.txt
with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

# Get version information
version = {}
with open(os.path.join("pylib_explorer", "__init__.py"), "r", encoding="utf-8") as f:
    exec(f.read(), version)

setup(
    name="pylib-explorer",
    version=version.get("__version__", "0.1.0"),
    author="Semih Ocaklı",
    author_email="semihocakli35@gmail.com",  
    description="LLM-powered Python library explorer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Semihocakli/pylib-explorer",       
    packages=find_packages(),
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "isort>=5.12.0",
            "flake8>=6.0.0",
            "twine>=4.0.0",
            "build>=0.10.0",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "pylib-explorer=pylib_explorer.cli:main",
        ],
    },
) 