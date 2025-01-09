"""Module to perform operations based on the input values."""

def f(x, y):
    """Performs operations based on the conditions for x and y."""
    if x < 0 or y < 0:
        return 0
    if x % 2 == 0 and y % 2 == 0:
        return x + y
    if x % 2 == 0 and y % 2 != 0:
        return x - y
    if x % 2 != 0 and y % 2 == 0:
        return x * y
    if x % 2 != 0 and y % 2 != 0:
        return x / y
    return -1


def g(x, y):
    """Calculates a sum based on the modulo of x and y."""
    if x < 0 or y < 0:
        return 0
    s = 0
    for i in range((x + y) % 2):
        s += i
    return s


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = f(a, b)
    d = g(a, b)
    print(c)
    print(d)   
