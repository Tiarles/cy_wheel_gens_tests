import sys
import inspect
import logging
    
logger = logging.getLogger(__file__)


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
    assert inspect.isgeneratorfunction(my_generator_cy)  # Will fail
