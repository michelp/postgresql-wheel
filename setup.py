from setuptools import setup

import os


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join("..", path, filename))
    return paths


extra_files = package_files("postgresql")

setup(
    name="postgresql_wheel",
    version="13.4",
    description="PostgreSQL Server compiled into a Python Wheel.",
    author="Michel Pelletier",
    packages=["postgresql"],
    package_data={"postgresql": extra_files},
    setup_requires=["cffi"],
    install_requires=["plumbum"],
    cffi_modules=["postgresql/build.py:ffibuilder"],
    python_requires=">=3.8,<3.9",
)
