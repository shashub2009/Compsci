def abs_value(x):
    """Return the absolute value of x."""
    if x < 0:
        return -x
    else:
        return x

for x in [-10, -5, 0, 5, 10]:
    print(f"The absolute value of {x} is {abs_value(x)}")