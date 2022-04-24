# def get_int_as_str(number):
#     return str(number)

# def print_int(my_function, number):
#     print(my_function(number))
#     return

# print_int(get_int_as_str, 130)


##----------------------------------------------------------##


# def get_int_as_str(number):
#     print(str(number))
#     return

# def print_int(my_function,number):
#     return my_function(number)

# print_int(get_int_as_str, 130)


##----------------------------------------------------------##


# def print_int(number):

#     def get_int_as_str(number):
#         print(str(number))
#         return

#     get_int_as_str(number)
#     return

# print_int(130)


##----------------------------------------------------------##


# def print_init(number):
    

#     def get_int_as_str(number):
#         print(str(number))
#         return

#     return get_int_as_str(number)


# print_init(130)


##----------------------------------------------------------##


# def print_init(number):
    

#     def get_int_as_str(number):
#         print(str(number))
#         return number

#     return get_int_as_str(number)


# @print_init
# def hello_world(text_content):
#     print(text_content)
#     return

# hello_world("hello Worl")


##----------------------------------------------------------##


# def print_int(my_function):

#     def any_function():
#         return my_function

#     return any_function()

# @print_int
# def get_int_as_str(number):
#     print(str(number))
#     return

# get_int_as_str(130)


##----------------------------------------------------------##


# from time import time

# def timer(any_function):
#     def count_time():
#         start = time()
#         any_function()
#         stop = time()
#         print(stop-start, 'seconds')
#         return any_function()
#     return count_time()

# @timer
# def hello():
#     print("hello world")
#     return

# hello()