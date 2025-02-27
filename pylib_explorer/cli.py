"""Command line interface for PyLib Explorer."""

import os
import sys
import argparse
import logging
from typing import List, Optional

from dotenv import load_dotenv

from .core import explore_random_package, explore_package

# Load environment variables
load_dotenv()

# Logging settings
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def parse_args(args: Optional[List[str]] = None) -> argparse.Namespace:
    """
    Parse command line arguments.
    
    Args:
        args: Command line arguments to parse. If None, sys.argv is used.
        
    Returns:
        argparse.Namespace: Parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description="PyLib Explorer - An LLM-powered tool for exploring Python libraries",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    
    parser.add_argument(
        "--package", "-p",
        help="Name of the Python package to explore. If not specified, a random package will be selected.",
        type=str,
        default=None,
    )
    
    parser.add_argument(
        "--provider", "-m",
        help="LLM provider to use ('openai' or 'claude').",
        type=str,
        choices=["openai", "claude"],
        default="openai",
    )
    
    parser.add_argument(
        "--api-key", "-k",
        help="API key for the LLM provider. If not specified, it will be read from environment variables.",
        type=str,
        default=None,
    )
    
    parser.add_argument(
        "--output-dir", "-o",
        help="Directory where README files will be saved.",
        type=str,
        default="./outputs",
    )
    
    parser.add_argument(
        "--min-downloads", "-d",
        help="Minimum download count filter for random selection.",
        type=int,
        default=10000,
    )
    
    parser.add_argument(
        "--language", "-l",
        help="Language for the README content (e.g.: 'en', 'tr', 'fr', 'de', etc.)",
        type=str,
        default="en",
    )
    
    parser.add_argument(
        "--verbose", "-v",
        help="Enable verbose logging mode.",
        action="store_true",
    )
    
    return parser.parse_args(args)


def main(args: Optional[List[str]] = None) -> int:
    """
    Main command line interface.
    
    Args:
        args: Command line arguments. If None, sys.argv is used.
        
    Returns:
        int: Exit code (0: success, 1: error).
    """
    parsed_args = parse_args(args)
    
    # Set verbose logging mode
    if parsed_args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    try:
        if parsed_args.package:
            logger.info(f"Exploring package '{parsed_args.package}' in {parsed_args.language} language...")
            result = explore_package(
                package_name=parsed_args.package,
                api_key=parsed_args.api_key,
                provider=parsed_args.provider,
                output_dir=parsed_args.output_dir,
                language=parsed_args.language,
            )
        else:
            logger.info(f"Exploring a random Python package in {parsed_args.language} language...")
            result = explore_random_package(
                api_key=parsed_args.api_key,
                provider=parsed_args.provider,
                min_package_downloads=parsed_args.min_downloads,
                output_dir=parsed_args.output_dir,
                language=parsed_args.language,
            )
        
        logger.info("Operation completed successfully.")
        return 0
        
    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")
        return 1


if __name__ == "__main__":
    sys.exit(main()) 