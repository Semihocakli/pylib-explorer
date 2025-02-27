# Contributing to PyLib Explorer

Thank you for your interest in contributing to PyLib Explorer! This document provides guidelines for contributing to the project.

## Getting Started

1. Fork the repository
2. Clone your fork to your local machine
3. Install the development dependencies:

```bash
cd pylib-explorer
pip install -e ".[dev]"
```

## Development Process

1. Create a branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes

3. Run the tests to ensure everything is working:
   ```bash
   pytest
   ```

4. Format your code:
   ```bash
   black pylib_explorer tests examples
   isort pylib_explorer tests examples
   flake8 pylib_explorer tests examples
   ```

5. Commit your changes:
   ```bash
   git commit -am "Add your detailed commit message"
   ```

6. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

7. Create a pull request from your fork to the main repository

## Code Style

- We use [Black](https://github.com/psf/black) for code formatting
- We use [isort](https://github.com/PyCQA/isort) for sorting imports
- We use [flake8](https://github.com/PyCQA/flake8) for linting

## Testing

- Write tests for new features using pytest
- Ensure all tests pass before submitting a pull request
- Aim for good test coverage

## Documentation

- Update the documentation for any changes to the API
- Document new features and provide examples
- Make sure code is well-documented with docstrings

## Pull Request Process

1. Update the README.md or documentation with details of changes if appropriate
2. Update the tests if needed
3. The PR should work on Python 3.7 and later versions
4. The PR needs to be approved by at least one maintainer before being merged

## License

By contributing to PyLib Explorer, you agree that your contributions will be licensed under the project's MIT License. 