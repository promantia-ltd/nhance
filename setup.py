# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import re
import ast

_version_re = re.compile(r"__version__\s*=\s*(.*)")

with open("requirements.txt") as f:
    install_requires = [
        requirement.strip()
        for requirement in f.readlines()
        if requirement.strip()
        and requirement.strip().lower() != "frappe"
    ]

with open("nhance/__init__.py", "rb") as f:
    version = str(
        ast.literal_eval(
            _version_re.search(
                f.read().decode("utf-8")
            ).group(1)
        )
    )

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
