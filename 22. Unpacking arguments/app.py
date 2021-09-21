def multiply(*args):
    # tuple of arguments
    print(args)
    total = 1
    for arg in args:
        total = total * arg

    return total


print(multiply(1, 3, 5))


def add(x, y):
    return x + y


nums = [3, 5]

print(add(*nums))


def add1(x, y):
    return x + y


nums = {"x": 15, "y": 25}

print(add1(**nums))


def multiply1(*args):
    # tuple of arguments
    print(args)
    total = 1
    for arg in args:
        total = total * arg

    return total


def apply(*args, operator):
    if operator == "*":
        # for passing individual numbers as individual numbers and not a tuple
        return multiply1(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided"


print(apply(1, 3, 6, 7, operator="*"))
