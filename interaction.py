from datetime import datetime

def days_since(last_date):
    if last_date == "Never":
        return float('inf')  # Means "never contacted"
    
    last_contact = datetime.strptime(last_date, "%Y-%m-%d")
    return (datetime.now() - last_contact).days