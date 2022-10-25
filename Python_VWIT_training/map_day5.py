# def find_length(word):
#   return len(word)
# x = map(find_length, ('apple', 'banana', 'cherry'))
# print('length of words:', list(x))

# ###### two variables
# def add(a,b):
#   return a+b

# x=map(add,(1,2,3),(5,6,7))
# print("result: ",list(x))

# #################### lambda function

# x=map(lambda x:x**2,(5,8,9))
# print("Result: ",list(x))

# ######### Reduce function #####
# def do_sum(x1, x2): 
#     return x1 + x2
# def my_reduce(func, seq):
#     first = seq[0]
#     for i in seq[1:]:
#         first = func(first, i)
#     return first
# print(my_reduce(do_sum, [1, 2, 3, 4]))

# ####################################################
# import functools
# # initializing list
# lis = [1, 3, 5, 6, 2]
# # using reduce to compute sum of list
# print("The sum of the list elements is : ", end="")
# print(functools.reduce(lambda a, b: a+b, lis))
# # using reduce to compute maximum element from list
# print("The maximum element of the list is : ", end="")
# print(functools.reduce(lambda a, b: a if a > b else b, lis))

# ###############################################
# from functools import reduce
# def do_sum(x1, x2):
#     return x1 + x2
# print(reduce(do_sum, [1, 2, 3, 4]))

# ################################################
# from functools import reduce
# print(reduce(lambda x,y:x*y, [1, 2, 3, 4]))

# ######FILTER

# ##### lambda #################
# ages = [5, 12, 17, 18, 24, 32]

# adults = filter(lambda x: x if x>=18 else '', ages)
# print(list(adults))

# ########### check even number
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # returns True if number is even
# def check_even(number):
#     if number % 2 == 0:
#           return True  
#     return False
# # Extract elements from the numbers list for which check_even() returns True
# even_numbers_iterator = filter(check_even, numbers)
# # converting to list
# even_numbers = list(even_numbers_iterator)
# print(even_numbers)

# ########## in vowels
# letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
# # a function that returns True if letter is vowel
# def filter_vowels(letter):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     return True if letter in vowels else False
# filtered_vowels = filter(filter_vowels, letters)
# # converting to tuple
# vowels = tuple(filtered_vowels)
# print(vowels)



# ############## using lambda function #######
# ##### Even Number ############
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# num = filter(lambda x:x if x%2==0 else "",numbers)
# print(list(num))

# ########## Vowels ##############
# letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
# vow = ['a','e','i','o','u']
# vowels = filter(lambda x:x if x in vow else "",letters)
# print(list(vowels))

# ############ Iterators ###########
# t1= ("apple", "banana", "cherry")
# myit = iter(t1)
# print(next(myit))
# print(next(myit))
# print(next(myit))

# ######### iter with class
# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self

#   def __next__(self):
#     x = self.a
#     self.a += 1
#     return x

# myclass = MyNumbers()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# #########  stop iteration  exception 
# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self
#   def __next__(self):
#     if self.a <= 4:
#       x = self.a
#       self.a += 1
#       return x
#     else:
#       raise StopIteration
# myclass = MyNumbers()
# myiter = iter(myclass)
# for x in myiter:
#   print(x)

# ############ generators ##############
# def multiple_yield():  
#     str1 = "First String"  
#     yield str1  
#     str2 = "Second string"  
#     yield str2  
#     str3 = "Third String"  
#     yield str3  
# obj = multiple_yield()  
# print(next(obj))  
# print(next(obj))  
# print(next(obj))  

# ################# list and generator 
# list = [1,2,3,4,5,6,7] 
# # List Comprehension  
# z = [x**3 for x in list]  
# print(z)
# # Generator expression  
# a = (x**3 for x in list)  
# print(a) 
# print(next(a))
'''
########### decorators ######
def greet():
    print('Hello! ', end='')
def mydecorator(fn):
    fn()
    print('How are you?')
mydecorator(greet)

############################
def mydecoratorfunction(some_function): # decorator function
    def inner_function(): 
        # write code to extend the behavior of some_function()
        some_function() # call some_function
        # write code to extend the behavior of some_function()
    return inner_function # return a wrapper function

##################

    #decorator function
def mydecorator(fn):
    def inner_function():        
        fn()
        print('How are you?')
    return inner_function
#applying decorator
@mydecorator
def greet():
  print('Hello! ', end='')
greet()
@mydecorator
def dosomething():
  print('I am doing something.', end='')
dosomething()


############# property decorator
class Student:  
    def __init__(self,name,grade):  
         self.name = name  
         self.grade = grade  
    @property  
    def display(self):  
         return self.name + " got grade " + self.grade  
stu = Student("John","B")  
print("Name:", stu.name)  
print("Grade:", stu.grade)  
print(stu.display) 

######## static decorator ########
class Person:  
     @staticmethod  
     def hello():  
          print("Hello Peter")  
per = Person()  
per.hello()  
Person.hello()
'''

#################### Types of Decorators with arguments #######
## we don't use it much!!
import functools  
def repeat(num):
    #Creating and returning a wrapper function  
    def decorator_repeat(func):  
        @functools.wraps(func)  
        def wrapper(*args,**kwargs):  
            for _ in range(num):  
                value = func(*args,**kwargs)  
            return value  
        return wrapper  
    return decorator_repeat  
#Here we are passing num as an argument which repeats the print function  
@repeat(num=5)  
def function1(name):  
     print(f"{name}")
function1('Hello Python')

######## Types of decorators: stateful decorator ######
import functools
def count_function(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call{wrapper_count_calls.num_calls}​​ of {func.__name__!r}​​")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls  
@count_function  
def say_hello():
    print("Say Hello")  
say_hello()  
say_hello() 

####### classes as decorators ##############
import functools   
class Count_Calls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call{self.num_calls}​​ of {self.func.__name__!r}​​")
        return self.func(*args, **kwargs)  
@Count_Calls  
def say_hello():
    print("Say Hello")  
say_hello()  
say_hello()












