#Initialize an empty address book dictionary
address_book = {}
#Function to add a new contact to the address book
def add_contact(name, phone_number):
    address_book[name] = phone_number
    print(f"Added{name} to the address book.")


#Function to display all contacts in the address book
def display_contacts():
        print("Address Book:")
        for name, phone_number in address_book.items():
            print(f"Name: {name}, Phone Number: {phone_number}")
            

#function to search for contact by name
def search_contact(name):
    if name in address_book:
        print(f"Name: {name}, Phone number: {address_book[name]}")

    else:
        print(f"{name} not found in the address book")

#function to delete for a contact by name
def delete_contact(name):
    if name in address_book:
        del address_book[name]
        print(f"Deleted {name} from address book.")
    else:
        print(f"{name} not found in the address book.")

#main menu
while True:
    print("\nAddress Book Menu:")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    c = input("Enter you choice here")

    if c == "1":
        name = str(input("Enter the name here"))
        phone = int(input("What is the number?"))
        add_contact(name,phone)
    elif c == "2":
        display_contacts()
    elif c == "3":
        j = str(input("Enter the name here"))
        search_contact(j)
    elif c == "4":
        k = str(input("Enter the name here"))
        delete_contact(k)
    elif c == "5":
        print("Exiting...")
        break
    else:
        print("Invaid choice.Please enter a number between 1 and 5.")
