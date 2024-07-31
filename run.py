# Import relevant libraries and credentials
import gspread
from google.oauth2.service_account import Credentials

# Import relevant package for email validation
from email_validator import validate_email, EmailNotValidError

# Import module to clear terminal
import os

# Import colorama to add color to terminal input/output
import colorama
from colorama import Fore, Back, Style

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
    print('\x1B[1m' + 'Welcome to The Cleaning Hack' + '\x1B[0m')
    print('\033[1;3m' + 'Transforming Spaces To Transform Minds' + '\033[0m')
    print(Style.RESET_ALL)
    print('To get a free cleaning estimate, please enter your details.')
    print(Fore.RED + 'DO NOT forget to press ENTER after each input!')
    print(Style.RESET_ALL)


# This idea was inspired by Alan Bushell, Code Institute Mentor
def clear_terminal():
    """
    Clears terminal after specific functions to give user room.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def get_user_details():
    """
    Get personal details from user then run validation.
    """
    while True:
        details_str = []
        # Declared as global variable for early access
        global name
        name = input('Enter Full Name: \n')
        mob = input('Enter Mobile Number: \n')
        email = input('Enter Email Address: \n')

        if all([validate_name(name), validate_mob(mob), validate_user(email)]):
            # Capitalize name once validated and before uploading to worksheet
            name = name.capitalize()
            clear_terminal()
            print(f"\nThanks, {name}! Now, let's get you that estimate...")
            print('Please enter room details as whole numbers.')
            details_str = name, mob, email
            break

    return details_str


def get_property_details():
    """
    Get property details from user then run validation.
    """
    while True:
        bed_rooms = input('No. of bedrooms: \n')
        bath_rooms = input('No. of bathrooms (add toilets): \n')
        living_rooms = input('No. of living areas (add kitchen): \n')
        other_rooms = input('Any other rooms (add conservatory, utility): \n')

        val = bed_rooms, bath_rooms, living_rooms, other_rooms

        if validate_rooms(val):
            clear_terminal()
            print(f'Thanks, {name}! Just getting your estimate now...\n')
            break

    return val


def validate_name(name):
    """
    Checks that user's name is provided not left blank.
    Raises UnicodeError if validation fails.
    """
    try:
        # Character length and alpha check inspired by Alan Bushell, Mentor
        if name == '' or len(name) < 2 or not name.isalpha():
            raise NameError(f'Your name must be at least 2 letters')
    except NameError as e:
        print(Fore.RED + f'Invalid Data: {e}. Please try again.')
        print(Style.RESET_ALL)
        return False

    return True


def validate_mob(mob):
    """
    Checks mobile number is 11 digits long.
    Raises ValueError if conversion fails.
    """
    try:
        if len(mob) != 11 or not mob.isnumeric():
            raise ValueError(f'Your number must be 11 digits')
    except ValueError as e:
        print(Fore.RED + f'Invalid Number: {e}. Please try again.')
        print(Style.RESET_ALL)
        return False

    return True


# This idea was inspired by Joshua Tauberer - email-validator 2.2.0 on pypi.org
def validate_user(email):
    """
    Checks that email syntax provided is valid.
    Raises EmailNotValidError if validation fails.
    """
    try:
        email_format = validate_email(email)
        email = email_format.normalized
    except EmailNotValidError as e:
        print(Fore.RED + 'Invalid Email: ' + str(e))
        print(Style.RESET_ALL)
        return False

    return True


# This idea was inspired by Code Institute's Love Sandwiches project
def validate_rooms(values):
    """
    Checks that user has entered an integer for number of rooms.
    Converts strings to integers.
    Raises ValueError if conversion fails.
    """
    try:
        [int(value) for value in values]
        if len(values) != 4:
            print()
    except ValueError:
        clear_terminal()
        print(Fore.RED + f'Invalid Data: You entered {values}.')
        print('Enter only numbers OR "0" if not applicable.')
        print(Style.RESET_ALL)
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
    # Declared as global variable for access inside other functions
    global user_name
    user_name = user[-1][0]


def calculate_estimate(val):
    """
    Calculates cleaning estimate using pre-defined formula based on
    number of rooms provided by user.
    """
    print(f'The below estimate is based on your entry of:')
    print(f'{val[0]} Beds {val[1]} Baths {val[2]} Receptions {val[3]} Other\n')
    tot_est = 0

    beds = val[0] * 15
    baths = val[1] * 30
    livingrooms = val[2] * 20
    others = val[3] * 30

    # Round calculation down to 2 decimal places
    tot_est = round(((beds + baths + livingrooms + others) * 1.15), 2)

    return f'Your estimated total is £{tot_est}.'


def get_new_estimate():
    """
    Requests if user would like to obtain another extimate or exit program.
    """
    while True:
        new_estimate = input('Enter "Y" for new estimate or any key to exit: ')

        if new_estimate.lower() == 'y':
            clear_terminal()
            print('Please enter room details as whole numbers.')
            new_rooms = get_property_details()
            new_property_values = [int(num) for num in new_rooms]
            update_worksheet(details, new_rooms)
            new_estimate = calculate_estimate(new_property_values)
            print(new_estimate)
            print('\033[1;3m' + 'Heavy-duty surcharge may apply' + '\033[0m')
            print()
        else:
            clear_terminal()
            print(f"Thanks for your enquiry, {user_name}.")
            print('A member of our team will be in touch within 24 hours.')
            break


def main():
    """
    Main function to run all program functions.
    """
    hello_user()

    # Declared as a global variable to enable access inside get_new_estimate()
    global details
    details = get_user_details()

    global rooms
    rooms = get_property_details()

    # Convert rooms from strings to integers
    val = [int(num) for num in rooms]
    update_worksheet(details, rooms)
    estimate = calculate_estimate(val)
    print(estimate)
    print('\033[1;3m' + 'Heavy-duty surcharge may apply.' + '\033[0m')
    print()
    get_new_estimate()


main()
