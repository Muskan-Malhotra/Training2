'''
ask the user their name 5 times
input file and add all the user's name
open input file--> read the file --> create a password for all users.

create a output file 
show like this 
UN: john thomas
Password: JOTHas123
'''
################### My code ############
'''
n1 = input("Enter your name: ")
n2 = input("Enter your name: ")
n3 = input("Enter your name: ")
n4 = input("Enter your name: ")
n5 = input("Enter your name: ")

f1 = open('user.txt','w')
f1.write('%s \n%s \n%s \n%s \n%s \n' %(n1,n2,n3,n4,n5))
print("Written in f1")
f1.close()

## use for loop

f2=open('user.txt','r')
f3 = open('user.txt','a')

for i in range(5):
  str = f2.readline()
  str2 = str.split()
  st = str2[0][0:2].upper(); st2=str2[0][2:]
  psw = st+st2+"1234"
  #random number() last two small
  f3.write("\n")
  f3.write("UN:{}Password: {}\n".format(str,psw))
  

f2.close()
f3.close()
'''
'''
Johan Smith
Enter your name: Smitten Tag
Enter your name: Catie Longform
Enter your name: John Stead
Enter your name: Peter Duplin
'''


#######trainer ##########
# import random

# i_file=open('names.txt','a')
# for i in range(5):
#   nm=input('enter your name:')
#   i_file.write(nm+'\n')
# i_file.close()

# r_file=open('names.txt','r')
# o_file=open('user.txt','a')
# records=r_file.readlines()
# for name in records:
#   f_name,l_name=name.split()
#   pw=f_name[:2].upper()+l_name[:2].upper()+\
#   l_name[(len(l_name)-2):].lower()+str(random.randint(100,125))
#   o_file.write('\nUN: %s'%name)
#   o_file.write('PW: %s'%pw+'\n')

# o_file.close()
# r_file.close()


''' 
Next Task !!!
[11:37] Saurika  Tiwary(Vatika82-N) (Guest)
    
Unix(/ˈjuːnɪks/; trademarked asUNIX) is a family ofmultitasking,multiusercomputeroperating systemsthat derive from the originalAT&TUnix, whose development started in 1969[1]at theBell Labsresearch center byKen Thompson,Dennis Ritchie, and others.
Initially intended for use inside theBell System, AT&TlicensedUnix to outside parties in the late 1970s, leading to a variety of both academic and commercial Unix variants from vendors includingUniversity of California, Berkeley(BSD),Microsoft(Xenix),Sun Microsystems(SunOS/Solaris),HP/HPE(HP-UX), andIBM(AIX). In the early 1990s, AT&T sold its rights in Unix toNovell, which then sold the UNIX trademark toThe Open Group, an industry consortium founded in 1996. The Open Group allows the use of the mark for certified operating systems that comply with theSingle UNIX Specification(SUS).
Help:IPA/EnglishThroughout Wikipedia, the pronunciation of words is indicated by means of the International Phonetic Alphabet (IPA). The following tables list the IPA symbols used for English words and pronunciations...en.wikipedia.org​[11:39] Saurika  Tiwary(Vatika82-N) (Guest)
    use this sentance....write into the file
then read the same file....uppercase words.

UNIX is the command Line world Syntax or operating SYSTEM
'''

# file3=open('test3.txt','w')
# file3.write("a family of multitasking, multiuser computer operating systems that derive from the original AT&T Unix, whose development started in 1969[1] at the Bell Labs research center by Ken Thompson, Dennis Ritchie, and others.Initially intended for use inside the Bell System, AT&T licensed Unix to")
# print("successfully created")
# file3.close()

# file1=open('test3.txt','r')
# l=file1.readline()
# file1=open('test3.txt','a')
# file1.write("\nUpper words are:\n")
# for word in l:
#   if word.isupper():
#     file1.write(word)
# file1.close()


file1=open('test3.txt','w')
file1.write('UNIX is the command Line world Syntax or operating SYSTEM')

file1.close()
file2=open('test3.txt','r')
a=file2.readline()
b=a.split()

for i in b:
    if i.isupper():
        print(i)

file2.close()
 
