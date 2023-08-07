import os
import time


count = 1
customers_data = {}
def sign_up():
    global count, customers_data
    name = input('enter your full name:  ')
    email = input('enter your email address:  ')
    password = input('enter your password:  ')
    confirm_password = input('enter your password ')
    if password == confirm:
         customers_data = ({count: (name, email, password)})
         count +=1
         print(customers_data)
    else:
         print('you entered wrong password\ncomfirm your password again?')
         clearing()
         sign_up()

def database(id,lis):
    customers_data[id] = lis



def login():
         email = input('enter your email address:  ')
         password = input('enter your password:  ')

def menu():
    while True:
     option = input('enter 1 or 2:')
     if option == '1':
         sign_up()
     elif option == '1':
         sign_up()
     elif option == '2':
         sign_up()
     else:
         print('read the instruction again and be clear on what to do.')
         menu()

def clearing():
        time.sleep(4)
        os.system('cls')
        

        if __name__ == '__main__':
         print('''
              Hello, welcome to our bag store.
              read the insruction carefully!
              enter 1 to signup and
              enter 2 to login
              ''')
         clearing()
         menu()


      