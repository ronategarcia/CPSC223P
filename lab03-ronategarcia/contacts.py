# Name: Rodrigo Onate
# Date: 02/14/2022
# File Purpose: Lab03 - functions that manipulate contact list
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
def add_contact(contacts,first_name,last_name):
    """Adding a contact to the list."""
    fullName = [first_name,last_name]
    contacts.append(fullName)
    return contacts
def modify_contact(contacts, first_name, last_name, index):
    """This function modifies the contact list."""
    if index > len(contacts)-1 or index < 0:
            print("Invalid index number.\n")
            return False
    else:
        fullName = [first_name, last_name]
        contacts[index] = fullName
        return contacts
def delete_contact(contacts, index):
    """This function deletes a contact from the list."""
    if index > len(contacts)-1 or index < 0:
        print("Invalid index number.")
        return False
    else:
        contacts.pop(index)
        return True
def sort_contacts(contacts, column):
    """This function sort contacts by first_name or last_name"""
    if column == 0:
        contacts.sort(key=lambda x: x[0].lower())
        return contacts
    elif column == 1:
        contacts.sort(key=lambda x: x[1].lower())
        return contacts