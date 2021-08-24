from cffi import FFI
from pathlib import Path


def build_ffi():
    ffibuilder = FFI()

    source = r"""
        """
    
    ffibuilder.set_source(
        "_postgresql",
        source,
        libraries=["postgresql"],
        extra_compile_args=[
        ],
    )

    return ffibuilder


ffibuilder = build_ffi()

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
