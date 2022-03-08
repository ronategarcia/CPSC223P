# Name: Rodrigo Onate
# Date: 02/03/2022
# File Purpose: Lab02 main program for contacts list.
from contacts import *
contacts = []
while True:
    print("\n\t*** TUFFY TITAN CONTACT MAIN MENU\n")
    print("1. Print list")
    print("2. Add contact")
    print("3. Modify contact")
    print("4. Delete contact")
    print("5. Exit the program\n")
    x = input("Enter menu choice: ")
    print("\n")
    if x == "1":
        print_list(contacts)
    elif x == "2":
        add_contact(contacts)
    elif x == "3":
        modify_contact(contacts)
    elif x == "4":
        delete_contact(contacts)
    elif x == "5":
        break
    else:
        print("Input a number between 1 and 5.")