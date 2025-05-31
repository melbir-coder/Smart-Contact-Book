import json

def save_contacts(contacts):  # Takes YOUR contacts dictionary
    with open('contacts.json', 'w') as f:
        json.dump(contacts, f)

def load_contacts():
    try:
        with open('contacts.json') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}  # Returns empty dict like your original