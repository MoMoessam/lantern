# Contributing to Lantern

Thank you for contributing to Lantern!

## Development Setup

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install the required dependencies.
4. Run the application and tests before making changes.

## Branch Naming Convention

Use descriptive, short-lived branches:

- `feature/description` for new features.
- `fix/description` for bug fixes.
- `docs/description` for documentation changes.
- `test/description` for test-related changes.

## Commit Message Convention

Follow Conventional Commits:

`type(scope): description`

Allowed types:

- `feat`: New functionality.
- `fix`: Bug fixes.
- `docs`: Documentation changes.
- `refactor`: Code restructuring.
- `test`: Adding or updating tests.
- `chore`: Maintenance tasks.

Example: `feat(cli): add task sorting by title`

## Pull Request Workflow

1. Create a GitHub issue describing the change.
2. Create a short-lived branch from the latest `main`.
3. Implement and test your changes.
4. Commit using Conventional Commits.
5. Push your branch and open a pull request against the original repository's `main`.
6. Explain what changed and why, and reference the issue using `Closes #ISSUE_NUMBER`.
7. Request a review from the other team member.
8. Address requested changes before approval.
9. The author merges the approved pull request and deletes the branch.

## Code Review

Every pull request must be reviewed and approved by the other team member before merging.

Keep changes focused, provide clear descriptions, and test your work before requesting review.