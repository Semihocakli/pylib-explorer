"""OpenAI API client for PyLib Explorer."""

import os
import logging
from typing import Optional

try:
    from openai import OpenAI
except ImportError:
    raise ImportError(
        "OpenAI package is not installed. Please install it using 'pip install openai'"
    )

logger = logging.getLogger(__name__)

class OpenAIClient:
    """Client for interacting with OpenAI's API."""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the OpenAI client.
        
        Args:
            api_key: OpenAI API key. If None, it will be read from the OPENAI_API_KEY environment variable.
        """
        # Use the provided API key or get it from environment variables
        self.api_key = api_key or os.environ.get("OPENAI_API_KEY")
        
        if not self.api_key:
            raise ValueError(
                "OpenAI API key not found. Please provide it as an argument or "
                "set the OPENAI_API_KEY environment variable."
            )
        
        # Initialize the OpenAI client
        self.client = OpenAI(api_key=self.api_key)
        logger.info("OpenAI client initialized")
    
    def generate_text(self, prompt: str) -> str:
        """
        Generate text using OpenAI.
        
        Args:
            prompt: Text prompt for generation.
            
        Returns:
            str: Generated text.
        """
        logger.debug(f"Sending prompt to OpenAI (length: {len(prompt)} characters)")
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",  # Using GPT-4 for high-quality README generation
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=2500,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0,
            )
            
            # Extract and return the generated text
            generated_text = response.choices[0].message.content
            logger.debug(f"Received response from OpenAI (length: {len(generated_text)} characters)")
            return generated_text
            
        except Exception as e:
            logger.error(f"Error generating text with OpenAI: {str(e)}")
            raise 