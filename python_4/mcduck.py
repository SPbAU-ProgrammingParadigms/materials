#!/usr/bin/env python3

from functools import total_ordering

def add_component(food):
    print(food)


def cutlet():
    add_component("--cutlet--")


def tomatos():
    add_component("#tomatos#")


def make_hamburger():
    add_component("</------\>")
    tomatos()
    cutlet()
    add_component("<\______/>")


# Decorators to the rescue!
def bread(func):
    def wrapper(*args, **kwargs):
        add_component("</------\>")
        func(*args, **kwargs)
        add_component("<\______/>")
    return wrapper


def tomato(func):
    def wrapper(*args, **kwargs):
        add_component("#tomatos#")
        func(*args, **kwargs)
    return wrapper


# порядок важен!
@bread
@tomato
def hamburger(food="--cutlet--"):
    add_component(food)

# hamburger = bread(tomato(hamburger))


def cheese(func):
    def wrapper(*args, **kwargs):
        add_component("***cheese***")
        func(*args, **kwargs)
    return wrapper


@bread
@tomato
@cheese
def cheeseburger(food="--cutlet--"):
    add_component(food)


def decoratorFunctionWithArguments(arg1, arg2, arg3):
    def wrap(f):
        def wrapped_f(*args):
            print("Inside wrapped_f({}, {}, {}):".format(arg1, arg2, arg3))
            f(*args)
            print("After f(*args)")
        return wrapped_f
    return wrap


@decoratorFunctionWithArguments('hello', 1, ("A", 5))
def hello_world():
    print('world')


class Foo:
    @staticmethod
    def bar():
        print("bar")

@total_ordering
class Natural:
    def __init__(self, value):
        self.value = value
    def __lt__(self, other): # Less than
        return self.value < other.value
    def __eq__(self, other):
        return self.value == other.value


if __name__ == '__main__':
    print("hamburger:")
    hamburger()

    print("soy cheeseburger:")
    cheeseburger(food="---соя---")

    hello_world()

    Foo.bar()
    foo = Foo()
    foo.bar()

    a = Natural(2)
    b = Natural(1)
    print("Comparison works:", a >= b)
