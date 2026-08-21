print("===== CONTACT BOOK =====")
print()
print("1. Add contact")
print("2. View contacts")
print("3. Search contact")
print("4. Delete contact")
print("5. Exit")
print()

contacts = []

def add_contact(name,phone,email):
    contact = {}
    contact["name"] = name
    contact["phone"] = phone
    contact["email"] = email
    return contact

def view_contacts(contacts):
    if not contacts:
        print("No contacts in the book.")
        return
    for index,contact in enumerate(contacts,start=1):
        print(f"{index}. {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print() 
def search_contact(contacts):
    if not contacts:
        print("No contacts in the book.")
        return
    name = input("Enter name: ").strip().title()
    for contact in contacts:
        if contact["name"] == name:
            print("Contact found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            return
        
    print("Contact not found.")
def delete_contact(contacts):
    if not contacts:
        print("No contacts in the book.")
        return
    name = input("Enter name: ").strip().title()
    for index,contact in enumerate(contacts):
        if contact['name'] == name:
            del contacts[index]
            print("Contact deleted successfully.")
            return
    print("Contact not found.")
while True:
    try:
        choice = int(input("Enter your choice (1-5): ").strip())
        if choice == 1:
            name  = input("Enter name: ").strip().title()
            phone = input("Enter phone number: ").strip()
            email = input("Enter email: ").strip()
            if not name or not phone or not email:
                print("Name, phone number, and email are required.")
                continue
            contact = add_contact(name,phone,email)
            contacts.append(contact)
            print("Contact added successfully.")
        elif choice == 2:
            view_contacts(contacts)
        elif choice == 3:
            search_contact(contacts)
        elif choice == 4:
            delete_contact(contacts)
        elif choice == 5:
            print("Exiting the contact book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")
