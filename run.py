#!/usr/bin/env python3.6
from user import User
import getpass
import random
import string

def create_account(fname,lname,username,password,confirm_password):
def create_account(account_name,username,password,confirm_password):

    """
    function to create a new account
    """

    new_user = User(fname,lname,username,password,confirm_password)
    new_user = User(account_name,username,password,confirm_password)

    return new_user

@@ -27,36 +28,52 @@ def display_all_details():
    """
    return User.display_all_details

# def gen_word(min, max):
#     vowels = list('aeiou')
# 	word = ''
# 	syllables = min + int(random.random() * (max - min))
# 	for i in range(0, syllables):
# 		word += gen_syllable()
#
# 	return word.capitalize()
def main():

    print("RE-INVENT THE WAY YOU SAVE YOUR PASSWORDS WITH OUR PASSWORD LOCKER APP")

    print('\n')

    print("Please enter a nickname")
    print("login")

    print('\n')

    print("please idetify yourself using your locker username")

    user_name = input()

    print(f"hey {user_name}, welcome to your password manager. what would you like to do")
    print(f"Hello {user_name}, welcome to your password manager, how can we help you today")

    print('\n')

    while True:

        print("Use these short codes : 1 - register a new account, 2 - display accounts, 3 -find accounts, 4 -exit the locker ")
        list =('''
        1-register a new account
        2-display accounts
        3-find accounts
        4-exit the locker\n''')
        print(list)


        short_code = input().lower()

        if short_code == '1':

            print("Hey New User")
            print("-"*10)
            print(f"{user_name} please fill in the following")

            print ("First name")
            f_name = input()
            print("-"*10)

            print("Last name")
            l_name = input()
            print ("account name")
            account_name = input()

            print("username")
            username = input()
@@ -66,32 +83,25 @@ def main():
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
            password = getpass.getpass('password:')
            print("*****")

                confirm_password = getpass.getpass('confirm password:')
                print("*****")
            confirm_password = getpass.getpass('confirm password:')
            print("*****")

            save_details(create_account(f_name,l_name,username,password,confirm_password))
            save_details(create_account(account_name,username,password,confirm_password))

            print ('\n')

            print(f"New User {f_name} {password} account created and password saved")
            print(f"{user_name} {account_name} account of {username} created and password saved")

            print ('\n')

            print(f"{user_name} what else do you want to do?")







if __name__ == '__main__':
    main()