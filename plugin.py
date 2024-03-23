import pytest

@pytest.hookimpl(hookwrapper=True)
def pytest_runtestloop(session):
    print("Before the pytest_runtestloop loop.")
    yield
    print("After the pytest_runtestloop loop.")
