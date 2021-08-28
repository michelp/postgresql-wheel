from setuptools import setup

import os


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join("..", path, filename))
    return paths


extra_files = package_files("postgresql_wheel/binary")

setup(
    name="postgresql_wheel",
    version="13.4",
    description="PostgreSQL in a Python Wheel.",
    author="Michel Pelletier",
    packages=["postgresql_wheel"],
    package_data={"postgresql_wheel": extra_files},
    setup_requires=["cffi>=1.0.0"],
    install_requires=["psycopg2-binary"],
    cffi_modules=["postgresql_wheel/__init__.py:ffibuilder"],
    python_requires=">=3.7,<3.10",
)
