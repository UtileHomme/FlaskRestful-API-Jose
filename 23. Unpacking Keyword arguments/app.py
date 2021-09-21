def named(**kwargs):
    print(kwargs)


named(name="Bob", age=25)


def names(name, age):
    print(name, age)


details = {"name": "Bob", "age": 25}

names(**details)


def namel(**kwargs):
    print(kwargs)


def print_nicely(**kwargs):
    namel(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")


print_nicely(name="Bob", age=25)


def both(*args, **kwargs):
    print(args)
    print(kwargs)


both(1, 3, 5, name="Bob", age=25)


def myfunction(**kwargs):
    print(kwargs)

# The below will give an error
# myfunction(**"bob")
# myfunction(**None)
