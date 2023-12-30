from typing import List


config_requires: List[str] = [
    "pyclassifiers",
]
dev_requires: List[str] = [
    "pypitools",
]
install_requires: List[str] = [
    "pytconf",
    "pylogconf",
]
make_requires: List[str] = [
    "pyclassifiers",
    "pymakehelper",
    "pydmt",
]
test_requires: List[str] = [
    "pylint",
    "pytest",
    "pytest-cov",
    "pyflakes",
    "flake8",
    "mypy",
]
requires = config_requires + install_requires + make_requires + test_requires
