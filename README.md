# Smart-Contact-Book  

## Description 
A Python-based contact management system that goes beyond basic storage by tracking interactions, calculating days since last contact, and providing reminders for inactive contacts. This tool helps users maintain relationships by identifying contacts they haven't communicated with in over 30 days and displaying key statistics about their interactions.

## Installation & Setup

1. Clone the repository:  
   ```bash  
   git clone https://github.com/melbir-coder/Smart-Contact-Book.git
- This creates a local copy of all project files in a folder named "Smart-Contact-Book"
- Ensure you have Git installed on your system before running this command
2. Navigate to the project directory:
   ```bash   
   cd smart-contact-book
- This changes your current working directory to the project root
3. Run the application:
   ```bash
   python main.py
- This executes the main Python script that launches the application
- You should see output in your terminal indicating the application is running

## Additional Notes

### System Requirements
- Python 3.6 or higher
- Git (for cloning the repository)
### Troubleshooting
If you encounter any issues:
- Check your Python version with
  ``` bash
  python --version
- Verify you're in the correct directory

### Git Installation Guide
Before cloning the repository, ensure Git is installed on your system:

#### Windows
- Download Git from [Go to git.com](https://git-scm.com/).
- Run the installer and follow the prompts (use default settings).
- Verify installation by opening Command Prompt and running:
  ``` bash
  git --version
#### macOS
- Option 1: Install via Homebrew (recommended):
  ``` bash 
  brew install git
- Option 2: Download from [Go to git.com](https://git-scm.com/).
- Verify with:
  ``` bash
  git --version

## Features

### Contact Management
- **View Contacts**: Displays a formatted list of all saved contacts, showing:
  - Name
  - Phone number
  - Last contact date
  - Category (e.g., Friend/Family)
- **Add/Delete Contacts**: Easily manage your contact list with add/remove functionality.  Allows users to add a new contact by entering:
   - Name
   - Phone number
   - Email address  Removes a contact by name (Automatically sets last_contact to "Never" and initializes an empty interactions list.)
### Interaction Tracking
- **Log Interactions**: Records a new interaction with a contact by:
  - Entering a date (YYYY-MM-DD format)
  - Updates the last_contact field
  - Appends the date to the interactions list
- **Last Contact Indicator**:
  - Computes how many days have passed since the last interaction.
  - Handles edge cases (e.g., "Never" contacted).
### Statistics & Insights
- View Contact Stats For a selected contact, shows:
  - Last contact date and days elapsed
  - Total number of interactions
  - First/last interaction dates (if available)
### Smart Reminders
- **Inactivity Alerts**: 
Identifies "inactive" contacts (no interaction in >30 days) and flags them with:
  - Contact name
  - Days since last interaction

## Group Members

| Name             | ID Number   |
|------------------|-------------|
| Biruk Zewdu      | UGR/9623/17 |
| Meklit Kiros     | UGR/0511/17 |
| Yilikal Kebede   | UGR/8385/17 |
| Endale Biru      | UGR/4513/17 |
