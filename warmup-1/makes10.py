def makes10(a, b):
    """Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10."""
    if a == 10 or b == 10 or a + b == 10:
        return True
    else:
        return False


print(makes10(9, 10))
print(makes10(9, 9))
print(makes10(9, 10))
