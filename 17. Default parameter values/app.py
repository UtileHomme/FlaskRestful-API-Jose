def add(x, y=8):
    print(x + y)


add(5)

default_y = 3


def add(x, y=default_y):
    print(x + y)


add(5)

default_y = 2

add(4)
