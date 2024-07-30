# The Cleaning Hack Calculator


## A Python command line calculator
> This application is a Python based calculation for a real cleaning company, The Cleaning Hack, which is used to produce a free cleaning estimate for potential clients. The application requires the user to enter their name, mobile number and email which is validated prior to entering the details required to produce an estimate such as number of bedrooms, bathrooms, living spaces.

#### Designed and Developed by Bola Akinmarin

### **[Live site](https://)**


### **[Repository](https://)**

  
## Table of contents


 1. [ Pre-Project Planning ](#plan)  
 2. [ Features Left to Implement ](#left)  
 3. [ Technology used ](#tech) 
 4. [ Testing ](#testing)  
 5. [ Bugs ](#bugs)  
 6. [ Deployment](#deployment)
 7. [ Credits](#credits)
 8. [ Content](#content)  
 9. [ Acknowledgements](#acknowledgements)  


## Flow

<a name="plan"></a>
### Pre-project Planning

> 

> Please see the below flow chart to better understand the initial design and concept
![Lucid Flow Chart](https://)

### Pre-Planning Structure

### Structure


#### User Details

- Name

- Mobile 

- Email


#### Property Details

- No. of Bedrooms

- No. of Bathrooms 

- No. of Livingrooms

- Any other rooms


## Program Flow - 
> When the user loads the program, they are presented with a welcome message and instructions on how to interact with the program as seen below:
![Welcome Page](https://)

> The user will then be asked to enter their name, mobile and email which will be validated before they are allowed to move on to the next stage:
![User Details](https://)

> If validation fails, the user will be shown the following error messages depending on the exception raised:
![Missing Name](https://)

![Invalid Mobile Number](https://)

![Invalid Email](https://)

> Next, the user will be asked to provide number of bedrooms, bathrooms, livingrooms and any other rooms:
![No. of Bedrooms](https://)

![No. of Bathrooms](https://)

![No. of Livingrooms](https://)

![Any other rooms](https://)

> The details provided will be displayed to the user along with their estimate:
![Cleaning Estimate](https://)

> The user will then be asked if they want to continue i.e. obtain another estimate or exit the program:
![Continue or Exit](https://)

> If the user selects continue, they will be asked to enter property details for a new estimate:
![New Property Details](https://)

> If the user selects exit, the program will stop running:
![Exit](https://)

<a name="left"></a>

### Features left to implement

> Functionality to prompt user to enter only the specific piecce of information which fails validation.

> Functionality to validate mobile number to ensure only UK mobile numbers are provided.


<a name="tech"></a>
# Technology Used
### Python
Used to create the application.

### Heroku
Used to deploy and host the application.

### Github
Used to store the code.

### Gitpod
IDE used for creating the application.

### Git
Used for version control.

<a name="testing"></a>
# Testing


### Testing Phase

#### Manual Testing

| Test | Result |
|--|--|
|On run programme the welcome message appears|Pass|
|After welcome message user prompted for name|Pass|
|Once name is input the menu option presents|Pass|
|Selecting 1 from the menu starts the game|Pass|
|Selecting 2 from the menu opens the rules|Pass|
|Dealer hand hidden during first round|Pass|
|When player stands dealer card is shown|Pass|
|When player stands the endgame calculation runs to determin winner|Pass|
|If player wins the player is presented with a win message|Pass|
|If the player wins the ascii art for bender is shown|Pass|
|If the dealer wins the dealer score is incremented|Pass|
|If the dealer wins the player is given a lose message|Pass|
|If the hand is a tie the player is notified|Pass|
|If the hand is a tie, neither player or dealers score increases|Pass|

#### User tests

The following tests are on the error handling throughout the project.
If the error handling works as expected it will be marked as pass.
If it does not work as expected then it will be marked as a fail.
> Enter Name Field
Error Msg: User must enter a name of at least 3 characters and it must be all letters.

| Test | Result |
|--|--|
|User enters a name of less than 3 characters | Pass|
|User tried to enter 3 characters with a number|Pass|
|User tried to enter an empty string|Pass|
|User tried to enter a name with a space in it|Fail|

While I expected the error handling to deal with names of less than 3 characters and only letters, I did not think ahead in case users would want to add multiple word names. For example: 'Handsome Joe'. This will throw an error to the user and advise them of the Error Msg above. 

> Main menu options
Error Msg: Please select 1 to start game or 2 to read the rules

| Test | Result |
|--|--|
|User tried to enter a number other than 1 or 2 | Pass|
|User tried to enter a letter |Pass|
|User tried to enter an empty selection|Pass|
|User tried to enter a special symbol|Pass|

> Hit or stand option
Error Msg: Please enter H to hit or S to stand
As I have the function set to accept the input as .lower() either case style of H(h) or S(s) is considered valid in this programme

| Test | Result |
|--|--|
|User tried to enter a number on hit or stand choice | Pass|
|User tried to enter a letter other than H or S |Pass|
|User tried to enter an empty selection|Pass|
|User tried to enter a special symbol|Pass|

The following tests will show pass if the functionality works as intended or fail if it does not
> Play again option
Error Msg: Please enter Y to play again or any other key to exit

| Test | Result |
|--|--|
|User tried to enter y to play again  | Pass|
|User tried to enter a number to exit|Pass|
|User tried to enter any other letter than y to exit|Pass|
|User tried to enter a an empty string to exit |Fail|

### Pep8 Checker tool

> I used the Pep8 checker tool to validate my python code and ensure it was free from errors. As shown here:

![Pep8](https://)

<a name="bugs"></a>
## **Bugs**

### Notification Message- Details Complete
> Unable to get sequence of notification messages in email validation function working - program currently displays when user email is invalid but not when all details have been entered correctly. **Fixed**

### 
> Unable to format estimate figure correctly to support appending to current row in worksheet.

### 
> 

<a name="deployment"></a>
## Deployment

####
> To deploy the project to Heroku, I followed the steps outlined below:

1. Prepare run.py file by adding a new line character ("\n") at the end of the text inside all input methods.

2. Create list of requirements necessary for program to run on heroku by typing "pip3 freeze > requirements.txt" into the command line.

3. Navigate to heroku.com and log in.

4. Click "New" to create a new App.

5. Assign name to application, choose region and Click 'Create New App'.

6. On the next page click on the 'Settings' tab to adjust settings.

7. Click on the 'Config Vars' button.

8. Supply a 'KEY' of "CREDS" and 'Value' of contents of creds.json file. Then click the 'Add' button.

9. Supply a 'KEY' of "PORT" and 'Value' of "8000". Then click the 'Add' button.

10. Add buildpacks to install future dependencies needed outside of the requirements file.

11. Select 'Python' then 'Node.js' and click 'Save' - **Make sure they are in this order.**

12. Navigate to the deploy section and choose deployment method. 

13. To connect with github select 'Github' and confirm.

14. Search for repository, select it and click 'Connect'.

15. To deploy, choose one of the following options: 

- Automatic deploys - meaning Heroku will rebuild the app everytime a new change is pushed.
  - For this option, choose the branch to deploy and click 'Enable automatic deploys'. 
  - This can be changed to manual deployment at a later stage.

- Manual deployment - which deploys current state of branch.

16. Click 'Deploy branch'.

17. Click 'Open App' to launch application.

<a name="credits"></a>
## Credits

Multiple resources used to better understand the logic and flow of functions and classes Python.

### [Stack Overflow](https://stackoverflow.com/questions/8022530/how-to-check-for-valid-email-address)
> Useful for learning how to validate email addresses.

### [TechWithNash](https://www.youtube.com/watch?v=4AycrAPVKV0)
> Useful tutorial on how to build an advanced calculator with Python.

### [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-make-a-calculator-program-in-python-3)
> Useful step-by-step guide on how to create a calculator program.

### [PyPi](https://pypi.org/project/email-validator/)
> A robust email address syntax validation library installed for use with this project.

### [Medium](https://medium.com/hacktive-devs/gspread-automate-google-sheet-with-python-dc1fa7c65c21)
> Useful guide by Sogo Ogundowole on GSpread: Automate Google Sheet with Python. Helped broaden my understanding of GSpread methods and applications.


<a name="content"></a>
## Content and Resources

### w3 schools
> Used to reference Python Structure and play around with code ideas prior to including them in my project.

### Code Institute
> Project created in line with course content and within project 3 scope.

### Stack Overflow
> Used to review my own code to ensure simplicity where possible. 

### Youtube
> One of the most accessible learning platforms with a global reach. Very useful in broadening my approach to coding, providing insights into coding concepts from different perspectives.

### Digital Ocean

<a name="acknowlegements"></a>
## Acknowledgements

### Alan Bushell
> My mentor who provided me with great feedback and guidance at the inception of this project, helping to keep at the forefront the requirements for a successful project.

### Code Community
> Other software developers who gave feedback on their experience whilst interacting with The cleaning Hack Calculator.