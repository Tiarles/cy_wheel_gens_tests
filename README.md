# Short test to check generators after cythonization

Example for the [Cython #6096](https://github.com/cython/cython/issues/6096) issue.

## Steps to reproduce

1. (optional) Create and activate a virtualenv:
```console
python -m venv venv
venv\Scripts\activate
```

2. Install the requirements:
```console
python -m pip install -r requirements
```

3. And run `tox` from the root:
```console
tox
```

### Output

Pytest will execute the tests and show the follow assertion report (Python 3.11 used):
```console
============================================================================================= test session starts ==============================================================================================
platform win32 -- Python 3.11.4, pytest-8.1.1, pluggy-1.4.0
cachedir: .tox\py311\.pytest_cache
rootdir: C:\...\cy_wheel_gens_tests
configfile: pyproject.toml
collected 1 item

test_cy_gens.py F                                                                                                                                                                                         [100%]

=================================================================================================== FAILURES =================================================================================================== 
_________________________________________________________________________________________________ test_cy_gens _________________________________________________________________________________________________ 

    def test_cy_gens():
        from test_gens import my_generator as my_generator_cy  # Importing cythonized and installed generator version
        from main import _my_generator as my_generator_py  # Regular python file

        try:
            for i in my_generator_cy():
                print("\ttest:", i)
        except OSError:
            pass

        logger.info(f"\n\nPython Version {sys.version}")
        logger.info("inspect.isgeneratorfunction(my_generator_cy):", inspect.isgeneratorfunction(my_generator_cy))
        logger.info("inspect.isgeneratorfunction(my_generator_py):", inspect.isgeneratorfunction(my_generator_py))

        assert inspect.isgeneratorfunction(my_generator_py)  # Will pass
>       assert inspect.isgeneratorfunction(my_generator_cy)  # Will fail
E       assert False
E        +  where False = <function isgeneratorfunction at 0x000001B4F8197CE0>(<function my_generator at 0x000001B4F8FB8F40>)
E        +    where <function isgeneratorfunction at 0x000001B4F8197CE0> = inspect.isgeneratorfunction

test_cy_gens.py:23: AssertionError
--------------------------------------------------------------------------------------------- Captured stdout call --------------------------------------------------------------------------------------------- 
my_generator: 6
        test: 6
my_generator: 12
=========================================================================================== short test summary info ============================================================================================ 
FAILED test_cy_gens.py::test_cy_gens - assert False
============================================================================================== 1 failed in 0.11s =============================================================================================== 

```

Note that, in the two assertion present in the `test_cy_gens.py` file, first checks the generator implement in the 
python file and the second one from the library where the same generator was cythonized on `setup.py` file.

Previously, in the code, the cythonized generator is used in a `for` loop showing that it behaves as one.
