# Import relevant libraries and credentials
import gspread
from google.oauth2.service_account import Credentials

# Import RegEx package for email validation
import re

# APIs for project scope
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('the-cleaning-hack-calculator')

#quotes = SHEET.worksheet('quotes')
#data = quotes.get_all_values()
#print(data)

def hello_user():
    """
    Display welcome message and instructions to user.
    """
    print('Welcome to The Cleaning Hack!')
    print('To get your free cleaning estimate, you will need to provide your contact details and answer a few questions regarding your property.')
    print('Please hit ENTER after each input...\n')

    choice_str = input('Do you wish to continue? Y or N: ')

def get_user_details():
    """
    Get details personal details from user and add to sheet.
    """
    details_str = []
    name_str = input('Enter your name: ')
    mobile_str = input('Enter your mobile number: ')
    email_str = input('Enter your email address: ')

    details_str = name_str, mobile_str, email_str
    validate_user_mobile(mobile_str)
    validate_user_email(email_str)  
               
def validate_user_mobile(user_mobile):
    """
    Converts strings to integers.
    Raises ValueError if conversion fails.
    Also Checks mobile number matches UK format.
    """
    try:
        if len(user_mobile) != 11:
            raise ValueError(f'Your mobile number needs to be 11 digits. You provided {len(user_mobile)}')
    except ValueError as e:
        print(f'Invalid Mobile Number: {e}. Please enter a valid UK number.\n')   

def validate_user_email(user_email):
    """
    Checks that email syntax provided is valid.
    Raises EmailNotValidError if validation fails.
    """
    pattern = re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]*\.*[com|org|edu]{3}$)", user_email)
    try:
        if user_email != pattern:
            raise ValueError(f'Your email address is invalid. You provided {user_email}')
    except ValueError as e:
        print(f'Invalid Email Address: {e}. Please enter your email address in the format: myaddress@email.com.\n') 
    

get_user_details()