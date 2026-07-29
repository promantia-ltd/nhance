# -*- coding: utf-8 -*-

import ast
import re

from setuptools import find_packages, setup


# Get version from __version__ variable in nhance/__init__.py
_version_re = re.compile(r"__version__\s*=\s*(.*)")

with open("requirements.txt", encoding="utf-8") as f:
	install_requires = [
		requirement.strip()
		for requirement in f
		if requirement.strip()
		and not requirement.strip().startswith("#")
		and requirement.strip().lower() != "frappe"
	]

with open("nhance/__init__.py", "rb") as f:
	version_match = _version_re.search(f.read().decode("utf-8"))

	if not version_match:
		raise RuntimeError(
			"Unable to find __version__ in nhance/__init__.py"
		)

	version = str(ast.literal_eval(version_match.group(1)))


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
