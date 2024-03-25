from setuptools import setup
import sys
import os
import shutil
FOLDER_DIR_PATH = os.path.dirname(__file__)
sys.path.insert(0, FOLDER_DIR_PATH)

ext_modules = None

if "bdist_wheel" in sys.argv:
    try:
        os.remove(os.path.join(FOLDER_DIR_PATH, R"src\test_gens\pytest_hooks_gens\plugin.py"))
    except FileNotFoundError:
        pass

    for src_rel, dst_rel in [ 
        ("main.py", R"src\test_gens\impl.pyx"),
        ("plugin.py", R"src\test_gens\pytest_hooks_gens\plugin.pyx")
    ]:
        shutil.copy(
            src=os.path.join(FOLDER_DIR_PATH, src_rel),
            dst=os.path.join(FOLDER_DIR_PATH, dst_rel)
        )

    from Cython.Build import cythonize
    from Cython.Compiler.Errors import CompileError
    try:
        language_level = 3
        ext_modules = cythonize(
            [
                R"src\test_gens\impl.pyx",
                R"src\test_gens\pytest_hooks_gens\plugin.pyx"
            ],
            compiler_directives={
                "binding": True,  # so inspect function works properly on cythonized functions
                "language_level": language_level,
            },  # avoid cython warnings
        )
        print(f"ext_modules: {ext_modules}")
    except CompileError:
        import sys
        sys.exit()

    for pyx_file in [
        R"src\test_gens\impl.pyx",
        R"src\test_gens\pytest_hooks_gens\plugin.pyx"
    ]:
        os.remove(os.path.join(FOLDER_DIR_PATH, pyx_file))

setup(
    ext_modules=ext_modules
)