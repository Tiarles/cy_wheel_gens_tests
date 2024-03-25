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

### Output UPDATED

For Python 3.11 it works but since I need to build our software with the old versions too the issue was 
found for Python 3.8, Python 3.9 and Python 3.10.

This example has fixed. Now the generator is imported directly from the cython module (``impl.c``) without calling through the ``__init__.py`` file.

```python
# ...

def test_cy_gens():
    from test_gens.impl import _my_generator as my_generator_cy  # Importing cythonized and installed generator version
    from main import _my_generator as my_generator_py  # Regular python file

    # ...
```

Here follows the test result for all the four Python version and the final ``tox`` outcome:

```console
PS C:\WORK\cy_wheel_gens_tests> tox

# ...

py38: commands[3]> pytest test_cy_gens.py --log-cli-level=INFO
========================================================================= test session starts =========================================================================
platform win32 -- Python 3.8.4, pytest-8.1.1, pluggy-1.4.0
cachedir: .tox\py38\.pytest_cache
rootdir: C:\WORK\cy_wheel_gens_tests
configfile: pyproject.toml
collected 1 item

test_cy_gens.py::test_cy_gens 
---------------------------------------------------------------------------- live log call ---------------------------------------------------------------------------- 
INFO     C:\WORK\cy_wheel_gens_tests\test_cy_gens.py:test_cy_gens.py:17

Python Version 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:46:45) [MSC v.1924 64 bit (AMD64)]
INFO     C:\WORK\cy_wheel_gens_tests\test_cy_gens.py:test_cy_gens.py:18 inspect.isgeneratorfunction(my_generator_cy): False
INFO     C:\WORK\cy_wheel_gens_tests\test_cy_gens.py:test_cy_gens.py:19 inspect.isgeneratorfunction(my_generator_py): True
INFO     C:\WORK\cy_wheel_gens_tests\test_cy_gens.py:test_cy_gens.py:20 type(my_generator_cy): <class '_cython_3_0_9.cython_function_or_method'>
FAILED                                                                                                                                                           [100%]

============================================================================== FAILURES =============================================================================== 
____________________________________________________________________________ test_cy_gens _____________________________________________________________________________ 

    def test_cy_gens():
        from test_gens.impl import _my_generator as my_generator_cy  # Importing cythonized and installed generator version
        from main import _my_generator as my_generator_py  # Regular python file

        try:
            for i in my_generator_cy():
                print("\ttest:", i)
        except OSError:
            pass

        logger.info(f"\n\nPython Version {sys.version}")
        logger.info(f"inspect.isgeneratorfunction(my_generator_cy): {inspect.isgeneratorfunction(my_generator_cy)}")
        logger.info(f"inspect.isgeneratorfunction(my_generator_py): {inspect.isgeneratorfunction(my_generator_py)}")
        logger.info(f"type(my_generator_cy): {type(my_generator_cy)}")

        assert inspect.isgeneratorfunction(my_generator_py)  # Will pass
>       assert inspect.isgeneratorfunction(my_generator_cy)  # Will fail
E       assert False
E        +  where False = <function isgeneratorfunction at 0x000001BFC87321F0>(<cyfunction _my_generator at 0x000001BFCB0135F0>)
E        +    where <function isgeneratorfunction at 0x000001BFC87321F0> = inspect.isgeneratorfunction

test_cy_gens.py:23: AssertionError
------------------------------------------------------------------------ Captured stdout call ------------------------------------------------------------------------- 
my_generator: 6
        test: 6
my_generator: 12
-------------------------------------------------------------------------- Captured log call -------------------------------------------------------------------------- 
INFO     C:\WORK\cy_wheel_gens_tests\test_cy_gens.py:test_cy_gens.py:17

Python Version 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:46:45) [MSC v.1924 64 bit (AMD64)]
INFO     C:\WORK\cy_wheel_gens_tests\test_cy_gens.py:test_cy_gens.py:18 inspect.isgeneratorfunction(my_generator_cy): False
INFO     C:\WORK\cy_wheel_gens_tests\test_cy_gens.py:test_cy_gens.py:19 inspect.isgeneratorfunction(my_generator_py): True
INFO     C:\WORK\cy_wheel_gens_tests\test_cy_gens.py:test_cy_gens.py:20 type(my_generator_cy): <class '_cython_3_0_9.cython_function_or_method'>
======================================================================= short test summary info ======================================================================= 
FAILED test_cy_gens.py::test_cy_gens - assert False
========================================================================== 1 failed in 0.19s ========================================================================== 

# ...

py39: commands[3]> pytest test_cy_gens.py --log-cli-level=INFO
========================================================================= test session starts =========================================================================
platform win32 -- Python 3.9.6, pytest-8.1.1, pluggy-1.4.0
cachedir: .tox\py39\.pytest_cache
rootdir: C:\WORK\cy_wheel_gens_tests
configfile: pyproject.toml
collected 1 item

test_cy_gens.py::test_cy_gens 
---------------------------------------------------------------------------- live log call ---------------------------------------------------------------------------- 
INFO     C:\WORK\cy_wheel_gens_tests\test_cy_gens.py:test_cy_gens.py:17

Python Version 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)]
INFO     C:\WORK\cy_wheel_gens_tests\test_cy_gens.py:test_cy_gens.py:18 inspect.isgeneratorfunction(my_generator_cy): False
INFO     C:\WORK\cy_wheel_gens_tests\test_cy_gens.py:test_cy_gens.py:19 inspect.isgeneratorfunction(my_generator_py): True
INFO     C:\WORK\cy_wheel_gens_tests\test_cy_gens.py:test_cy_gens.py:20 type(my_generator_cy): <class '_cython_3_0_9.cython_function_or_method'>
FAILED                                                                                                                                                           [100%]

============================================================================== FAILURES =============================================================================== 
____________________________________________________________________________ test_cy_gens _____________________________________________________________________________ 

    def test_cy_gens():
        from test_gens.impl import _my_generator as my_generator_cy  # Importing cythonized and installed generator version
        from main import _my_generator as my_generator_py  # Regular python file

        try:
            for i in my_generator_cy():
                print("\ttest:", i)
        except OSError:
            pass

        logger.info(f"\n\nPython Version {sys.version}")
        logger.info(f"inspect.isgeneratorfunction(my_generator_cy): {inspect.isgeneratorfunction(my_generator_cy)}")
        logger.info(f"inspect.isgeneratorfunction(my_generator_py): {inspect.isgeneratorfunction(my_generator_py)}")
        logger.info(f"type(my_generator_cy): {type(my_generator_cy)}")

        assert inspect.isgeneratorfunction(my_generator_py)  # Will pass
>       assert inspect.isgeneratorfunction(my_generator_cy)  # Will fail
E       assert False
E        +  where False = <function isgeneratorfunction at 0x00000226DAA6B670>(<cyfunction _my_generator at 0x00000226DB6EE520>)
E        +    where <function isgeneratorfunction at 0x00000226DAA6B670> = inspect.isgeneratorfunction

test_cy_gens.py:23: AssertionError
------------------------------------------------------------------------ Captured stdout call ------------------------------------------------------------------------- 
my_generator: 6
        test: 6
my_generator: 12
-------------------------------------------------------------------------- Captured log call -------------------------------------------------------------------------- 
INFO     C:\WORK\cy_wheel_gens_tests\test_cy_gens.py:test_cy_gens.py:17

Python Version 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)]
INFO     C:\WORK\cy_wheel_gens_tests\test_cy_gens.py:test_cy_gens.py:18 inspect.isgeneratorfunction(my_generator_cy): False
INFO     C:\WORK\cy_wheel_gens_tests\test_cy_gens.py:test_cy_gens.py:19 inspect.isgeneratorfunction(my_generator_py): True
INFO     C:\WORK\cy_wheel_gens_tests\test_cy_gens.py:test_cy_gens.py:20 type(my_generator_cy): <class '_cython_3_0_9.cython_function_or_method'>
======================================================================= short test summary info ======================================================================= 
FAILED test_cy_gens.py::test_cy_gens - assert False
========================================================================== 1 failed in 0.16s ========================================================================== 

# ...

py310: commands[3]> pytest test_cy_gens.py --log-cli-level=INFO
========================================================================= test session starts =========================================================================
platform win32 -- Python 3.10.4, pytest-8.1.1, pluggy-1.4.0
cachedir: .tox\py310\.pytest_cache
rootdir: C:\WORK\cy_wheel_gens_tests
configfile: pyproject.toml
collected 1 item

test_cy_gens.py::test_cy_gens 
---------------------------------------------------------------------------- live log call ---------------------------------------------------------------------------- 
INFO     C:\WORK\cy_wheel_gens_tests\test_cy_gens.py:test_cy_gens.py:17

Python Version 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)]
INFO     C:\WORK\cy_wheel_gens_tests\test_cy_gens.py:test_cy_gens.py:18 inspect.isgeneratorfunction(my_generator_cy): False
INFO     C:\WORK\cy_wheel_gens_tests\test_cy_gens.py:test_cy_gens.py:19 inspect.isgeneratorfunction(my_generator_py): True
INFO     C:\WORK\cy_wheel_gens_tests\test_cy_gens.py:test_cy_gens.py:20 type(my_generator_cy): <class '_cython_3_0_9.cython_function_or_method'>
FAILED                                                                                                                                                           [100%]

============================================================================== FAILURES =============================================================================== 
____________________________________________________________________________ test_cy_gens _____________________________________________________________________________ 

    def test_cy_gens():
        from test_gens.impl import _my_generator as my_generator_cy  # Importing cythonized and installed generator version
        from main import _my_generator as my_generator_py  # Regular python file

        try:
            for i in my_generator_cy():
                print("\ttest:", i)
        except OSError:
            pass

        logger.info(f"\n\nPython Version {sys.version}")
        logger.info(f"inspect.isgeneratorfunction(my_generator_cy): {inspect.isgeneratorfunction(my_generator_cy)}")
        logger.info(f"inspect.isgeneratorfunction(my_generator_py): {inspect.isgeneratorfunction(my_generator_py)}")
        logger.info(f"type(my_generator_cy): {type(my_generator_cy)}")

        assert inspect.isgeneratorfunction(my_generator_py)  # Will pass
>       assert inspect.isgeneratorfunction(my_generator_cy)  # Will fail
E       assert False
E        +  where False = <function isgeneratorfunction at 0x000001B8CC1FA170>(<cyfunction _my_generator at 0x000001B8CD2D6A80>)
E        +    where <function isgeneratorfunction at 0x000001B8CC1FA170> = inspect.isgeneratorfunction

test_cy_gens.py:23: AssertionError
------------------------------------------------------------------------ Captured stdout call ------------------------------------------------------------------------- 
my_generator: 6
        test: 6
my_generator: 12
-------------------------------------------------------------------------- Captured log call -------------------------------------------------------------------------- 
INFO     C:\WORK\cy_wheel_gens_tests\test_cy_gens.py:test_cy_gens.py:17

Python Version 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)]
INFO     C:\WORK\cy_wheel_gens_tests\test_cy_gens.py:test_cy_gens.py:18 inspect.isgeneratorfunction(my_generator_cy): False
INFO     C:\WORK\cy_wheel_gens_tests\test_cy_gens.py:test_cy_gens.py:19 inspect.isgeneratorfunction(my_generator_py): True
INFO     C:\WORK\cy_wheel_gens_tests\test_cy_gens.py:test_cy_gens.py:20 type(my_generator_cy): <class '_cython_3_0_9.cython_function_or_method'>
======================================================================= short test summary info ======================================================================= 
FAILED test_cy_gens.py::test_cy_gens - assert False
========================================================================== 1 failed in 0.21s ========================================================================== 

# ...

py311: commands[3]> pytest test_cy_gens.py --log-cli-level=INFO
========================================================================= test session starts =========================================================================
platform win32 -- Python 3.11.4, pytest-8.1.1, pluggy-1.4.0
cachedir: .tox\py311\.pytest_cache
rootdir: C:\WORK\cy_wheel_gens_tests
configfile: pyproject.toml
collected 1 item

test_cy_gens.py::test_cy_gens 
---------------------------------------------------------------------------- live log call ---------------------------------------------------------------------------- 
INFO     C:\WORK\cy_wheel_gens_tests\test_cy_gens.py:test_cy_gens.py:17

Python Version 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)]
INFO     C:\WORK\cy_wheel_gens_tests\test_cy_gens.py:test_cy_gens.py:18 inspect.isgeneratorfunction(my_generator_cy): True
INFO     C:\WORK\cy_wheel_gens_tests\test_cy_gens.py:test_cy_gens.py:19 inspect.isgeneratorfunction(my_generator_py): True
INFO     C:\WORK\cy_wheel_gens_tests\test_cy_gens.py:test_cy_gens.py:20 type(my_generator_cy): <class '_cython_3_0_9.cython_function_or_method'>
PASSED                                                                                                                                                           [100%]

========================================================================== 1 passed in 0.08s ========================================================================== 
  py38: FAIL code 1 (53.58=setup[21.52]+cmd[2.53,24.55,3.75,1.23] seconds)
  py39: FAIL code 1 (49.66=setup[25.39]+cmd[4.56,16.08,2.59,1.03] seconds)
  py310: FAIL code 1 (50.23=setup[22.11]+cmd[2.95,20.11,3.88,1.19] seconds)
  py311: OK (45.53=setup[22.55]+cmd[2.12,17.33,2.53,1.00] seconds)
  evaluation failed :( (199.86 seconds)
```

Note that, in the two assertion present in the `test_cy_gens.py` file, first checks the generator implement in the 
python file and the second one from the library where the same generator was cythonized on `setup.py` file.

Previously, in the code, the cythonized generator is used in a `for` loop showing that it behaves as one.