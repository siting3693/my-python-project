#https://youtu.be/kr0mpwqttM0?si=Te4loONg8tIvpWB4
#First-Class Function: A programming language is said to have "first-class functions" if it treats functions as first-class citizens.
#First-Class Citizen (or First-Class Object): An entity in a programming language that supports all the operations generally available to other entities. These operations typically include being assigned to a variable, passed as an argument to a function, and returned from a function.

#1. Assigning functions to variables
def square(n):
    return n * n

f = square    # f is also a function because no parentheses means no execution of function
print(square) # Prints the function object
print(f(5))   # Prints 25




#2. Passing functions as arguments (Higher-Order Functions)
def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square, [1, 2, 3, 4, 5])
print(squares) # Prints [1, 4, 9, 16, 25]

def cube(n):
    return n * n * n

cubes = my_map(cube, [1, 2, 3, 4, 5])
print(cubes)





#3. Returning functions from functions
def logger(msg):
    def log_message():
        print('Log:', msg)
    return log_message   #return function as variable, no execution

log_hi = logger('Hi!')        #log_hi is now a log_message function where msg is 'Hi!'
log_hi() #execute log_hi function which is log_message function. Prints 'Log: Hi!'





#4. Practical Example
def html_tag(tag):
    def wrap_text(msg):
        print('<{0}><{1}></{0}>'.format(tag, msg))
    return wrap_text

print_h1 = html_tag('h1')  #'h1' is tag
print_h1('Test Headline')  #'Test Headline' is msg












print('\n\n\n')
#https://youtu.be/FsAPt_9Bf3U?si=4AX3r2f_F7fU9Jni
#Decorators
def outer_function():
    message = 'Hi'

    def inner_function():
        print(message)
    return inner_function

my_func = outer_function()    #my_func = inner_function
my_func()                     #execute my_func means executing inner function (=inner_function())




def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

hi_func = outer_function('Hi')
hi_func()




def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function

def display():
    print('display function ran')

decorated_display = decorator_function(display)        #display function as an argument is sent to decorator_function, decorated_function is now wrapper_function which the original_function is display
decorated_display()                                    #execute wrapper_function and means executing original_function() since it returns original_function() (with brackets!)




def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function

def display():
    print('display function ran')

display = decorator_function(display)        #this line also same as @decorator_function written before def display():
display() 




@decorator_function
def display2():
    print('display function2 ran')

display2()




def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):                  #add *args and **kwargs because maybe the original function needs parameters but we dont know how much parameters needed
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Justin',18)





def changecase(func):
  def myinner():
    return func().upper()      #"Hello Sally".upper() because myfunction() return "Hello Sally"
  return myinner

def myfunction():
  return "Hello Sally"

myfunction = changecase(myfunction)
print(myfunction())




#SAME AS
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())
