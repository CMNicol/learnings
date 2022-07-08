
# Define a decorator method
def a_decorator(function_we_are_decorating):

    def inner_method():
        print("Inner method start.")
        function_we_are_decorating()
        print("Inner method end.")

    return inner_method

#  Decorating a method without using @
def hello_world():
    print("hello world")

print_hello_world = a_decorator(hello_world)
print_hello_world()


# Decorating a method using @
@a_decorator
def hello_world():
    print("hello world")

hello_world()
