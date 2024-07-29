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

def hello_user():
    """
    Display welcome message and instructions to user.
    """
    print('Welcome to The Cleaning Hack!')
    print('To get your free cleaning estimate, please provide your contact details.')
    print('Do not forget to press ENTER after each input...\n')


def get_user_details():
    """
    Get personal details from user then run validation.
    """
    while True:
        details_str = []
        name_str = input('Enter your name: ')
        mobile_str = input('Enter your mobile number: ')
        email_str = input('Enter your email address: ')

        if validate_user_name(name_str) and validate_user_mobile(mobile_str) and validate_user_email(email_str):
            print('Thank you for providing your details!\n')
            print("Now, let's get you that estimate...")
            print('Please note that estimate is subject to increase depending on property condition upon arrival.\n')
            print('Please enter room details as whole numbers.')
            
            details_str = name_str, mobile_str, email_str
                
            break
        
    return details_str


def get_property_details():
    """
    Get property details from user then run validation.
    """
    property_str = []

    no_of_bedrooms = input('No. of bedrooms: ')
    no_of_bathrooms = input('No. of bathrooms (include separate toilets): ')
    no_of_livingrooms = input('No. of living rooms (include office, conservatory): ') 
    no_of_otherrooms = input('Any other rooms (include kitchen, utility): ')

    property_str = no_of_bedrooms, no_of_bathrooms, no_of_livingrooms, no_of_otherrooms

    if validate_rooms(property_str):
        print()

    return property_str    


def validate_user_name(name_str):
    """
    Checks that user's name is provided not left blank.
    Raises UnicodeError if validation fails.
    """        
    try:
        if name_str == '':
            raise NameError(f'You failed to enter your name.')
    except NameError as e:
        print(f'Missing Data: {e}. Please try again.\n')    
        return False

    return True    


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


# This idea was inspired by Joshua Tauberer - email-validator 2.2.0 on pypi.org
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


# This idea was inspired by Code Institute's Love Sandwiches walkthrough project
def validate_rooms(values):
    """
    Checks that user has entered an integer for number of rooms.
    Converts strings to integers.
    Raises ValueError if conversion fails.
    """
    try:
        [int(value) for value in values]
        if len(values) != 4:
            raise ValueError('You must provide number of rooms.')
    except ValueError as e:
        print(f'Missing Details: {e}. Please enter 0 if not applicable.\n')        
        return False

    return True                        


def update_worksheet(details, rooms):
    """
    Add the details provided by the user to worksheet.
    Adds a new row to the quotes worksheet.
    Provides personalised confirmation to user of estimate being calculated.
    """  
    quotes_worksheet = SHEET.worksheet('quotes')
    quotes_worksheet.append_row(details + rooms)
    user = SHEET.worksheet('quotes').get_all_values()
    user_name = user[-1][0]
    print(f'Thank you, {user_name}!')
    print('Just getting your estimate now...\n')

def calculate_estimate(property_values):
    """
    Calculates cleaning estimate using pre-defined formula based on 
    number of rooms provided by user.
    """
    print(f'You entered {property_values[0]} bedrooms, {property_values[1]} bathrooms, {property_values[2]} living rooms and {property_values[3]} other rooms.')  
    estimate_value = []
    total_estimate = 0

    bedrooms = property_values[0] * 15
    bathrooms = property_values[1] * 30
    livingrooms = property_values[2] * 20
    otherrooms = property_values[3] * 30

    # Round calculation down to 2 decimal places
    total_estimate = round(((bedrooms + bathrooms + livingrooms + otherrooms) * 1.15), 2)
    estimate_value = total_estimate
    return f'Based on your entry, we estimate it will cost around £{total_estimate} to get your property cleaned.'


def main():
    """
    Main function to run all program functions.
    """
    #hello_user()
    details = get_user_details()
    rooms = get_property_details()
    # Convert rooms from strings to integers
    property_values = [int(num) for num in rooms]
    update_worksheet(details, rooms)
    estimate = calculate_estimate(property_values)
    print(estimate)
    

main()