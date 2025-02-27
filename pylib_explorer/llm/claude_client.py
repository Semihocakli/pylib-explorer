"""Anthropic Claude API client for PyLib Explorer."""

import os
import logging
from typing import Optional

try:
    import anthropic
except ImportError:
    raise ImportError(
        "Anthropic package is not installed. Please install it using 'pip install anthropic'"
    )

logger = logging.getLogger(__name__)

class ClaudeClient:
    """Client for interacting with Anthropic's Claude API."""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the Claude client.
        
        Args:
            api_key: Anthropic API key. If None, it will be read from the ANTHROPIC_API_KEY environment variable.
        """
        # Use the provided API key or get it from environment variables
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        
        if not self.api_key:
            raise ValueError(
                "Anthropic API key not found. Please provide it as an argument or "
                "set the ANTHROPIC_API_KEY environment variable."
            )
        
        # Initialize the Anthropic client
        self.client = anthropic.Anthropic(api_key=self.api_key)
        logger.info("Claude client initialized")
    
    def generate_text(self, prompt: str) -> str:
        """
        Generate text using Claude.
        
        Args:
            prompt: Text prompt for generation.
            
        Returns:
            str: Generated text.
        """
        logger.debug(f"Sending prompt to Claude (length: {len(prompt)} characters)")
        
        try:
            response = self.client.messages.create(
                model="claude-3-opus-20240229",  # Using Claude 3 Opus for high-quality README generation
                max_tokens=4000,
                temperature=0.7,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            # Extract and return the generated text
            generated_text = response.content[0].text
            logger.debug(f"Received response from Claude (length: {len(generated_text)} characters)")
            return generated_text
            
        except Exception as e:
            logger.error(f"Error generating text with Claude: {str(e)}")
            raise 