def fun1(x, y):
    """Add two numbers"""
    return x + y


def fun2(x, y):
    """Subtract y from x"""
    return x - y


def fun3(x, y):
    """Multiply two numbers"""
    return x * y


def fun4(x, y):
    """
    Combine results of fun1, fun2, and fun3
    and return their sum
    """
    return fun1(x, y) + fun2(x, y) + fun3(x, y)
