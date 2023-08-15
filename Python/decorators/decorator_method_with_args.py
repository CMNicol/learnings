# Define a decorator method
def a_decorator(function_we_are_decorating):
    def inner_method(*args, **kwargs):
        print("Inner method start.")
        function_we_are_decorating(*args, **kwargs)
        print("Inner method end.")

    return inner_method


#  Decorating a method without using @
def say_something(something):
    print(something)


print_hello_world = a_decorator(say_something)
print_hello_world(something="I'm giving up on you.")


# Decorating a method using @
@a_decorator
def say_something(something):
    print(something)


say_something(something="I'm giving up on you.")
