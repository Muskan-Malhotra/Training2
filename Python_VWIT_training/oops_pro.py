'''
Menu Options:

1.Add Teacher Data
2.Display All Teachers Data
3.Update Teacher Data By ID
4.Delete Teacher Data By ID
5.Search Teacher Data By ID
6.Exit
'''
# Create a class
class Teacher:
    # Constructor
    def __init__(self,ID,Name,Date_of_Join,Salary,Assigned_class):
        self.ID = ID
        self.Name = Name
        self.Date_of_Join = Date_of_Join
        self.Salary = Salary
        self.Assigned_class = Assigned_class
         
    # Function to add a new teacher   
    def add(self,ID,Name,Date_of_Join,Salary,Assigned_class):
        T1 = Teacher(ID,Name,Date_of_Join,Salary,Assigned_class)
        data.append(T1)
    
      # Function to display teachers details     
    def display(self, T1):
            print('-'*20)
            print("ID   : ", T1.ID)
            print("Name : ", T1.Name)
            print("Joining Date : ", T1.Date_of_Join)
            print("Salary : ", T1.Salary)
            print("Assigned Class : ", T1.Assigned_class)
            print('-'*20)

    # Update Function   
    def update(self, ID, No,update_data):
        i = T1.search(ID)
        if No=='1':
                data[i].Name = update_data
        elif No=='2':
                data[i].Date_of_Join = update_data
        elif No=='3':
                data[i].Salary = update_data
        elif No=='4':
                data[i].Assigned_class = update_data
    # Delete Function
    def delete(self, ID):
        i = T1.search(ID)
        del data[i]

    # Search Function
    def search(self, ID):
        for i in range(len(data)):
            if(data[i].ID == ID):
                return i
    data =[]#list to add teachers
    T1 = Teacher(0,'','',0,'')#Teacher object
    print('Welcome To Teacher Management System')


while True:
    print("\nMenu Options:")
    print('\n1.Add Teacher Data\n2.Display All Teachers Data\n3.Update Teacher Data By ID\n4.Delete Teacher Data By ID\n5.Search Teacher Data By ID\n6.Exit')
    option = input("\nEnter Your Option:")
    #add option
    if(option == '1'):
        ask=int(input('\nHow many techers do you want to add? '))
        for i in range(ask):
            ID=int(input('\nEnter New ID: '))
            Name=input('Enter Teacher Name: ')
            Date_of_Join=input('Enter Date of Joining: ')
            Salary= int(input("Enter Teacher's Salary: "))
            Assigned_class=input('Enter Assigned Class Detail: ')
        T1.add(ID,Name,Date_of_Join,Salary,Assigned_class)
    #display option
    elif(option == '2'):
        print("\nList of Teachers")
        for i in range(len(data)):
            T1.display(data[i])
    
    #update option
    elif(option == '3'):
        update_ID=int(input('Enter ID which do you want to update: '))
        display_ID = T1.search(update_ID)
        if display_ID != None:
            print('What do you want to update?')
            while True:
                print('\n1.Name\n2.Date_of_Join\n3.Salary\n4.Assigned_class')
            
            option=input('\nEnter your option: ')
            if option=='1':
                Name=input('Enter Modified Teacher Name: ')
                T1.update(update_ID, '1',Name)
                break
            elif option=='2':
                Date_of_Join=input('Enter Modified Date of Joining: ')
                T1.update(update_ID,'2',Date_of_Join)
                break
            elif option=='3':
                Salary= int(input("Enter Modified Teacher's Salary: "))
                T1.update(update_ID,'3',Salary)
                break
            elif option=='4':
                Assigned_class=input('Enter Modified Assigned Class Detail: ')
                T1.update(update_ID,'4',Assigned_class)
                break
            else:
                print('Invalid option selection')
        else:
            print("ID doesn't exist") 

    
        print("\nList of Teachers after updation:")
        for i in range(len(data)):
            T1.display(data[i])

        #delete option
    elif(option == '4'):
        del_ID=int(input('\nWhich ID do you want to delete? '))
        display_ID = T1.search(del_ID)
        if display_ID != None:
            T1.delete(del_ID)
        else:
            print("ID doesn't exist")
            print("\nList of Teacher Data after deletion:")
        if len(data)>=1:
            for i in range(len(data)):
                print('-'*30)
                T1.display(data[i])
                print('-'*30)
        else:
            print('-'*30)
            print('There is no data in table')
            print('-'*30)
    
    #search option
    elif(option == '5'):
        search_ID=int(input('\nWhich ID do you want to search? '))
        display_ID = T1.search(search_ID)
        if display_ID != None:
            T1.display(data[display_ID])
        else:
            print("ID doesn't exist")

        #exit option
    elif(option == '6'):
        print("\nThanks For Using ME!!!")
        break
    
    #invalid option
    else:
        print('\nInvalid option')







