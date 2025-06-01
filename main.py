contacts = {
    "Biruk Zewdu": {
        "phone": "0945367823",
        "email": "birukzewdu245@gmail.com",
        "last_contact": "2025-03-01",
        "category": 'Friend',
        "interactions": ["2025-01-15", "2025-03-01", "2025-04-29"]
    },
    "yilkal Kebede": {
        "phone": "0972123256",
        "email": "yheys345@gmail.com",
        "last_contact": "2025-05-10",
        "category": 'Family',
        "interactions": ["2025-04-28", "2025-05-10", "2025-05-23"]

    },
    "Endale Biru": {
        "phone": "0965743613",
        "email": "endalebiru03@gmail.com",
        "last_contact": "2025-05-25",
        "category": 'Family',
        "interactions": ["2025-04-29", "2025-05-15", "2025-05-25"]
    },
    "Meklit Kiros": {
        "phone": "0990345632",
        "email": "meklitkir76@gmail.com",
        "last_contact": "2024-12-10",
        "category": 'Friend',
        "interactions": ["2024-09-10", "2024-12-10"]
    }

}

def display_contacts():
    """Show all contacts with basic info"""
    print("\n--- CONTACTS ---")
    for name, info in contacts.items():
        print(f"{name} | Phone: {info['phone']} | Last contact: {info['last_contact']} | Category: {info['category']}")

def add_contact():
    """Add a new contact to the book"""
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()
    category = input("Enter Category(family/friend, etc.): ").strip()
    
    contacts[name] = {
        "phone": phone,
        "email": email,
        "last_contact": "Never",
        "category": category,
        "interactions": []
    }
    print(f"✓ {name} added!")

def delete_contact():
    """Remove a contact"""
    name = input("Enter name to delete: ").strip()
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

def calculate_days_since(last_date):
    """Calculate days since last contact (simplified)"""
    if last_date == "Never":
        return float('inf')
    
    # For simplicity, assume today is 2025-10-10
    year, month, day = map(int, last_date.split("-"))
    return (2025 - year) * 365 + (10 - month) * 30 + (10 - day)

def show_stats():
    """Display interaction statistics"""
    name = input("Enter saved contact name: ").strip()
    if name not in contacts:
        print("Contact not found!")
        return
    
    data = contacts[name]
    days = calculate_days_since(data["last_contact"])
    
    print(f"\n Stats for {name}:")
    print(f"Last contact: {data['last_contact']} ({int(days)} days ago)")
    print(f"Total interactions: {len(data['interactions'])}")
    
    # Interaction frequency (simplified)
    if len(data["interactions"]) > 1:
        first = min(data["interactions"])
        last = max(data["interactions"])
        print(f"First interaction: {first} | Last: {last}")

def check_reminders():
    """Show contacts not interacted with in >30 days"""
    print("\n--- REMINDERS ---")
    inactive = []
    
    for name, data in contacts.items():
        days = calculate_days_since(data["last_contact"])
        if days > 30:
            inactive.append((name, days))
    
    if not inactive:
        print("No inactive contacts!")
    else:
        for name, days in inactive:
            print(f"⚠️ Contact {name} ({int(days)} days since last interaction)")

def main_menu():
    """Main user interface"""
    while True:
        print("\n📖 SMART CONTACT BOOK")
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
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")
if __name__ == "__main__":
    main_menu()