class Colors:
    RED = '\033[91m'    # For warnings
    GREEN = '\033[92m'  # For success messages
    BLUE = '\033[94m'   # For headers
    RESET = '\033[0m'   # Reset color

def print_contact(name, info):
    print(f"{name} | Phone: {info['phone']} | Last: {info['last_contact']} | Category: {info['category']}")

def print_reminder(message):
    print(f"{Colors.RED}⚠️ {message}{Colors.RESET}")