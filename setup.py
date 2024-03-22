from setuptools import setup
import sys
import os
import shutil
FOLDER_DIR_PATH = os.path.dirname(__file__)
sys.path.insert(0, FOLDER_DIR_PATH)

shutil.copy(R"C:\WORK\generators_test_pys\main.py", R"C:\WORK\generators_test_pys\src\test_gens\impl.pyx")

from Cython.Build import cythonize
from Cython.Compiler.Errors import CompileError
try:
    language_level = 3
    ext_modules = cythonize(
        [R"src\test_gens\impl.pyx"],
        compiler_directives={
            "binding": True,  # so inspect function works properly on cythonized functions
            "language_level": language_level,
        },  # avoid cython warnings
    )
except CompileError:
    import sys
    sys.exit()

os.remove(R"C:\WORK\generators_test_pys\src\test_gens\impl.pyx")

setup(
    ext_modules=ext_modules
)