'''
Exercise: Contact Book
Name: Pawan Shrestha
Day: 2
'''
#Input Value
contacts = {}

#Calculations
while True:
    print("\n===== Contact Book =====")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. Display all contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add contact
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        contacts[name] = {
            "phone": phone,
            "email": email
        }

        print("Contact added successfully!")

    # Search contact
    elif choice == "2":
        name = input("Enter name to search: ")

        if name in contacts:
            print("\nContact found!")
            print("Name:", name)
            print("Phone:", contacts[name]["phone"])
            print("Email:", contacts[name]["email"])
        else:
            print("Contact not found.")

    # Delete contact
    elif choice == "3":
        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    # Display all contacts
    elif choice == "4":
        if contacts:
            print("\n===== All Contacts =====")

            for name, details in contacts.items():
                print("Name:", name)
                print("Phone:", details["phone"])
                print("Email:", details["email"])
                print("------------------------")
        else:
            print("No contacts available.")

    # Exit
    elif choice == "5":
        print("Exiting Contact Book. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")