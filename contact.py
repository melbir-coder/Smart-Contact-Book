class Contact:
    def __init__(self, name, phone, email, category):
        self.name = name
        self.phone = phone  # Will be validated
        self.email = email
        self.category = category
    
    def is_valid_phone(self):
        return len(self.phone) == 10 and self.phone.isdigit()