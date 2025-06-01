class Colors:
    RED = '\033[91m'    # Red color For warnings
    GREEN = '\033[92m'  # Green color For success messages
    BLUE = '\033[94m'   # Blue color For headers
    RESET = '\033[0m'   # Reset color

def print_contact(name, info):
    print(f"{name} | Phone: {info['phone']} | Last: {info['last_contact']} | Category: {info['category']}")

def print_reminder(message):
    print(f"{Colors.RED} ⚠️ {message}{Colors.RESET}")