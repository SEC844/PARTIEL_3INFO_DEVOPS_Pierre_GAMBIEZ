def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b


def greet(name):
    if name == "":
        return "Hello, World!"
    return f"Hello,{name}"
