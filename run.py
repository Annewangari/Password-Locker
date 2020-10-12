#!/usr/bin/env python3.6
from user import User
from  credentials import Credential
import getpass
import random

def create_account(login_account,login_username,credential_detail):
def create_account(fname,lname,username,password,confirm_password):

    """
    function to create a new account
    """

    new_user = User(login_account,login_username,)
    new_password = Credential(credential_detail)
    new_user = User(fname,lname,username,password,confirm_password)

    return new_user
    return new_password

def save_details(detail):
def save_details(user):

    """
    function to save save_details
    """
    detail.save_detail()
    user.save_detail()

def save_creadential(credential_detail):
def display_all_details():

    """
    function to save passwords
    function used to return all saved save_details
    """
    credential_detail.save_creadential()
    return User.display_all_details

def main():

def display_all_details():
    print("RE-INVENT THE WAY YOU SAVE YOUR PASSWORDS WITH OUR PASSWORD LOCKER APP")

    """
    function used toreturn all saved save_details
    """
    return User.display_all_details
    print('\n')

    print("Please enter a nickname")

    user_name = input()

    print(f"hey {user_name}, welcome to your password manager. what would you like to do")

    print('\n')

    while True:

        print("Use these short codes : 1 - register a new account, 2 - display accounts, 3 -find accounts, 4 -exit the locker ")

        short_code = input().lower()

        if short_code == '1':

            print("Hey New User")
            print("-"*10)

            print ("First name")
            f_name = input()

            print("Last name")
            l_name = input()

            print("username")
            username = input()

            print('\n')

            print("Do you want a randomly generated password?")
            ans = input()

            ans = input()
            if ans:
                WORDS = ("{user_name}", "{user_name}123", "{user_name}zyx", "{user_name}098", "{user_name}567",  "{user_name}hfg")
                word = random.choice(WORDS)
                correct = word
                jumble = ""
                while word:
                    position = random.randrange(len(word))
                    word = word[:position] + word[(position + 1):]
                print(word[position])

            else:
                password = getpass.getpass('password:')
                print("*****")

                confirm_password = getpass.getpass('confirm password:')
                print("*****")

            save_details(create_account(f_name,l_name,username,password,confirm_password))

            print ('\n')

            print(f"New User {f_name} {password} account created and password saved")

            print ('\n')




if __name__ == '__main__':

    main()