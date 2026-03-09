##Are powerful tool for modifying or extending 
##the behavior of functions without changing their code.
# They are used to add functionality to existing functions in a clean and reusable way.

#JS callback functions are similiar to decorators in python.
#  They are functions that are passed as arguments to other functions and are executed 
# after a certain event or condition is met.

# create simple decorator
# Have multiple function that use the docorator
# Remove the function call inside the decorator
#see original function is not called.

import time

def time_taken(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        print(f"Executing {func.__name__}...")
        result=func(*args,**kwargs)
        end_time=time.time()
        print(f"Time taken: {end_time-start_time} seconds")
    return wrapper

def my_dec(func):
    def wrapper():
        print("Before the function is called")
        func()
        print("After the function is called")
    return wrapper

@my_dec
def say_hello():
    print("Hello!")

@my_dec
def my_name_is():
    print("My name is John")

@time_taken
def add(a,b):
    print("a is",a)
    print("b is",b )
    sum=a+b
    print("Sum is",sum)

@time_taken
def long_process():
    for i in range(1000000000):
        k=i*2
    

# add(10,12)

long_process()

## add(10,12) ->my_dec()=>wrapper()->func()
## it calls it without inputs
##  args, and kwargs 
## add(args,kwargs)->my_dec(arrgs,kwargs)->wrappper(args,kwargs)->func(args,kwargs)