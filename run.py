# Import relevant libraries and credentials
import gspread
from google.oauth2.service_account import Credentials

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
    print('Please confirm if you wish to continue...\n')

    choice_str = input('Do you wish to continue? Y or N: ')
    
#hello_user()

def get_user_details():
    """
    Get details personal details from user and add to sheet.
    """
    details_str = []
    name_str = input('\nEnter your name: ')
    mobile_str = input('Enter your mobile number: ')
    email_str = input('Enter your email address: ')


    details_str = name_str, mobile_str, email_str
    data_validation(details_str)
    #print(details_str)

#get_user_details() 

def data_validation(details):
    """
    Converts strings to integers and integers to strings.
    Raises ValueError if conversion fails or if mobile and email format incorrect.
    """
    try:
        if len(mobile_str) != 11:
            raise ValueError(
                f'Your mobile number needs to be 11 digits. You provided {len(details)}. Please enter a valid UK mobile number.')
    except ValueError as e:
        print(f'Invalid data: {e}, please try again.\n')     
               
get_user_details()