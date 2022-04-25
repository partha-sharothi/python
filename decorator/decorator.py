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
#         return any_function

#     return count_time()

# @timer
# def hello():
#     print("hello world")
#     return

# hello()

# @timer
# def another_function():
#     for item in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#         print(item)
#     return

# another_function()


##--------------------------  @classmethod  --------------------------------##



# class MyClass:
#     """Simple class to define something"""
#     def __init__(self):
#         pass

#     def square(self, x):
#         return x**2

#     @classmethod
#     def cube(self, x):
#         return x**3

# if __name__ == "__main__":
#     myclass = MyClass()
#     print(myclass.square(3))
#     print(myclass.cube(3))
#     print(MyClass.cube(3))
#     print(MyClass.square(3))



##--------------------------  @staticmethod  --------------------------------##


# class MyClass:
#     """simple class to define something"""

#     def __init__(self):
#         pass

#     def square(self, x):
#         return x**2

#     @staticmethod
#     def cube(x):
#         return x**3


# if __name__ == "__main__":
#     myclass = MyClass()
#     print(myclass.square(3))
#     print(myclass.cube(3))
#     print(MyClass.cube(3))
#     print(MyClass.square(3))



##--------------------------  @property  -------- we can use it as read only property or getter method ------------------------##


class MyClass:
    """simple class to define something"""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

if __name__ == "__main__":
    myclass = MyClass('partha', 'sharothi')
    print(myclass.full_name)
    myclass.full_name = 'New Name'
