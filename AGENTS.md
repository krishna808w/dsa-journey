# DSA Journey Python Architecture & Guidelines

`dsa-journey` is a repository of Data Structures & Algorithms implementations and problem solutions.

---

## 1. Code Standards & Python Conventions

- **Python 3 Typing**: Use standard type hints from `typing` (e.g. `List[int]`, `Dict[str, Any]`, `Optional[TreeNode]`).
- **Complexity Documentation**: Every algorithm implementation must include a docstring documenting:
  - **Time Complexity**: $\mathcal{O}(...)$ with brief explanation.
  - **Space Complexity**: $\mathcal{O}(...)$ auxiliary memory explanation.
- **Unit Testing**: Include inline test cases (e.g. `if __name__ == "__main__":` or `unittest`/`pytest` test functions) verifying edge cases (empty input, duplicates, large bounds).

---

## 2. File Organization

- Structure problem folders by category: `01-arrays/`, `02-two-pointers/`, `03-strings/`, `04-trees/`, `05-graphs/`, `06-dp/`.
- File names: `01-<problem-name-in-kebab-case>.py`.
