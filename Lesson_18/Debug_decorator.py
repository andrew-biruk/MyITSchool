# Create decorator "debug" which, by every call of decorated function,
# shows the func name, all the arguments passed and its return value.
# Afterwards, the result is shown.

def debug(func):
    def wrap(*args, **kwargs):

        pos_args = [str(arg) for arg in args]
        key_args = [f"{k}={v}" for k, v in kwargs.items()]
        func_args = ", ".join(pos_args) + ", ".join(key_args)
        return_value = func(*args, **kwargs)

        print(f"Call to: {func.__name__}({func_args}); return: {return_value}")
        return return_value
    return wrap


@debug
def add_concat(a, b):
    return a + b


add_concat(3, 5)
add_concat(a="Py", b="thon")
