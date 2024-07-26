# Import relevant libraries and credentials
import gspread
from google.oauth2.service_account import Credentials

# Import relevant package for email validation
from email_validator import validate_email, EmailNotValidError

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
               
def validate_user_mobile(mobile):
    """
    Converts strings to integers.
    Raises ValueError if conversion fails.
    Checks mobile number is 11 digits long.
    """
    try:
        if len(mobile) != 11:
            raise ValueError(f'Your mobile number needs to be 11 digits. You entered {len(mobile)}')
    except ValueError as e:
        print(f'Invalid Mobile Number: {e}. Please enter a valid UK number.\n')   

def validate_user_email(email):
    """
    Checks that email syntax provided is valid.
    Raises EmailNotValidError if validation fails.
    """
    try:
        email_format = validate_email(email)  # validate and get info
        email = email_format.normalized  # replace with normalized form
    except EmailNotValidError as e:
        # email is not valid, exception message is human-readable
        print(str(e))


get_user_details()