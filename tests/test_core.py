"""Tests for core functions of PyLib Explorer."""

import os
import unittest
from unittest.mock import patch, MagicMock

import sys
import importlib.metadata

from pylib_explorer.core import LibExplorer

class TestLibExplorer(unittest.TestCase):
    """Test cases for the LibExplorer class."""
    
    @patch('pylib_explorer.llm.openai_client.OpenAIClient')
    def test_init(self, mock_openai):
        """Tests that the __init__ method works correctly."""
        # Initialize with API key
        explorer = LibExplorer(api_key="test_key", provider="openai")
        self.assertEqual(explorer.provider, "openai")
        
    @patch('pylib_explorer.llm.claude_client.ClaudeClient')
    def test_init_claude(self, mock_claude):
        """Tests initialization with Claude provider."""
        explorer = LibExplorer(api_key="test_key", provider="claude")
        self.assertEqual(explorer.provider, "claude")
    
    @patch('pylib_explorer.core.LibExplorer._create_readme_prompt')
    @patch('pylib_explorer.core.LibExplorer.get_random_package')
    @patch('pylib_explorer.llm.openai_client.OpenAIClient')
    def test_generate_readme_random(self, mock_openai, mock_get_random, mock_create_prompt):
        """Tests the README generation function for a random package."""
        # Set up mock values
        mock_get_random.return_value = ("test_package", {"name": "test_package"})
        mock_create_prompt.return_value = "test prompt"
        mock_client = MagicMock()
        mock_client.generate_text.return_value = "Test README content"
        mock_openai.return_value = mock_client
        
        # Test
        explorer = LibExplorer(api_key="test_key")
        result = explorer.generate_readme()
        
        # Assertions
        self.assertEqual(result, "Test README content")
        mock_get_random.assert_called_once()
        mock_create_prompt.assert_called_once()
        mock_client.generate_text.assert_called_once_with("test prompt")
    
if __name__ == '__main__':
    unittest.main() 