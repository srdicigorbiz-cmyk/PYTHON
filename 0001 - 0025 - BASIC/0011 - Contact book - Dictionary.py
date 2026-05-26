# Menu
def display_menu():
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")
# Add contact
def add_contact(contact_book):
    # input the contact data
    name = input()
    phone = input()
    email = input()
    address = input()
    # check is name in dic
    if name in contact_book:
        print("Contact already exists!")
    else:
        contact_book[name] = {
	                            "phone": phone,
	                            "email": email,
	                            "address": address
                            }
        print("Contact added successfully!")

def view_contact(contact_book):
    search_word = input()
    if search_word in contact_book:
        print(f"Name: {search_word}")
        print(f"Phone: {contact_book[search_word]['phone']}")
        print(f"Email: {contact_book[search_word]['email']}")
        print(f"Address: {contact_book[search_word]['address']}")
    else:
        print("Contact not found!")
def edit_contact(contact_book):
    search_word = input()
    if search_word in contact_book:
        phone = input()
        email = input()
        address = input()
        if phone != "":
            contact_book[search_word]["phone"]=phone
        if email != "":
            contact_book[search_word]["email"]=email
        if address != "":
            contact_book[search_word]["address"]=address
        print("Contact updated successfully!")
    else:
        print("Contact not found!")
def delete_contact(contact_book):
    search_word = input()
    if search_word in contact_book:
        del(contact_book[search_word])
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")