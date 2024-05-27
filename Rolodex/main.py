"""
Names: Tina Toma, Hill Niteshbhai Vaghasiya

Date: 2/20/2024

This program simulates a Rolodex which can be searched and updated.

The user is prompted to make a choice to: display contacts, add contact, search contacts,
modify contact, and save and quit. The program updates the list accordingly. 
"""

from contact import Contact
import check_input


def read_file(filename):
    """Reads the file and returns a list of contacts."""
    contacts = []
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            contact = Contact(*data)
            contacts.append(contact)
    contacts.sort()
    return contacts

def write_file(filename, contacts):
    """Writes the list of contacts to the file."""
    with open(filename, 'w') as file:
        for contact in contacts:
            file.write(repr(contact) + '\n')

def get_menu_choice():
    """Displays the menu and gets the user's choice."""
    print("\nMain Menu:")
    print("1. View Contacts")
    print("2. Search Contacts")
    print("3. Add Contact")
    print("4. Modify Contact")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice

def modify_contact(contact):
    """Modifies the given contact."""
    while True:
        print("\nModify Menu:")
        print("1. First Name")
        print("2. Last Name")
        print("3. Phone")
        print("4. Address")
        print("5. City")
        print("6. Zip Code")
        print("7. Save")
        choice = check_input.get_int_range("Enter your choice: ", 1, 7)

        if choice == 1:
            contact.first_name = input("Enter new first name: ")
        elif choice == 2:
            contact.last_name = input("Enter new last name: ")
        elif choice == 3:
            contact.phone = input("Enter new phone number: ")
        elif choice == 4:
            contact.address = input("Enter new address: ")
        elif choice == 5:
            contact.city = input("Enter new city: ")
        elif choice == 6:
            contact.zip_code = input("Enter new zip code: ")
        elif choice == 7:
            break


def main():
  filename = 'addresses.txt'
  contacts = read_file(filename)

  # Enters the main loop
  while True:
      print("\nRolodex Menu:")
      print("1. Display Contacts")
      print("2. Add Contact")
      print("3. Search Contacts")
      print("4. Modify Contact")
      print("5. Save and Quit")

      # Gets the user's choice
      choice = check_input.get_int_range("> ", 1, 5)

      # Displays the contacts
      if choice == 1:
          print(f"Number of contacts: {len(contacts)}")
          for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. First Name: {contact.first_name}\n   Last Name: {contact.last_name}\n   Phone: {contact.phone}\n   Address: {contact.address}\n   City: {contact.city}\n   Zip: {contact.zip_code}")

      # Adds a contact
      elif choice == 2:
          print("Enter new contact:")
          first_name = input("First name: ")
          last_name = input("Last name: ")
          phone = input("Phone #: ")
          address = input("Address: ")
          city = input("City: ")
          zip_code = input("Zip: ")
          new_contact = Contact(first_name, last_name, phone, address, city, zip_code)
          contacts.append(new_contact)
          contacts.sort()

      # Searches for a contact
      elif choice == 3:
          print("Search:")
          print("1. Search by last name")
          print("2. Search by zip")
          search_option = check_input.get_int_range("> ", 1, 2)
          if search_option == 1:
              last_name = input("Enter last name: ")
              search_results = [contact for contact in contacts if contact.last_name.lower() == last_name.lower()]
          elif search_option == 2:
              zip_code = input("Enter zip code: ")
              search_results = [contact for contact in contacts if contact.zip_code == zip_code]

          print("Search Results:")
          for idx, contact in enumerate(search_results, start=1):
              print(f"{idx}. First Name: {contact.first_name}\n   Last Name: {contact.last_name}\n   Phone: {contact.phone}\n   Address: {contact.address}\n   City: {contact.city}\n   Zip: {contact.zip_code}")
          else:
              print("No contacts found.")

      # Modifies a contact
      elif choice == 4:
          first_name = input("Enter first name: ")
          last_name = input("Enter last name: ")
          found = False
          for contact in contacts:
              if contact.first_name.lower() == first_name.lower() and contact.last_name.lower() == last_name.lower():
                  print("Contact Found:")
                  print(contact)
                  modify_contact(contact)
                  contacts.sort()
                  found = True
                  break
          if not found:
              print("Contact not found.")

      # Saves and quits
      elif choice == 5:
          write_file(filename, contacts)
          print("Saving File...")
          print("Ending Program")
          break
      else:
          print("Invalid choice. Please try again.")

main()
