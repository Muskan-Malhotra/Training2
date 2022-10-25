########## class and object ######
# class Math:
#   n1=20
#   n2=30
#   def add(self,a,b):
#     print(a+b)

# m1=Math()
# print(m1.n1)
# print(m1.n2)
# m1.add(m1.n1,m1.n2)
# m1.add(5,6)
# Math.add(2,9) # without self it will work


###########################################
# class Math:
#        n1=20
#        n2=30
#        def add(self,a,b):
#               print(a+b)
         
#        def subtract(self,a,b):
#             print(a-b)
         
#        def multiply(self,a,b):
#               print(a*b)
         
#        def divide(self,a,b):
#             print(a/b)
    

 

# m1=Math()
# print(m1.n1)
# print(m1.n2)
# m1.add(m1.n1,m1.n2)
# m1.add(5,6)
# print("*****************")
# #Here object m2 is created of class math
# m2 = Math()
# #Calling N1 with M2 Object
# print(m2.n1)
# #Calling N2 With M2 Object
# print(m2.n2)
# #Calling the function 
# m2.add(10,100)
# m2.subtract(10,5)
# m2.multiply(10,5)
# m2.divide(10,5)


# ###########################################

# class Math:
#   n1=20
#   n2=30
#   def add(self,a,b):        
#     print(a+b)

# m1 = Math()
# m1.add(m1.n1,m2.n2)

# m2 = Math()
# m2.n1=80 # update the existing attribute's  value
# m2.n3 = 60  # add new attribute
# m2.add(m2.n1,m2.n3)

# del m2.n1 #delete updated value member 
# del m2 #delete the object


# ######## doc string shows the information related to class #######
# class Math:
#   'this is class doc string'
#   n1=20
#   n2=30
#   def add(self,a,b):        
#     print(a+b)

# m1 = Math()
# print(m1.__doc__)


# #### return class #####
# # class type after mention 'object'
# class Myclass(object):
#             pass
# print("Myclass:",Myclass.__bases__)

# #number class type
# class Mynumber(int):
#             pass
# print("Mynumber:", Mynumber.__bases__)

# #string class type
# class Mystring(str):
#             pass
# print("Mystring:",Mystring.__bases__)

# # class type without mention 'object'
# class Mynewclass:
#     pass
# print("Mynewclass:",Myclass.__bases__)


# ##############################
# class Mynumber:
#   "This is a python number class"
#   num='integer number'
#   def add(a,b):
#     c=a+b
#     return c
# print("name: ",Mynumber.__name__) # access class name
# print("doc: ",Mynumber.__doc__) # access doc string
# print("module: ",Mynumber.__module__) # access class module
# print("base class name: ",Mynumber.__bases__) # access base classe
# print("Is object a base class for Mynumber? ",[object in cls.__bases__ for cls in {Mynumber}])
# print("dict: ",Mynumber.__dict__) # access class namespace dict



# ###############################
class Employee:
         id=211
         name='Rimi'
e1= Employee()
print("id is exist? ",hasattr(e1,'id')) # returns true if 'id' attribute exists
print("get name value: ",getattr(e1,'name') ) # returns value of 'id' attribute
setattr(e1,'designation','HR')  # set attribute 'designation' at 'HR'
print("added new value: ",  e1.designation)
delattr(e1,'designation') #delete attribute 'designation'
# print( e1.designation)












