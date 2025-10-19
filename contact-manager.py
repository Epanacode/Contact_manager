import json

# -----------------------------
# ذخیره و بارگذاری مخاطب‌ها
# -----------------------------

def save_contacts():
    with open("contacts.json", "w") as f:
        json.dump(contacts, f, indent=4)

def load_contacts():
    global contacts
    try:
        with open("contacts.json", "r") as f:
            contacts = json.load(f)
    except FileNotFoundError:
        contacts = []

# -----------------------------
# شروع برنامه
# -----------------------------

contacts = []
load_contacts()

while True:
    print("\n📒 Contact Manager")
    print("1. Add contact")
    print("2. Show contacts")
    print("3. Delete contact")
    print("4. Search contact")
    print("5. Exit")
    
    choice = input("Choose an option : ")
    
    if choice == '1':
        name = input("Enter name: ")
        age = input("Enter age: ")
        email = input("Enter email: ")
            
        contact = {
            "name" : name,
            "age" : age,
            "email" : email
        }
        
        contacts.append(contact)
        save_contacts()
        print(f"✔ Contact {name} added successfully!")
    
    elif choice == '2':
        if not contacts:
            print("⚠️ No contacts found")
        else:
            print("\n 🌙 Contact list :")
            for i, contact in enumerate(contacts, start=1):
                print(f"{i}. Name: {contact['name']}, Age: {contact['age']}, Email: {contact['email']}")
            print("-----------------------")
    
    elif choice == '3':
        if not contacts:
            print("⚠️ No contact to delete!")
        else:
            print("\n 🌙 Contact list :")
            for i, contact in enumerate(contacts, start=1):
                print(f"{i}. Name: {contact['name']}, Age: {contact['age']}, Email: {contact['email']}")
            try:
                number = int(input("Enter the number of the contact to delete: "))
                if 1 <= number <= len(contacts):
                    deleted = contacts.pop(number - 1)
                    save_contacts()
                    print(f"🗑️ Deleted : {deleted['name']}")
                else:
                    print("❌ Invalid number!")
            except ValueError:
                print("Please enter a valid number!")
    
    elif choice == '4':
        if not contacts:
            print("⚠️ No contact to search!")
        else:
            query = input("Enter name to search : ").lower()
            found = False
            print("\n🔎 Search Results:")
            for contact in contacts:
                if query in contact["name"].lower():
                    print(f"Name: {contact['name']}, Age: {contact['age']}, Email: {contact['email']}")
                    found = True
            if not found:
                print("❌ No contacts found with that name.")
    
    elif choice == '5':
        print("👋 Goodbye!")
        break
    
    else:
        print("❌ Invalid choice. Please try again.")
