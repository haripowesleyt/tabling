# Contributing to Tabling

Thank you for considering contributing to **Tabling**! We welcome bug reports, feature requests, code improvements, and documentation updates.

## How to Contribute

1. **Fork** the repository.
2. **Create a new branch** for your feature or fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**.
4. **Ensure quality checks pass** (see below).
5. **Commit** with clear, conventional messages.
6. **Push** to your fork and open a **pull request**.

## Code Style & Quality

Tabling uses the following tools to ensure a clean and consistent codebase:

### Code Formatter: `black`
- Automatically formats Python code to PEP 8 standards.
- Run before committing:
  ```bash
  black --line-length 100 .
  ```

### Linter: `pylint`
- Enforces code style, detects bugs and smells.
- Run and fix issues:
  ```bash
  pylint tabling
  ```

### Static Typing: `mypy`
- Ensures correct type annotations.
- Run:
  ```bash
  mypy tabling
  ```

## Commit Conventions

Use clear, conventional commit messages:
```
fix: correct column alignment bug
feat: add Markdown export support
docs: update README example
```

## Before You Submit

- Make sure all formatters, linters, and type checks pass.
- Check your changes don't break existing examples.
- Write tests for new functionality if applicable.
- Update documentation for any new features or changes.

## Need Help?

Feel free to open an issue for questions, clarifications, or suggestions.