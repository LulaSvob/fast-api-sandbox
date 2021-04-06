# Region

# def say_hello(name):
#     return f"Hello {name}"
#
#
# def be_awesome(name):
#     return f"Yo {name}, together we are the awesomest!"
#
#
# def greet_bob(greeter_func):
#     return greeter_func("Bob")
#
#
# print(greet_bob(say_hello))
# print(greet_bob(be_awesome))
#
#
# def parent(num):
#     def first_child():
#         return "Hi, I am Emma"
#
#     def second_child():
#         return "Call me Liam"
#
#     if num == 1:
#         return first_child
#     else:
#         return second_child
#
#
# first = parent(1)
# second = parent(2)
#
# print(first())
# print(second())

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
#
#
# @my_decorator
# def say_whee():
#     print("Whee!")
#
#
# say_whee()

# say_whee = my_decorator(say_whee)
# say_whee()
import math
import random

from decorators import debug, slow_down, register, PLUGINS

#
# @do_twice
# def say_whee():
#     print("Whee!")
#
#
# say_whee()
#
#
# @do_twice
# def greet(name):
#     print(f"Hello {name}")
#
#
# greet("World")
#
#
# @do_twice
# def return_greeting(name):
#     print("Creating greeting")
#     return f"Hi {name}"
#
#
# hi_adam = return_greeting("Adam")
#
# print(hi_adam)
#
#
# @timer
# def waste_some_time(num_times):
#     for _ in range(num_times):
#         # print(sum([i**2 for i in range(10000)]))
#         sum([i ** 2 for i in range(10000)])
#
#
# waste_some_time(5)
#
# @debug
# def make_greeting(name, age=None):
#     if age is None:
#         return f"Howdy {name}!"
#     else:
#         return f"Whoa {name}! {age} already, you are growing up!"
#
#
# make_greeting("Richard", age=112)

math.factorial = debug(math.factorial)  # Apply a decorator to a standard library function


def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))


# print(approximate_e())


@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)


# countdown(100)


@register
def say_hello(name):
    return f"Hello {name}"


@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"


def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)


# print(randomly_greet("Bubitu"))



