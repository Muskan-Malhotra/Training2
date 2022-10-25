# # data={}
# # data = [{"name":"apple","Price":"500"},{"name":"banana","price":"1500"}]


# # name=[]
# # price=[]
# # for i in data:
# # #{​​'name':'bitcoin','price':500}​​
# #   for j in i:
# # #'name','price'
# #     if j == 'name':
# #       name.append(i[j])
# #     else:
# #       if i[j].isnumeric():
# #         price.append(int(i[j]))


# # print(name)
# # print(price)

# # lst = ['51','52','53']
# # for i in lst:
# #   if i.isnumeric():  #return true if it is a numeric string
# #     print(i)


# '''
# [10:29] Saurika  Tiwary(Vatika82-N) (Guest)
#     price=[500, 1500, 500, 1500, None]
# ​[10:30] Saurika  Tiwary(Vatika82-N) (Guest)
#     name= ['bitcoin', 'bitcoins','bitcoin', 'bitcoins', 'abc']
# ​[10:30] Saurika  Tiwary(Vatika82-N) (Guest)
#     for i in range(len(price)):
# if price[i]==None:
# price.pop(i)
# name.pop(i)
# ​[10:30] Saurika  Tiwary(Vatika82-N) (Guest)
#     print(name,price)
# '''



# ## persons data that starts with j
# names=['john thomas','Sam','Lily','JOHN','Jonas Mark','Peter','John','Lee']

# for i in names:
#   if i.startswith('j') or i.startswith('J'):
#     print(i)

# ######### Exercise 2 #########
# task = 'welcome python and JOY class'

# for i in range(len(task)):
#   if(task[i].lower()=='o'):
#     print(i)


# ########## armstrong number ##############
# num = input("Enter the number: ")
# temp = int(num)
# lgt = len(list(num))

# ans = 0
# while(temp>0):
#   rem = temp%10
#   temp = temp//10  ##--> changes to 
#   ans = ans+rem**lgt

# if(ans == int(num)):
#   print("Is an armstrong number")
# else:
#   print("Not an armstrong number")

# #############part 2 ################
# num = input("Enter the number: ")

# n = len(num) #3
# res=0
# for i in num:
#   res = int(i)**n+res

# if(res == int(num)):
#   print("%s Is an armstrong number" %num)
# else:
#   print("%s Not an armstrong number" %num)



# ###############Leap year ##############
# y = 2025
# if( y%4 == 0 and y%100 == 0):
#   print("Leap year")
# else:
#   print("Not leap year")

# ###############temp check #############
# temp=35;rain='no';hum=50
# if temp == 15 and rain == 'no' and hum == 20:
#   print('cold day')
# elif temp == 35 and rain == 'no' and hum == 50:
#   print('hot day')
# elif rain=='yes':
#   print('rainy day')
# else:
#   print('normal day')


# ###############################################
# UN = input('enter un: ')

# if UN == 'admin':
#   PW=input('enter pw: ')
#   if PW=='admin1234':
#     print('success')
#   else:
#     print('invalid username')
    

# ################# QUESTION ########################
# '''
# bank application
# deposit -> 1,50,000
# if deposit -> more than 5,00,000  
# 2) deposit ->20,000 to 5,00,000
# 3)deposit -> 1000-20,000
# 4) deposit -> 1000, less than 1000 -> i deposit right now
# '''
# #############################################

# deposit = int(input("Enter the amount to be deposited: "))
# if(deposit == 150000):
#   print("Thank you for depositing")
# elif(deposit>500000):
#   print("Need to deposite PAN card copy")
# elif(deposit >=20000 and deposit<500000):
#   print("Please print your receipt")
# elif(deposit >=1000 and deposit<20000):
#   print("Thank you for choosing us!")
# elif(deposit<1000):
#   print("Need to maintain minimum balance as per policies")



# ################# ODD EVEN #############################

# for i in range(1,20,2):
#   print(i+1)



# l1=[5,8,9,'a','n','b']
# for i in range(len(l1)):
#   print(l1[i])


# a=2
# while a>0:
#   print(a)
#   a=a-1

# for i in range(7):
#   for j in range(7):
#     print('j',end='')
#   print(i)

# '''
# jjjjjjj0
# jjjjjjj1
# jjjjjjj2
# jjjjjjj3
# jjjjjjj4
# jjjjjjj5
# jjjjjjj6
# '''

