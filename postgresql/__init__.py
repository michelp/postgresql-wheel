from cffi import FFI

ffibuilder = FFI()

ffibuilder.set_source("_postgresql", "")

ffibuilder.cdef("")

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
