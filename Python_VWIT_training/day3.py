############ write ###########
f1=open('test.txt','w')
f1.write("this is python file")
f1.write('\n The result of 25+26 is %s'%str(25+26))
print('successfully created')
f1.close()

#### read characters ##########
file2=open('test.txt','r')
print('\n')
print(file2.read(10))
print('\nsuccessfully read')
file2.close()


########## read ###########
file2=open('test.txt','r')
print('\n')
for i in range(2):
  print(file2.readline())
print('\nsuccessfully read')
file2.close()

######### append #############
f3=open('test.txt','a')

f3.write("this is appended line")
msg = ['\ngood morning','\nGood Morning today','Wonderful Day']
f3.writelines(msg)
print('successfully appended')
f3.seek(2,0)
print(f3.tell())
f1.close()


### to find cursor position ##
print(f3.tell())

##### seek() #######
'''
to change the curcor position.
seek(offset,position)
offset end position
position -> 0 -> beginning of file
1-> current postion
2-> end position of last line 
'''
'''
seek(10,0)  #--> 0+10 --> 10  --> first comma at position 10..we are starting at the 0 position
seek(5,1)  #5+10 = 15  --> current posotion is 10 after this it is 10+5
seek(-5,2)  #50-5 = 45
seek(5,2) #50+5 = 55 (this is blank)
'''
'''
0 1 2 is fixed
offset is the 

this is a ,python file and, knowledge of the langu,age.
'''








