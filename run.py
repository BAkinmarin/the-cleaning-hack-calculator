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
    print('To get your free cleaning estimate, please provide your contact details.')
    print('Do not forget to press ENTER after each input...\n')

def get_user_details():
    """
    Get details personal details from user and add to sheet.
    """
    while True:
        details_str = []
        name_str = input('Enter your name: ')
        mobile_str = input('Enter your mobile number: ')
        email_str = input('Enter your email address: ')

        if validate_user_mobile(mobile_str) and validate_user_email(email_str):
            print('Thank you for providing your details!\n')
            # Obtain relevant information from user to calculate estimate and convert to integer
            print("Now, let's get you that estimate...")
            print('Please enter property details as whole numbers.\n')
            no_of_bedrooms = int(input('No. of bedrooms: '))
            no_of_bathrooms = int(input('No. of bathrooms (include separate toilets): '))
            no_of_livingrooms = int(input('No. of living rooms: '))
            no_of_other_rooms = input('Any other rooms i.e. kitchen, utility, conservatory: ')

            details_str = name_str, mobile_str, email_str, no_of_bedrooms, no_of_bathrooms, no_of_livingrooms, no_of_other_rooms

            break

    return details_str       
               
def validate_user_mobile(mobile_str):
    """
    Checks mobile number is 11 digits long.
    Raises ValueError if conversion fails.
    """
    try:
        if len(mobile_str) != 11:
            raise ValueError(f'Your mobile number needs to be 11 digits. You entered {len(mobile_str)}')
    except ValueError as e:
        print(f'Invalid Mobile Number: {e}. Please enter a valid UK number.\n')
        return False

    return True    

# This idea was inspired by Joshua Tauberer - maintains email-validator 2.2.0 on pypi.org
def validate_user_email(email_str):
    """
    Checks that email syntax provided is valid.
    Raises EmailNotValidError if validation fails.
    """
    try:
        email_format = validate_email(email_str)
        email = email_format.normalized
    except EmailNotValidError as e:
        print(str(e))
        print()
        return False

    return True       

def update_worksheet(details):
    """
    Add the details provided by the user to worksheet.
    Adds a new row to the quotes worksheet.
    Provides personalised confirmation to user of estimate being calculated.
    """      
    quotes_worksheet = SHEET.worksheet('quotes')
    quotes_worksheet.append_row(details)
    user = SHEET.worksheet('quotes').get_all_values()
    user_name = user[-1][0]
    print(f'\nThank you, {user_name}! Just getting your estimate...\n')    


hello_user()
details = get_user_details()
values = validate_property_details()
update_worksheet(details)