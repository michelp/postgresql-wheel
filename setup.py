from setuptools import setup

setup(
    name='postgresql',
    version='13.4',
    description='PostgreSQL in a Python Wheel.',
    author='Michel Pelletier',
    packages=['postgresql'],    
    setup_requires=["cffi>=1.0.0"],
    cffi_modules=['postgresql/build.py:ffibuilder'],
    install_requires=["cffi>=1.0.0"],
)
