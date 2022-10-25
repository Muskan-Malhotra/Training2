# ########## parameterised constructor ########

# class Employee:
#   def __init__(self,id,name,designation):
#     self.ID = id
#     self.Name = name
#     self.Designation = designation
#   def display(self):
#     print(self.ID,self.Name,self.Designation)

# E1=Employee(10,"John","HR")
# E1.display()

 
# ############## Without Parameters ###########
# class Employee:
#   def __init__(self):
#     pass
#   def display(self,ID,Name,Designation):
#     print(ID,Name,Designation)

# E1=Employee()
# E1.display(10,"John","HR")

########### task ##############
'''
class Company:
  def __init__(self):
    pass
  
  def display(self,ID,Name,totl_cust,tot_policy):
    print(ID,Name,totl_cust,tot_policy)

  def display(self,ID,Name,totl_policy,pan):
    print(ID,Name,totl_policy,pan)

  def display(self,ID,Name,salary,pan):
    print(ID,Name,salary,pan)

advisor = Company()
advisor.display(1041,"John",50,25)

customer = Company()
customer.display(1033,"Peter",55,"GPMJK654L")

employee = Company()
employee.display(1035,"Catherine",25000,"GHJKL9870L")

'''
################### Trainer ##################
'''
class User:
  def __init__(self):
    self.id = id
    self.name = nm
    self.totl_policy = tp
  
  def display(self,name,tp):
    return self.id,self.name,self.totl_policy

advisor = User(11001,"John",20)
advisor.total_cust=30
r1,r2,r3=advisor.display()
print(r1,r2,r3,advisor.total_cust)

customer = User(22001,"Peter",5)
customer.pan="LKJHN9807L"
r1,r2,r3=customer.display()
print(r1,r2,r3.customer.pan)

employee = User(33001,"Mark",50)
employee.pan="LUNHY9876O"
employee.salary=30000
employee.total_advisor= 10
r1,r2,r3 = advisor.display()
print(r1,r2,r3,employee.total_advisor,employee.salary, employee.pan)


'''

############################################### actual correct code
'''
class User:
  def __init__(self,id,nm,tp):
    self.id=id
    self.name=nm
    self.total_policy=tp

  def display(self):
    return self.id , self.name, self.total_policy
advisor=User(1011,'John',20)
advisor.total_cust=20
r1,r2,r3=advisor.display()
print(r1,r2,r3,advisor.total_cust)

customer=User(11,'Peter',5)
customer.pan='NJHK1452GHJ'
r1,r2,r3=customer.display()
print(r1,r2,r3,customer.pan)

employee=User(100,'Mark',50)
employee.total_advisor=10
employee.pan='LKJH1245UIO'
employee.sal=50000
r1,r2,r3=advisor.display()
print(r1,r2,r3,employee.total_advisor,employee.pan,employee.sal)

'''
######################################### adding multiple objects #############
# object_data=[]
# class User:
#   def __init__(self,id,nm,tp):
#     self.id=id
#     self.name=nm
#     self.total_policy=tp

#   def display(self):
#     return self.id , self.name, self.total_policy
  
#   def add(self,obj):
#     object_data.append(obj)

# id1=[]
# name=[]
# t_p=[]
# n=int(input("How many user's wants to add?"))
# for i in range(n):
#   id=input('enter id: ')
#   nm=input('enter name: ')
#   tp=input('enter total policy: ')
#   u1 = User(id,nm,tp)
#   u1.add(u1)
#   print("")
#   r1,r2,r3=u1.display()
#   id1.append(r1)
#   name.append(r2)
#   t_p.append(r3)
# print("")
# for i in range(len(id1)):
#   print(id1[i],name[i],t_p[i])


############public private protected ##########

'''
class Cup():
  def __init__(self):
    self._content_="Tea"
  def Fill(self):
    print(self._content_)

c=Cup()
c.Fill()

'''
##########################################
'''
from datetime import datetime
now=datetime.now()
print("repr representation of datetime: ",repr(now))
print("str representation of datetime: ",str(now))
'''
###########################################
'''
class Box():
        def __init__(self,x,y):
                self.x=x
                self.y=y
        def __str__(self):
                return "str value is'%s'"%self.x
        def __repr__(self):
                return "repr value is'%s'"%self.x
        def __del__(self):
                class_name = self.__class__.__name__
                print(class_name,"destroyed")
b1=Box(10,20)
print(str(b1)) # str representation
print(repr(b1)) # repr representation
b2=b1 # create 'b2' object
del b2 # delete 'b2' object
print(b1)
'''
########################################
'''
class Bird:
  color='brown'
  height='small'

class sparrow(Bird):
  look='tiny'

B1=Bird()
print(B1.color,B1.height)

s1=sparrow()
print(s1.color,s1.height,s1.look)
'''
####### multiple inheritance ########
'''
class BirdF:
  color='brown'
class BirdM:
  height='small'

class sparrow(BirdF,BirdM):
  look='tiny'

s1=sparrow()
print(s1.color,s1.height,s1.look)
'''

