import os

import versioneer
from setuptools import setup


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join("..", path, filename))
    return paths


setup(
    name="postgresql_wheel",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="PostgreSQL Server compiled into a Python Wheel.",
    author="Michel Pelletier",
    packages=["postgresql"],
    package_data={"postgresql": package_files("postgresql")},
    setup_requires=["cffi"],
    cffi_modules=["postgresql/build.py:ffibuilder"],
    python_requires=">=3.7,<3.10",
)
