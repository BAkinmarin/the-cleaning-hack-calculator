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
    print('DO NOT forget to press ENTER after each input...\n')


def get_user_details():
    """
    Get personal details from user then run validation.
    """
    while True:
        details_str = []
        name_str = input('Enter your name: \n')
        mobile_str = input('Enter your mobile number: \n')
        email_str = input('Enter your email address: \n')

        if validate_user_name(name_str) and validate_user_mobile(mobile_str) and validate_user_email(email_str):
            print(f"Thanks, {name_str}! Now, let's get you that estimate...")
            print('Please note that this amount may increase depending on condition upon arrival.\n')
            print('Please enter room details as whole numbers.')
            
            details_str = name_str, mobile_str, email_str
                
            break
        
    return details_str


def get_property_details():
    """
    Get property details from user then run validation.
    """
    property_str = []
   
    while True:
        no_of_bedrooms = input('No. of bedrooms: \n')
        no_of_bathrooms = input('No. of bathrooms (include separate toilets): \n')
        no_of_livingrooms = input('No. of living rooms (include office, conservatory): \n') 
        no_of_otherrooms = input('Any other rooms (include kitchen, utility): \n')

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
    # Declared as global variable to enable access inside other functions and keep personalised theme
    global user_name 
    user_name = user[-1][0]
    print(f'Thank you, {user_name}! Just getting your estimate now...')


def calculate_estimate(property_values):
    """
    Calculates cleaning estimate using pre-defined formula based on 
    number of rooms provided by user.
    """
    print(f'You entered {property_values[0]} Bedroom(s), {property_values[1]} Bathroom(s), {property_values[2]} Living-room(s) and {property_values[3]} Other room(s).')    
    estimate_value = []
    total_estimate = 0

    bedrooms = property_values[0] * 15
    bathrooms = property_values[1] * 30
    livingrooms = property_values[2] * 20
    otherrooms = property_values[3] * 30

    # Round calculation down to 2 decimal places
    total_estimate = round(((bedrooms + bathrooms + livingrooms + otherrooms) * 1.15), 2)
    estimate_value = total_estimate
    return f'Based on your entry, we estimate it will cost around £{total_estimate} to get your property cleaned.\n'


def get_new_estimate():
    """
    Requests if user would like to obtain another extimate or exit program.
    """
    while True:
        new_estimate = input('Enter "Y" for new estimate or any other key to exit: ')

        if new_estimate.lower() == 'y':
            new_rooms = get_property_details()
            new_property_values = [int(num) for num in new_rooms]
            update_worksheet(details, new_rooms)
            new_estimate = calculate_estimate(new_property_values)
            print(new_estimate)      
        else:
            print(f'Thanks for your enquiry, {user_name}! A member of our team will be in touch within 24 hours.')  
            break  


def main():
    """
    Main function to run all program functions.
    """
    hello_user()
    # Declared as a global variable to enable access inside get_new_estimate()
    global details
    details = get_user_details()
    rooms = get_property_details()
    # Convert rooms from strings to integers
    property_values = [int(num) for num in rooms]
    update_worksheet(details, rooms)
    estimate = calculate_estimate(property_values)
    print(estimate)
    get_new_estimate()

main()