# for i in range(7):
#   for j in range(i):
#     print('j',end='')
#   print(i)
# '''
# 0
# j1
# jj2
# jjj3
# jjjj4
# jjjjj5
# jjjjjj6
# '''
# for i in range(6,0,-1):
#   for j in range(i):
#     print('j',end='')
#   print(i)

# '''
# jjjjjj6
# jjjjj5
# jjjj4
# jjj3
# jj2
# j1
# '''
  
# for i in range(7):
#   for j in range(i):
#     print('j',end='')
#   print(i)  
# for i in range(7):
#   for j in range(6-i):
#     print('j',end='')
#   print("i")

# i=0;j=0
# while(i<7):
#   while(j<i):
#     print("j",end="")
#     j = j+1
#   print('i')
#   i+=1
#   j=0


    

# for i in range(1,7):
#   for j in range(1, i+1):
#     print(i, end="")
#   print()

# for i in range(1,7):
#   for j in range (1,i):
#     print(j,end='')
#   print()

'''
1
12
123
1234
12345
'''

# for i in range(1,7):
#   for j in range (i):
#     print(i,end='')
#   print()


'''
1
22
333
4444
55555
666666
'''



from random import *
random()
randrange(1,10,2)
randrange(1,10,2)
randrange(1,10,2)

randint(1,6)

uniform(1,5)
uniform(1,5)

choice('python')
choice('python')
choice('python')

from math import *
sqrt(16)

round(2.3456,3)
s1='python'
l1=[2,5,'l','k','o','p']
shuffle(l1)
l1


###############QUESTION####################
'''
guessing num -> random number from 1 to 20
player enter the number from 1 to 20

guessing num...random number from 1-20

player....enter num from 1-20
if palyer and guessing num....win the game otherwise write loose the game
'''

m=random.randint(1,20)
n=int(input("Enter number to be guessed "))
if n == m:
    print("You won!!")

else:
    print("You lost and correct number is ",m)

'''
'welcome scientific calculator'
1.percentage....ask number..5% of 100
2.sqrt...ask number 16
3.lcm....ask number...
4.exit...stop working

if selected 5....invalid option and repeate loop
if instead of number enter string...invalid value...all to enter again the number
'''
import math
print('Welcome Scientific Calculator')
print("1.Percentage")
print("2.Square Root")
print("3.LCM")
print("4.Exit")
n = int(input("Press the key: "))
while n != 4 :
   
    if n == 1:
        a = int(input("Enter the share: "))
        b = int(input("Enter the amount: "))
        print("Percentage amount: ",(a / 100) * b)
   
    elif n == 2:
        a = int(input("Enter the number: "))
        print("Square root: ",math.sqrt(a))
   
    elif n == 3:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        i = max(a,b)
        j = min(a,b)
        for k in range(1,j+1):
            if (i*k) % j == 0 :
                lcm = i*k
                break
        print("LCM: ",lcm)
               
    elif n == 4 :
        break
   
    else :
        print("Invalid Choice")
   
    print('Welcome Scientific Calculator')
    print("1.Percentage")
    print("2.Square Root")
    print("3.LCM")
    print("4.Exit")
    n = int(input("Press the key"))
print("Exit")




################################

    

print('WELCOME TO SCIENTIFIC CALCULATOR')
print('1.Percentage')
print('2.Square root')
print('3.LCM')
print('4.Exit')

while True:
    choice = int(input('Enter number between 1-4: '))
    if choice == 1:
        num = int(input('Enter the number whose percentage is to be find: '))
        num1 = int(input('Enter the percentage value: '))
        ans = num * (num1/100)
        print(ans)
    elif choice == 2:
        num2 = int(input('Enter the number: '))
        numSqrt = num2 ** 0.5
        print(numSqrt)
    elif choice == 3:
        x = int(input('Enter first number: '))
        y = int(input('Enter second number: '))
        if x > y:
            lcm = x
        else:
            lcm = y
        while (True):
            if ((lcm % x == 0) and (lcm % y == 0)):
                d = lcm
                break
            lcm += 1
        print('LCM is', d)
    elif choice == 4:
        print('EXIT')
    else:
        print('You entered wrong choice!!!')
        print('Enter the value again: ')

