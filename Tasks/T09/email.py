### --- OOP Email Simulator --- ###

# 0: initial status
# 1: Read an email
# 2: View unread emails
status = 0

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email():
    # Declare the class variable, with default value, for emails. 
    has_been_read = False
    # Initialise the instance variables for emails.
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        self.has_been_read = True

# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox = []
# --- Functions --- #
# Build out the required functions for your program.
def populate_inbox():
    # Create 3 sample emails and add it to the Inbox list. 
    email_1 = Email("student1@gmail.com", "Welcome to HyperionDev!", "Content: Welcome to HyperionDev!")
    inbox.append(email_1)
    email_2 = Email("student2@gmail.com", "Great work on the bootcamp!", "Content: Great work on the bootcamp!")
    inbox.append(email_2)
    email_3 = Email("student3@gmail.com", "Your excellent marks!", "Content: Your excellent marks!")
    inbox.append(email_3)

# Create a function which prints the email’s subject_line, along with a corresponding number.
def list_emails():
    print(f"\nHere are total {len(inbox)} emails.")
    for index, element in enumerate(inbox):
        print(f"    {index}  {element.subject_line}")

# Create a function which displays a selected email.  
# return True: success  False: faile    
def read_email(index):
    try:
        email = inbox[index]
        print(f'''{index} index email's info:
        Email address:  {email.email_address}
        Subject line:   {email.subject_line}
        Email content:  {email.email_content}''')
        # Once displayed, call the class method to set its 'has_been_read' variable to True.
        email.has_been_read = True
        #email.mark_as_read()
        print(f"\nEmail from {email.email_address} marked as read.\n")
        return True
    except IndexError as e:
        print(f"--IndexError: {e}")
        return False


# --- Email Program --- #
# Call the function to populate the Inbox for further use in your program.
populate_inbox()

# Read an email
# return True: success  False: faile 
def read_an_email():
    list_emails()
    try:
        email_index = int(input("\nPleae select email index: "))
        return read_email(email_index)
    except ValueError as e:
        print(f"ValueError: {e}")
        return False

# View unread emails
def view_unread_emails():
    unread_emails_num = 0
    for email in inbox:
        if email.has_been_read == False:
            unread_emails_num += 1
    if unread_emails_num <= 0:
        print("All emails have been read.")
        return
        
    print("Here are unread emails: ")
    for index, element in enumerate(inbox):
        if element.has_been_read == False:
            print(f"    {index}  {element.subject_line}")

# Fill in the logic for the various menu operations.
#menu = True
while True:
    try:
        if status == 0:
            user_choice = int(input('''\nWould you like to:
            1. Read an email
            2. View unread emails
            3. Quit application

            Enter selection: '''))

        if user_choice == 1:
            # add logic here to read an email
            status = 1
            if read_an_email() == True:
                status = 0
        elif user_choice == 2:
            # add logic here to view unread emails
            status = 2
            view_unread_emails()
            status = 0
        elif user_choice == 3:
            # add logic here to quit appplication
            print("\nGoodbye!")
            status = 0
            break
        else:
            status = 0
            print("Oops - incorrect input.")
            
    except ValueError as e:
        status = 0
        print(f"ValueError: {e}")