######################################
'''
class Point:
  def __init__(self, x , y ):
    self.x = x
    self.y = y
  def __str__(self):
    return "Point(%d,%d)"%(self.x,self.y)
  def __add__(self,other):
    x = self.x + other.x
    y = self.y + other.y
    return Point(x,y)

p1=Point(2,3)
print('p1 data:',p1)
p2=Point(-1,2)
p3=p1+p2 # Call method by using operator
print(p3)
print(p1.__add__(p2)) # call method by name
print(Point.__add__(p1,p2)) # call method name with class
'''

##########################################
'''
class Point:
  def __init__(self, x , y ):
    self.x = x
    self.y = y

  def  __str__(self):
    return"Point(%d,%d)"%(self.x,self.y)

  def __add__(self,other):
    x = self.x + other.x
    y = self.y + other.y
    return Point(x,y)
  def __sub__(self,other):
    x=self.x-other.x
    y=self.y-other.y
    return Point(x,y)
  def __mul__(self,other):
    x=self.x*other.x
    y=self.y*other.y
    return Point(x,y)
  def __truediv__(self,other):
    x=self.x/other.x
    y=self.y/other.y
    return Point(x,y)

 
p1=Point(2,3)
print('p1 data:',p1)
p2=Point(-1,2)
p3=p1+p2# Call method by using operator
print(p3)
print(p1.__add__(p2)) # call method by name
print(Point.__add__(p1,p2)) # call method name with cla
print(p1.__sub__(p2)) 
print(Point.__sub__(p1,p2))
print(p1.__mul__(p2)) 
print(Point.__mul__(p1,p2))
print(p1.__truediv__(p2)) 
print(Point.__truediv__(p1,p2))
'''
##################################################
'''
class Point:
    def __init__(self, x , y ):
        self.x = x
        self.y = y
    def __lt__(self,other):
        self_mag = (self.x ** 2) + (self.y ** 2)
        other_mag = (other.x ** 2) + (other.y ** 2)
        return self_mag < other_mag 
p1=Point(1,1)
p2=Point(-2,-3)
p3=p1< p2 # call method by using operator
print(p3)
print(p1.__lt__(p2)) # call method by name
print(Point.__lt__(p1,p2)) # call method name with class


'''
############ checking if object or not!! #######################
# class Calci1:  
#     def Sum(self,a,b):  
#         return a+b 
# class Calci2():  
#     def Div(self,a,b):  
#         return a/b
# c1=Calci1() 
# c2 = Calci2()  
# print(isinstance(c1,Calci2))

# ############is a sub class ? ####################
# class Calci1:  
#     def Sum(self,a,b):  
#         return a+b 
# class Calci2:  
#     def Mul(self,a,b):  
#         return a*b  
# class Calci3(Calci1,Calci2):  
#     def Div(self,a,b):  
#         return a/b  
# print(issubclass(Calci3,Calci2))  
# print(issubclass(Calci1,Calci2)) 


# ############ Operator Overiding ##############
# class Animal: 
#     def speak(self): 
#         print("speaking") 
# class Dog(Animal): 
#     def speak(self): 
#         print("Barking") 
# d = Dog() 
# d.speak()

# ########## Encapsulation #################
# class Bag:
#    def __init__(self):
#       self.a = "Bag-a"
#       self._b = "Bag-b"
#       self.__c = "Bag-c"
# b1 = Bag()
# print("a value:",b1.a)
# print("b value:",b1._b)
# print("c value:",b1._Bag__c)
# # print("c value:",b1.__c)

