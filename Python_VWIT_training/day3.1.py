### error handling ###### Exception Handling ####

# try:
#   a=int(input("Enter the number: "))
#   b=int(input("Enter the number: "))
#   print(a/b)
# except:
#   print('number should be integer')


######### assert ##############
# try:
#   age=int(input('Enter a age: '))
#   assert 0 < age, "Only positive numbers accepted."
#   assert age>=15, "Only accept number greater than or equal to 15."
#   print('You entered: ', age)
# except AssertionError as e:
#   print(e)


#######
# enter_again = True

# while enter_again == True:
#   try:
#     age = int(input('Enter your age: '))
#   except ValueError:
#     print ('You have to enter a number!')
#     try:
#       start_again = int(input('To start again, enter 0. To exit,\
#                     press any other key. '))
#     except:
#       print('OK, you do not want to start again, see you soon!')
#       enter_again = False
#     else:
#       if start_again == 0:
#         enter_again = True
#       else:
#         print('OK, you do not want to start again, see you soon!')
#         enter_again = False

# ############ List comprehension ###############
# l1= [i for i in range(2)]
# print(l1)
# l1=[i for i in range(20) if i%2==0]
# print(l1)

############## tuple comprehension python #######
# l1= (i for i in range(2))
# next(l1)
# print(tuple(l1))

########### dictionary comprehension ########

##########functions#############
def hbd():
  print('happy bday')

hbd();hbd();hbd()

def add(a,b):
  print(a+b)

add(3,4)
add(5,6)

def math(a,b):
  c=add(a,b)
  d=add(a,b)
  return c+d,c-d,c*d,c/d

r1,r2,r3,r4=math(5,3)
print(r1)
print(r2)

########## local and global ##########
a=20
add(a,2)
def mul():
  x=20
  y=2
  print(x*y)
  return x*y
mul()

'''
types of argument
positional
keyword
default
variable length single *
'''

#lambda function for single value and used as smaller code

find_max=lambda a,b:a if a>b else b
find_max(5,2)


