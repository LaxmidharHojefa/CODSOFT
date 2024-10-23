# Contact Management System

contacts = []

def add_contact():
    """Add a new contact to the list."""
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    
    contacts.append(contact)
    print(f"\nContact for {name} added successfully!\n")

def view_contacts():
    """Display the list of all contacts."""
    if not contacts:
        print("\nNo contacts available.\n")
        return
    
    print("\nContact List:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")
    print()

def search_contact():
    """Search for a contact by name or phone number."""
    query = input("\nEnter name or phone number to search: ").lower()
    found_contacts = [c for c in contacts if query in c['name'].lower() or query in c['phone']]
    
    if found_contacts:
        print("\nSearch Results:")
        for contact in found_contacts:
            print_contact_details(contact)
    else:
        print("\nNo contact found matching the search.\n")

def print_contact_details(contact):
    """Helper function to print detailed contact information."""
    print(f"\nName: {contact['name']}")
    print(f"Phone: {contact['phone']}")
    print(f"Email: {contact['email']}")
    print(f"Address: {contact['address']}\n")

def update_contact():
    """Update an existing contact."""
    query = input("\nEnter the name or phone number of the contact to update: ").lower()
    found_contacts = [c for c in contacts if query in c['name'].lower() or query in c['phone']]
    
    if not found_contacts:
        print("\nNo contact found to update.\n")
        return

    contact = found_contacts[0]
    print("\nCurrent Contact Details:")
    print_contact_details(contact)
    
    print("\nEnter new details (press Enter to keep existing values):")
    name = input(f"New name [{contact['name']}]: ") or contact['name']
    phone = input(f"New phone number [{contact['phone']}]: ") or contact['phone']
    email = input(f"New email [{contact['email']}]: ") or contact['email']
    address = input(f"New address [{contact['address']}]: ") or contact['address']
    
    contact.update({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    
    print(f"\nContact for {name} updated successfully!\n")

def delete_contact():
    """Delete a contact."""
    query = input("\nEnter the name or phone number of the contact to delete: ").lower()
    found_contacts = [c for c in contacts if query in c['name'].lower() or query in c['phone']]
    
    if not found_contacts:
        print("\nNo contact found to delete.\n")
        return
    
    contact = found_contacts[0]
    print("\nContact to be deleted:")
    print_contact_details(contact)
    
    confirm = input("Are you sure you want to delete this contact? (yes/no): ").lower()
    if confirm == "yes":
        contacts.remove(contact)
        print(f"\nContact for {contact['name']} deleted successfully!\n")
    else:
        print("\nDelete action canceled.\n")

def menu():
    """Display the menu and get user input."""
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")
    return choice

def contact_manager():
    """Main function to manage the contact list."""
    print("Welcome to Contact Manager")

    while True:
        choice = menu()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("\nExiting Contact Manager. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please enter a valid option.\n")

if __name__ == "__main__":
    contact_manager()
