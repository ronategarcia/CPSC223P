# Name: Rodrigo Onate
# Date: 02/03/2022
# File Purpose: Lab02 - functions that manipulate contact list
# in main.py
def print_list(contacts):
    """Prints the contact list."""
    print("================== CONTACT LIST ==================")
    print("Index   First Name            Last Name")
    print("======  ====================  ====================")
    if len(contacts) == 0:
        print("No contacts in the list")
    else:
        for i in range(len(contacts)):
            print(f'{str(i):8}{contacts[i][0]:22}{contacts[i][1]:22}')
def add_contact(contacts):
    """Adding a contact to the list."""
    fname = input("Enter first name: ")
    lname = input("Enter last name: ")
    print("\n")
    fullName = [fname, lname]
    contacts.append(fullName)
    return contacts
def modify_contact(contacts):
    """This function modifies the contact list."""
    index = int(input("Enter the index number: "))
    print("\n")
    if index > len(contacts)-1:
        print("Invalid index number.\n")
        return contacts
    else:
        fname = input("Enter first name: ")
        lname = input("Enter last name: ")
        fullName = [fname, lname]
        contacts[index] = fullName
        return contacts
def delete_contact(contacts):
    """This function deletes a contact from the list."""
    index = int(input("Enter the index number: "))
    if index > len(contacts)-1:
        print("Invalid index number.")
        return contacts
    else:
        contacts.pop(index)
    return contacts