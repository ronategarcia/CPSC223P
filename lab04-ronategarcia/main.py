# Name: Rodrigo Onate
# Date: 02/17/2022
# File Purpose: Lab04 main program for contacts list.
#
"""Main module - Lab04."""
from contacts import print_contact, add_contact, modify_contact
from contacts import delete_contact, find_contact

CONTACTS = {}
while True:
    print("\n\t*** TUFFY TITAN CONTACT MAIN MENU\n")
    print("1. Add contact")
    print("2. Modify contact")
    print("3. Delete contact")
    print("4. Print contact list")
    print("5. Find contact")
    print("6. Exit the program")
    print("\n")
    X = input("Enter menu choice: ")
    print("\n")
    if X == "1":
        ID = input("Enter phone number: ")
        FIRST_NAME = input("Enter first name: ")
        LAST_NAME = input("Enter last name: ")
        if ID.isdigit() and len(ID) == 10:
            R = add_contact(CONTACTS, ID, FIRST_NAME, LAST_NAME)
            if R == "error":
                print("Phone number already exists.")
            else:
                print("Added:", end=" ")
                print(CONTACTS[int(ID)][0], end=" ")
                print(CONTACTS[int(ID)][1], end=".")
        else:
            print("Incorrect phone number.")
            print("Input only 10 integers.")
    elif X == "2":
        ID = input("Enter phone number: ")
        FIRST_NAME = input("Input first name: ")
        LAST_NAME = input("Input last name: ")
        R = modify_contact(CONTACTS, FIRST_NAME, LAST_NAME, ID)
        if R == "error":
            print("Phone number does not exists.")
        else:
            print("Modified:", end=" ")
            print(CONTACTS[int(ID)][0], end=" ")
            print(CONTACTS[int(ID)][1], end=".")
    elif X == "3":
        ID = input("Enter phone number: ")
        R = delete_contact(CONTACTS, ID)
        if R == "error":
            print("Invalid phone number.")
        else:
            print("Deleted:", end=" ")
            print(R[0], end=" ")
            print(R[1], end=".")
    elif X == "4":
        print_contact(CONTACTS)
    elif X == "5":
        FIND = input("Enter search string: ")
        R = find_contact(CONTACTS, FIND)
        if R == "error":
            print("Invalid search string.")
        else:
            print("================== FOUND CONTACT(S) ==================")
            print("Last Name             First Name            Phone")
            print("====================  ====================  ==========")
            for k, var in R.items():
                print(f"{var[1]:22}{var[0]:22}{k:8}")
    elif X == "6":
        break
    else:
        print("Invalid Command. Input a number between 1 and 6.")
