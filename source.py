#importing libraries
import pickle  
import os
import sys
from prettytable import PrettyTable

#function to check if the logged in user is admin or not.
def isUserAdmin(usertype):
  if(usertype == 'admin'):
    return True
  return False  

#function to authenticate the user and return his/her login status.
def login():
  username = input('Input Username: ') #input the username
  password = input('password: ')#input the password
  print('--------------------------------------------------------------------')
  file = open('users.dat','rb') #open the file in read mode
  admincheck = False
  while True:
    record = pickle.load(file) #load the data from the file.
    #checking if the data entered (username and password) matches with record in the file.
    if (record['username']==username and record['password'] == password): 
      usertype = record['usertype']
      
      #function to check logged in user is admin or not.
      adminCheck = isUserAdmin(usertype)
      print('Welcome ', username,'!!!') 
      file.close
      return True, adminCheck
     
  file.close #closing the file.
  return False, adminCheck

#function to add new user to the users.dat file
def registerNewUser():
  print('--------------------------------------------------------------------')
  while True: 
    username = input('Input the username(should be of atleast length 3): ')
    password = input('Input the password(should be of atleast length 3): ')
    if len(username) >=3 and len(password)>=3:
      usertype = input('The user should be admin? (yes/no): ')
      userDict= {}
      userDict['username'] = username
      userDict['password'] = password
      if usertype == 'yes':
        userDict['usertype'] = 'admin'
      else:
        userDict['usertype'] = 'non-admin'
      file=open('users.dat','ab')
      pickle.dump(userDict,file)
      file.close()
      print('New0 User Registered Successfully !!!!')
      break
  print('--------------------------------------------------------------------')
    

def write_data():
  print('--------------------------------------------------------------------')
  file=open('vaccine.dat','ab') #a-append b-binary
  n=int(input('ENTER THE NO. OF PERSON TO BE VACCINATED: '))
  for i in range(n):
    print('ENTER THE DETAILS OF PERSON: ',i+1)
    dict['AADHAR NUMBER']=int(input('Enter Aadhar number: '))
    dict['NAME']=(input('Enter Name: '))
    dict['AGE']=int(input('Enter Age: '))
    dict['VACCINE TYPE']=(input('Enter Vaccine: '))
    dict['DOSE'] = int(input('Dose (1/2): '))
    pickle.dump(dict,file) #dump is used to write in a file
    print('RECORD ADDED SUCCESSFULLY!!!')
  file.close()
  print('--------------------------------------------------------------------')


def display():
    print('--------------------------------------------------------------------')
    file=open('vaccine.dat','rb') #r-read b-binary
    
    records = PrettyTable(['Aadhar', 'Name', 'Age', 'Vaccine','Dose'])
    try:
      while True:
        var=pickle.load(file) #load is used to read
        records.add_row([var['AADHAR NUMBER'], var['NAME'],var['AGE'],var['VACCINE TYPE'], var['DOSE']])
    except EOFError:
           pass
    file.close
    print(records)
    print('--------------------------------------------------------------------')

def search():
    print('--------------------------------------------------------------------')
    file=open('vaccine.dat','rb') #r-read b-binary
    a=int(input('Enter Aadhar number to be searched: '))
    found=0
    try:
      while True:
        vac=pickle.load(file) #load is used to read
        if vac["AADHAR NUMBER"]==a:
            found=1
            print('RECORD FOUND!!!')
            #print(vac)
            records = PrettyTable(['Aadhar', 'Name', 'Age', 'Vaccine','Dose'])
            records.add_row([vac['AADHAR NUMBER'], vac['NAME'],vac['AGE'],vac['VACCINE TYPE'], vac['DOSE']])
            print(records)
            break
    except EOFError:
      pass
    if found==0:
      print("RECORD NOT FOUND!!!")
    file.close 
    print('--------------------------------------------------------------------')

def update():
    print('--------------------------------------------------------------------')
    file=open('vaccine.dat','rb') #r-read b-binary
    f=open('temp.dat','ab')
    a=int(input('Enter Aadhar number to be updated: '))
    found=0
    try: 
      while True:
        vac=pickle.load(file) #load is used to read
        if vac['AADHAR NUMBER']==a:
          found=1
          print('ENTER NEW DETAILS')
          dict['AADHAR NUMBER']=int(input('Enter Aadhar Number: '))
          dict['NAME']=(input('Enter Name: '))
          dict['AGE']=int(input('Enter Age'))
          dict['VACCINE TYPE']=(input('Enter Vaccine: '))
          dict['DOSE'] = int(input('Dose(1/2): '))
          pickle.dump(dict,f) #dump is udes to write in a file
          print('RECORD UPDATED!!!')
        else:
          pickle.dump(vac,f)
    except EOFError:
      pass
    file.close()
    f.close()
    if found==0:
      print("RECORD NOT FOUND!!!")
    os.remove('vaccine.dat')
    os.rename('temp.dat','vaccine.dat')
    
    print('--------------------------------------------------------------------')

def delete():
    print('--------------------------------------------------------------------')
    file=open('vaccine.dat','rb') #r-read b-binary
    f=open('temp.dat','ab')
    a=int(input('Enter aadhar number to be deleted: '))
    found=0
    try:
      while True:
        vac=pickle.load(file) #load is used to read
        if vac['AADHAR NUMBER']==a:
          found=1
        else:
          pickle.dump(vac,f)
    except EOFError:
      pass
    file.close()
    f.close()
    if found==0:
      print('RECORD NOT FOUND!!!!')
    os.remove('vaccine.dat')
    os.rename('temp.dat','vaccine.dat')
    
    if found==0:
      print('NO RECORDS HAS BEEN DELETED!!!') 
    else:
      print('RECORD DELETED SUCCESSFULLY!!!') 
    print('--------------------------------------------------------------------')

#main program
print('-------------------- Vaccine Management System----------------------')
print('-----------------------------Login----------------------------------')
loginStatus, adminCheck = login() #calling login function.
if loginStatus == True:
  if adminCheck == True:
    registerOption = input('Do You want to Register any new user ?(yes/no)')
    if registerOption =='yes':
      while True:
        registerNewUser() #function to register new user.
        registerMore = input('Want to register more user?(yes/no)')
        if registerMore == 'no':
          break
  while True:
    print('-------------------------Services----------------------------------')
    print('1. Insert Records')
    print('2. Display Records')
    print('3. Search Record')
    print('4. Update Record')
    print('5. Delete Record')
    ch=int(input('Select the Service: '))
    while True:
      if ch==1:
        write_data()
        break
      if ch==2:
        display()
        break
      if ch==3:
        search()
        break
      if ch==4:
        update()
        break
      if ch==5:
        delete()
      
      else:
        print('You have entered wrong choice !!! Please correct choice.')
        ch = int(input('Select the correct Service: '))
    
  else:
    print('Sorry !!! Unable to login...')


