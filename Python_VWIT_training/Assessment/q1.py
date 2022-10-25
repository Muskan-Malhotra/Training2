'''
Write a function in python which find the even length of words in a given user string and return a list of less length word of even words.
Output:
Enter your string: I am Python Developer
Minimum length even word:  ['am']
'''

str = input("Enter the String: ").split(" ")

evenLen = filter(lambda x:x if len(x)%2==0 else "",str)
sortedList = sorted(list(evenLen), key=len)
ans = filter(lambda x:x if len(x)<=len(sortedList[0]) else "",sortedList)

print(list(ans))


'''
Write a program to find the sequence of negative numbers from the range as (n1 , n2) = (-10,5)  and display only that numbers, which divisible by 2 only.
Output:
-10 -8 -6 -4 -2
'''

n1 = int(input("Enter num1: "))
n2 = int(input("Enter num2: "))

lst = [i for i in range(n1,n2+1) if i<0 and i%2==0]
print(lst)


'''
Write a program to display the chain of numbers from 1 to N (where N=user input) as per following rules.
Display word as Magic instead of number, if number is divisible by 2
Display word as Buzzer instead of number, if number is divisible by 3
Display word as Win instead of number, if number is divisible by 3 and 5
Display word as …MagicBuzzer… instead of number, if number by 2 and 3
Display number, if it is not according to a), b), c) and d) rules
Next line will come at rule d)

Output:
Enter N value: 20
1MagicBuzzerMagic5
...MagicBuzzer...7MagicBuzzerMagic11
...MagicBuzzer...13MagicWinMagic17
...MagicBuzzer...19Magic

'''

n1 = int(input("Enter the number"))
for i in range(1,n1+1):
  if i%3==0 and i%5==0:
    print("Win",end="")
  elif i%2==0 and i%3==0:
    print("…MagicBuzzer…",end="")
  elif i%3 == 0:
    print("Buzzer",end="")
  elif i%2==0 and i%3==0 and i%5==0:
    print("Win"+"…MagicBuzzer…",end="")
  elif i%2 == 0: 
    print("Magic",end="")
  else:
    print(i,end="")


