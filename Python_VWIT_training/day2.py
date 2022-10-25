name = input("Enter your name: ")
fname,lname = name.split()
acc = input("Enter your account: ")
add= input("Enter your address: ")

firstname = name.split(" ")
pswd = fname[::-1]
psw = fname[0][::-1]

t1=(name,acc,add,psw)

print(t1)
t2 = list(t1)
t2[3]=input("New address: ")
t1 = tuple(t2)
print(t1)

'''
Enter your name: John Newman
Enter your account: 12345
Enter your address: A-64 Street,LA
('John Newman', '12345', 'A-64 Street,LA', 'namweN nhoJ')
'''


##########################################################################



