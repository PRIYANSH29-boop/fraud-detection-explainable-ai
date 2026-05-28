"""Project task entry points invoked via `uv run <name>`."""

import subprocess


def eda() -> int:
    """Launch the EDA notebook in Jupyter Lab."""
    return subprocess.run(
        ["jupyter", "lab", "notebooks/01_eda.ipynb"], check=True
    ).returncode


def test() -> int:
    """Run the pytest test suite."""
    return subprocess.run(["pytest"], check=True).returncode


def lint() -> int:
    """Run ruff lint on src and tests."""
    return subprocess.run(["ruff", "check", "src", "tests"], check=True).returncode


def fmt() -> int:
    """Run ruff format on src and tests."""
    return subprocess.run(["ruff", "format", "src", "tests"], check=True).returncode
