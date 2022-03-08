# Name: Rodrigo Onate
# Date: 02/14/2022
# File Purpose: Lab03 main program for contacts list.
from contacts import *
contacts = []
while True:
    print("\n\t*** TUFFY TITAN CONTACT MAIN MENU\n")
    print("1. Print list")
    print("2. Add contact")
    print("3. Modify contact")
    print("4. Delete contact")
    print("5. Sort list by first name")
    print("6. Sort list by last name")
    print("7. Exit the program")
    print("\n")
    x = input("Enter menu choice: ")
    print("\n")
    if x == "1":
        print_list(contacts)
    elif x == "2":
        first_name = input("Input first name: ")
        last_name = input("Input last name: ")
        add_contact(contacts, first_name, last_name)
    elif x == "3":
        index = int(input("Enter the index number: "))
        first_name = input("Input first name: ")
        last_name = input("Input last name: ")
        modify_contact(contacts, first_name, last_name, index)
    elif x == "4":
        index = int(input("Enter the index number: "))
        delete_contact(contacts, index)
    elif x == "5":
        column = 0
        sort_contacts(contacts, column)
    elif x == "6":
        column = 1
        sort_contacts(contacts, column)
    elif x == "7":
        break
    else:
        print("Invalid Command. Input a number between 1 and 7.")