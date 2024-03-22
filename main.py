def _my_generator():
    value = 6
    print("my_generator:", value)
    yield value
    value = value + 6
    print("my_generator:", value)
