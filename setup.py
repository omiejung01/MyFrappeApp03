from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in mitsib_insurance/__init__.py
from mitsib_insurance import __version__ as version

setup(
	name="mitsib_insurance",
	version=version,
	description="Mitsib Car Insurance System",
	author="Dhirachat Chayaporn",
	author_email="omiejung@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
