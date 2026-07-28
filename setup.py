# -- coding: utf-8 --

import ast
import re
from pathlib import Path

from setuptools import find_packages, setup


# Get version from __version__ in nhance/__init__.py
version_pattern = re.compile(r"__version__\s*=\s*(.*)")

app_root = Path(__file__).parent
init_file = app_root / "nhance" / "__init__.py"

init_content = init_file.read_text(encoding="utf-8")
version_match = version_pattern.search(init_content)

if not version_match:
    raise RuntimeError(
        "Unable to find __version__ in nhance/__init__.py"
    )

version = str(ast.literal_eval(version_match.group(1)))


# Load valid third-party Python requirements
requirements_file = app_root / "requirements.txt"

install_requires = []

if requirements_file.exists():
    install_requires = [
        line.strip()
        for line in requirements_file.read_text(
            encoding="utf-8"
        ).splitlines()
        if line.strip()
        and not line.strip().startswith("#")
        and line.strip().lower() not in {"frappe", "erpnext"}
    ]


setup(
    name="nhance",
    version=version,
    description="Nhance",
    author="Epoch",
    author_email="support@epochconsulting.in",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires,
)