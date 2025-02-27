# PyLib Explorer

PyLib Explorer is an LLM-powered tool for exploring Python libraries. This library generates comprehensive README.md files for randomly selected or specified Python packages, helping developers understand new libraries and implement them in their applications.

## Features

- 🔍 Random Python library discovery
- 🤖 OpenAI and Claude LLM integrations
- 📚 Detailed README.md file generation
- 🔧 Code examples and usage scenarios
- 📊 Popularity-based filtering
- 🧩 Easy-to-use API and CLI
- 🌍 Multi-language support (create READMEs in any language)

## Installation

```bash
pip install pylib-explorer
```

## Quick Start

### Python API Usage

```python
from pylib_explorer.core import LibExplorer

# You can provide your API key directly or use environment variables
# English is the default language (language="en")
explorer = LibExplorer(api_key="your_api_key_here", provider="openai")

# For README in a different language:
explorer_tr = LibExplorer(api_key="your_api_key_here", provider="openai", language="tr")

# Generate README for a random package
readme_content = explorer.generate_readme()
print(f"README file created: {explorer.output_dir}")

# or for a specific package:
readme_content = explorer.generate_readme(package_name="requests")
```

```python
from pylib_explorer.core import LibExplorer
from dotenv import load_dotenv

load_dotenv()

# You can provide use environment variables
explorer = LibExplorer(language="en")

# Generate README for a random package
readme_content = explorer.generate_readme()
print(f"README file created: {explorer.output_dir}")

# or for a specific package:
readme_content = explorer.generate_readme(package_name="pytorch")
```

### Command Line Usage

**For a random library exploration:**

```bash
# Set your OpenAI API key as an environment variable
export OPENAI_API_KEY=your_api_key_here

# Explore a random library (default language: English)
pylib-explorer

# Explore in Turkish
pylib-explorer --language tr

# Explore in German
pylib-explorer --language de
```

**For a specific library exploration:**

```bash
# English (default)
pylib-explorer --package requests

# Turkish
pylib-explorer --package requests --language tr
```

**Using Claude API:**

```bash
export ANTHROPIC_API_KEY=your_anthropic_api_key

pylib-explorer --provider claude --package pandas --language fr
```

## Command Line Options

```
usage: pylib-explorer [-h] [--package PACKAGE] [--provider {openai,claude}]
                      [--api-key API_KEY] [--output-dir OUTPUT_DIR]
                      [--min-downloads MIN_DOWNLOADS] [--language LANGUAGE]
                      [--verbose]

Options:
  -h, --help            Show this help message and exit
  --package PACKAGE, -p PACKAGE
                        Name of the Python package to explore. If not specified, a random package will be selected.
  --provider {openai,claude}, -m {openai,claude}
                        LLM provider to use ('openai' or 'claude').
  --api-key API_KEY, -k API_KEY
                        API key for the LLM provider. If not specified, it will be read from environment variables.
  --output-dir OUTPUT_DIR, -o OUTPUT_DIR
                        Directory where README files will be saved.
  --min-downloads MIN_DOWNLOADS, -d MIN_DOWNLOADS
                        Minimum download count filter for random selection.
  --language LANGUAGE, -l LANGUAGE
                        Language for the README content (e.g.: 'en', 'tr', 'fr', 'de', etc.)
  --verbose, -v         Enable verbose logging mode.
```

## Supported Languages

PyLib Explorer can generate READMEs in any language supported by the LLMs. To specify the language:

- You can use ISO language codes: `en`, `tr`, `fr`, `de`, `es`, `it`, etc.
- Or you can use full language names: `English`, `Turkish`, `French`, `German`, etc.

English is the default language (`en`).

### How Language Selection Works

PyLib Explorer communicates your language choice to the LLM with clear and strong instructions. Here's how it works:

1. Your language choice (short codes like `tr`, `en`) is converted to full language names
2. The prompt sent to the LLM includes:
   - At the beginning: "IMPORTANT: You must prepare this README in {language} language!"
   - At the end: "REMINDER: All content must be in {language} language! This is very important."
3. These strong instructions ensure the LLM produces content in the specified language

If you request a specific language but get content in a different language, please report it through GitHub issues.

## Setting Up API Keys

PyLib Explorer requires API keys for either OpenAI or Claude APIs. You can provide these keys in these ways:

1. **Environment Variables:** Set `OPENAI_API_KEY` or `ANTHROPIC_API_KEY` environment variables.
2. **Direct Parameter:** Provide API keys directly via code or CLI.
3. **.env File:** Create a `.env` file in your project's root directory:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ANTHROPIC_API_KEY=your_anthropic_api_key
   ```

## Development

### Requirements

- Python 3.7+
- OpenAI and/or Anthropic API keys

### Installation

```bash
git clone https://github.com/username/pylib-explorer.git
cd pylib-explorer
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

## License

Licensed under the MIT License. See [LICENSE](LICENSE) file for more information.

## Contributing

Contributions are welcome! Please check out [CONTRIBUTING.md](CONTRIBUTING.md).

## Contact

For questions or feedback, please use [GitHub Issues](https://github.com/username/pylib-explorer/issues). 
