from setuptools import setup

import os


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join("..", path, filename))
    return paths


extra_files = package_files("postgresql/binary")

setup(
    name="postgresql",
    version="13.4",
    description="PostgreSQL in a Python Wheel.",
    author="Michel Pelletier",
    packages=["postgresql"],
    package_data={"postgresql": extra_files},
    setup_requires=["cffi>=1.0.0"],
    cffi_modules=["postgresql/__init__.py:ffibuilder"],
    python_requires=">=3.7,<3.10",
)