################## data abstraction ###############
'''
class Employee:
  __count = 0
  def __init__(self):
    Employee.__count=Employee.__count+1
  def display(self):
    print("The number of employees",Employee.__count)

e1=Employee()
e1.display()
e2=Employee()
e2.display()
# print(e1.__count)

###############################################################
class Employee:
  __count = 0
  def __init__(self):
    Employee.__count = Employee.__count+1
  def display(self):
    print("The number of employees",Employee.__count)
e1 = Employee()
e1.display()
e2 = Employee()
e2.display()
# print(e1.__count) #not printed coz private

##################### Polymorphism #############
class Cat:
  def sound(self):
          print ("meow!")
class Dog:
  def sound(self):
          print ("Woof woof!")
def makeSound(animalType):
  animalType.sound()

catObj = Cat()
dogObj = Dog()
makeSound(catObj)
makeSound(dogObj)

'''
##################### Using super ############
'''
class Base1:
  def __init__(self):
    super().__init__()
    self.name='kapil dev'

class Base2:
  def __init__(self):
    super().__init__()
    self.occupation='player'
class Base3:
  def __init__(self):
    self.best_score=175
    

class Child(Base2,Base1,Base3):
  def __init__(self):
    super().__init__()
    self.win= '1983' #child member
ch=Child()
print(Child.__mro__)
print(ch.__dict__)


'''

######################################3
#not use super in parent class
'''
class Base1:
  def __init__(self):
    self.name='kapil dev'

class Base2:
  def __init__(self):
    self.occupation='player'
class Base3:
  def __init__(self):
    self.best_score=175
class Child(Base2,Base1,Base3):
  def __init__(self):
    super().__init__()
    self.win= '1983' #child member
ch=Child()
print(Child.__mro__)
print(ch.__dict__)
'''
###############################################
'''
class Base1:
  def __init__(self):
    self.name='kapil dev'
        

class Base2:
  def __init__(self):
    self.occupation='player'

class Base3:
  def __init__(self):
    self.best_score=175

class Child(Base2,Base1,Base3):
  # def __init__(self): #won't work like this
  def __init__(self):
    #Base1.__init__(self)  #this won't work until
    Base1.__init__(self)  ## pass in the init of child and parent equally
    Base2.__init__(self)
    Base3.__init__(self)
    self.win= '1983' #child member

ch=Child()
print(Child.__mro__)  ###just to provide information about how super is flowing
print(ch.__dict__)
'''

'''
class Base1:
  def __init__(self,name):
    self.name=name

class Base2:
  def __init__(self):
    self.occupation='player'
class Base3:
  def __init__(self):
    self.best_score=175
class Child(Base2,Base1,Base3):
  def __init__(self,name):
    Base1.__init__(self,name)
    Base2.__init__(self)
    Base3.__init__(self)
    self.win= '1983' #child member
ch=Child('john')
print(Child.__mro__)
print(ch.__dict__)

'''
############ using parent function mutlilevel ###########
'''
class parent:
  def __init__(self):
    super().__init__()
    self.game='cricket'

class base1(parent): #parent is called
  def __init__(self):
    super().__init__()
    self.name='kapil dev'
class base2(parent):
  def __init__(self):
    super().__init__()
    self.occupation='player'
class base3:
  def __init__(self):
    super().__init__()
    self.best_score=175
class child(base1,base2,base3):
  def __init__(self):
    super().__init__()
ch=child()
print(child.__mro__)
print(ch.__dict__)


'''
######### multi level ##########
'''
class parent:
  def __init__(self):
    super().__init__()
    self.game='cricket'

class base1(parent):
  def __init__(self):
    super().__init__()
    self.name='kapil dev'
class base2(base1):
  def __init__(self):
    super().__init__()
    self.occupation='player'
class base3:
  def __init__(self):
    self.best_score=175
class child(base2,base3):
  def __init__(self):
    super().__init__()
ch=child()
print(child.__mro__)
print(ch.__dict__)

'''

############## POLYMORPHISM OVERIDING Using this method ########
#polymorphishm overriding
'''
class person:
  def __init__(self):
    self.name='person'
    super().__init__()

  def display(self):
    print(self.name)
class student(person):
  def __init__(self):
    self.course='java'
    super().__init__()

  def display(self):
    print(self.name)
    print(self.course)

st=student()
st.display()
'''
#### abstract method which we can extract in children ######
'''
from abc import ABC,abstractmethod
class switch(ABC):
  @abstractmethod
  def switch_on():
      pass

  @abstractmethod
  def switch_off():
      pass

class plastic_switch(switch):
    def switch_on():
        print('plastic swtich on')

    def switch_off():
        print('plastic swtich off')
class wifi_switch(switch):
  def switch_on():
    print('wifi swtich on')

  def switch_off():
    print('wifi swtich off')

class Fan:
  def __init__(self,switch):
    self.state=False
    self.switch=switch

  def get_state(self):
    return self.state
  def turn_on(self):
    self.state=True
    switch.switch_on()
  def turn_off(self):
    self.state=False
    switch.switch_off()

pl_sw=plastic_switch()
fn=Fan(pl_sw)
fn.turn_on()
print(fn.get_state())
fn.turn_off()
print(fn.get_state())


'''






