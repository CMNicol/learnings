# Define a decorator method
def a_decorator(function_we_are_decorating):
    def inner_method():
        print("Inner method start.")
        value = function_we_are_decorating()
        print("Inner method end.")
        return value

    return inner_method

#  Decorating a method without using @
def say_something():
    return "Something returned"

print_hello_world = a_decorator(say_something)
value_returned = print_hello_world()
print(value_returned)


# Decorating a method using @
@a_decorator
def say_something():
    return "Something returned"

value_returned = say_something()
print(value_returned)