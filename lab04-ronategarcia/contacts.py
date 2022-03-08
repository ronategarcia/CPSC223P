# Name: Rodrigo Onate
# Date: 02/17/2022
# File Purpose: Lab04 contact functions program for main.py
#
"""Contacts module for main.py - Lab04"""


def print_contact(contacts):
    """Prints the contact list."""
    print("==================== CONTACT LIST ====================")
    print("Last Name             First Name            Phone")
    print("====================  ====================  ==========")
    if len(contacts) == 0:
        print("No contacts in the list")
    else:
        for k, var in contacts.items():
            print(f"{var[1]:22}{var[0]:22}{k:8}")


def add_contact(contacts, id, first_name, last_name):
    """Adds a contact to the dictionary."""
    if int(id) in contacts:
        return "error"
    if not first_name.isupper() and not last_name.isupper():
        first_name = first_name.capitalize()
        last_name = last_name.capitalize()
    contacts[int(id)] = [first_name, last_name]
    return contacts


def modify_contact(contacts, first_name, last_name, id):
    """Modify a contact in the dictionary."""
    if int(id) not in contacts:
        return "error"
    if not first_name.isupper() and not last_name.isupper():
        first_name = first_name.capitalize()
        last_name = last_name.capitalize()
    contacts[int(id)] = [first_name, last_name]
    return contacts


def delete_contact(contacts, id):
    """Delete a contact from the directory."""
    if int(id) not in contacts:
        return "error"
    v_removed = contacts.pop(int(id))
    return v_removed


def sort_contacts(un_sorted):
    """Sort all contacts by last name and then first name"""
    sorted_first = dict(sorted(un_sorted.items(), key=lambda x: x[1]))
    sorted_last = dict(sorted(sorted_first.items(), key=lambda x: x[1][1]))
    return sorted_last


def find_contact(contacts, find):
    """Find a contact in the directory."""
    a_dict = {}
    if find.isdigit() and int(find) in list(contacts):
        a_dict[int(find)] = contacts[int(find)]
    else:
        if not find.isupper():
            find = find.capitalize()
        for k, var in contacts.items():
            if find in var[0] or find in var[1]:
                a_dict[k] = var
        if len(a_dict) == 0:
            return "error"
        a_dict = sort_contacts(a_dict)
    return a_dict
