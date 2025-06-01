from storage import load_contacts, save_contacts
from contact import Contact
from interaction import days_since
from ui import Colors, print_contact, print_reminder

contacts =  load_contacts() or {
    "Biruk Zewdu": {
        "phone": "0945367823",
        "email": "birukzewdu245@gmail.com",
        "last_contact": "2025-03-01",
        "category": 'Friend',
        "interactions": ["2024-11-28", "2025-01-15", "2025-03-01"]
    },
    "yilkal Kebede": {
        "phone": "0972123256",
        "email": "yheys345@gmail.com",
        "last_contact": "2025-05-10",
        "category": 'Family',
        "interactions": ["2025-04-28", "2025-05-10"]

    },
    "Endale Biru": {
        "phone": "0965743613",
        "email": "endalebiru03@gmail.com",
        "last_contact": "2025-05-25",
        "category": 'Family',
        "interactions": ["2025-04-29", "2025-05-15"]
    },
    "Meklit Kiros": {
        "phone": "0990345632",
        "email": "meklitkir76@gmail.com",
        "last_contact": "2024-12-10",
        "category": 'Friend',
        "interactions": ["2024-09-10", "2024-12-10", "2025-04-18"]
    }

}

def display_contacts():
    """Show all contacts with basic info"""
    print(f"\n{Colors.GREEN}--- CONTACTS ---{Colors.RESET}")
    for name, info in contacts.items():
        print_contact(name, info)

def add_contact():
    """Add a new contact to the book"""
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()
    category = input("Enter Category(family, friend, etc.): ").strip()
    
    # Contact class for validation of contact number
    new_contact = Contact(name, phone, email, category)
    if not new_contact.validate():
        print("Invalid phone number!")
        return

    contacts[name] = {
        "phone": new_contact.phone,
        "email": new_contact.email,
        "last_contact": "Never",
        "category": new_contact.category,
        "interactions": []
    }
    print(f"✓ {name} added!")

def delete_contact():
    """Remove a contact"""
    name = input("Enter the name you want to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"✗ {name} deleted.")
    else:
        print("Contact not found!")

def log_interaction():
    """Record a new interaction with date"""
    name = input("Enter contact name: ").strip()
    if name not in contacts:
        print("Contact not found!")
        return
    
    date = input("Enter date (YYYY-MM-DD): ").strip()
    contacts[name]["last_contact"] = date
    contacts[name]["interactions"].append(date)
    print(f"📅 Logged interaction with {name} on {date}")

def show_stats():
    """Display interaction statistics"""
    name = input("Enter contact name: ").strip()
    if name not in contacts:
        print("Contact not found!")
        return
    
    data = contacts[name]
    days = days_since(data["last_contact"])
    
    print(f"\n Stats for {name}:")
    print(f"Last contact: {data['last_contact']} ({int(days)} days ago)")
    print(f"Total interactions: {len(data['interactions'])}")
    
    # Interaction frequency
    if len(data["interactions"]) > 1:
        first = min(data["interactions"])
        last = max(data["interactions"])
        print(f"First interaction: {first} | Last: {last}")

def check_reminders():
    """Show contacts not interacted with in >30 days"""
    print(f"\n{Colors.RED}--- REMINDERS ---{Colors.RESET}")
    inactive = []
    
    for name, data in contacts.items():
        days = days_since(data["last_contact"])
        if days > 30:
            inactive.append((name, days))
    
    if not inactive:
        print("No inactive contacts!")
    else:
        for name, days in inactive:
            print(f"⚠️ Contact {name} ({int(days)} days since last interaction)")

def main_menu():
    """Main user interface"""
    try:
        while True:
            print(f"\n{Colors.BLUE}📖 SMART CONTACT BOOK{Colors.RESET}")
            print("1. View Contacts")
            print("2. Add Contact")
            print("3. Delete Contact")
            print("4. Log Interaction")
            print("5. View Stats")
            print("6. Check Reminders")
            print("7. Exit")
        
            choice = input("Choose an option (1-7): ").strip()
        
            if choice == "1":
                display_contacts()
            elif choice == "2":
                add_contact()
            elif choice == "3":
                delete_contact() 
            elif choice == "4":
                log_interaction()
            elif choice == "5":
                show_stats()
            elif choice == "6":
                check_reminders()
            elif choice == "7":
                print("Have A Nice Time!")
                break
            else:
                print("Invalid choice!")
    finally:
        save_contacts(contacts)  # Auto-save on exit    

if __name__ == "__main__":
    main_menu()