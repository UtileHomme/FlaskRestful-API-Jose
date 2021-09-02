def add(x, y):
    return x + y


print(add(5, 7))

# Above function written as lambda function

add_lambda = lambda x, y: x + y

print(add_lambda(5, 7))

print((lambda x, y: x + y)(12, 34))


def double(x):
    return x * 2


sequence = [1, 3, 5]
doubled = [double(x) for x in sequence]

doubled_map = map(double, sequence)

doubled_lambda = list(map(lambda x: x*2, sequence))

print(doubled_lambda)


