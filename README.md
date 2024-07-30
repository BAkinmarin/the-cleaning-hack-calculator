# The Cleaning Hack Calculator


## A Python command line calculator
> This application is a Python based calculation for a real cleaning company, The Cleaning Hack, which is used to produce a free cleaning estimate for potential clients. The application requires the user to enter their name, mobile number and email which is validated prior to entering the details required to produce an estimate such as number of bedrooms, bathrooms, living spaces. These details are then uploaded to a Google Worksheet for the business owner to reference in follow-up conversations with the prospective client.

#### Designed and Developed by Bola Akinmarin

### **[Live site](https://the-cleaning-hack-calculator-7f6b677fafbc.herokuapp.com/)**


### **[Repository](https://github.com/BAkinmarin/the-cleaning-hack-calculator)**

  
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

> For my portfolio project 3, I wanted to address a real need hence my decision to create a cleaning estimate calculator for The Cleaning Hack, a real and active cleaning business. 

> Upon confirmation from the business owner that there was a gap in their processes where automation of cleaning estimates and, lead tracking were concerned, I was resolved in my decision.

> Utilising Lucid Chart, I created a flow diagram to help visualise the steps and logic I needed for the project design and execution to be as efficient as possible.

> Please see the below flow chart to better understand the initial design and concept.
![Lucid Flow Chart](assets/readme/tch-calculator-flowchart.png)

### Pre-Planning Structure

### Structure

#### User Details

- Name

- Mobile 

- Email

This information feeds into the business owner's lead generation and management system.


#### Property Details

- No. of Bedrooms

- No. of Bathrooms 

- No. of Livingrooms

- Other rooms

This information allows the business owner to predict how long a job might take ans assign resources accordingly. 


## Program Flow
> When the user loads the program, they are presented with a welcome message and instructions on how to interact with the program as seen below.

> The user will also be prompted to enter their name, followed by their mobile number and email address which will be validated before they can then move on to entering relevant property details.

![Welcome Page](assets/readme/tch-calculator-welcome.png)

> If validation fails at this stage, the user will be shown the corresponding error message or messages depending on the exception raised:

![Invalid Name](https://)

![Invalid Mobile Number](assets/readme/tch-calculator-invalid-mobile.png)

![Invalid Email](https://)

![All Details Invalid](assets/readme/tch-calculator-all-details-invalid.png)

> Next, the user will be asked to provide number of bedrooms, bathrooms, living areas / receptions and any other rooms:

![No. of Bedrooms](assets/readme/tch-calculator-bedrooms-prompt.png)

![No. of Bathrooms](assets/readme/tch-calculator-bathrooms-prompt.png)

![No. of Living areas](assets/readme/tch-calculator-living-areas-prompt.png)

![Any other rooms](assets/readme/tch-calculator-other-rooms-prompt.png)

> The details provided will be displayed to the user along with their estimate.

> Additionally, the user will be asked if they would like to get a new estimate or exit the program as seen below:

![Cleaning Estimate](assets/readme/tch-calculator-estimate.png)

> If the user selects new estimate, they will be asked to enter property details for a new estimate:

![New Details](assets/readme/tch-calculator-new-room-details-prompt.png)

> If the user selects exit, they will be presented with an exit message and the program will stop running:

![Exit Message](assets/readme/tch-calculator-exit-message.png)

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
|On run programme the welcome message and instructions appear|Pass|
|After instructions, user is prompted for name|Pass|
|Once name is input user is prompted for mobile number|Pass|
|Once mobile number is input, user is prompted for email address|Pass|
|Feedback message shows with further instructions on how to enter property details|Pass|
|After instructions, user is prompted for no. of bedrooms|Pass|
|Once no. of bedrooms is input, user is prompted for no. of bathrooms|Pass|
|Once no. of bathrooms is input, user is prompted for no. of livingrooms|Pass|
|Once no. of livingrooms is input, user is prompted for other rooms|Pass|
|Once no. of other rooms is input, feedback message is displayed with estimate|Pass|
|User is then asked if they want to obtain another quote or exit program|Pass|
|If user selects obtain another quote, user is again prompted to enter new property details|Pass|
|Once new property details have been entered, user is provided with new estimate|Pass|
|If user selects exit program, user is shown exit message and program ends|Pass|

#### User testing

The following tests are on error handling throughout the project.
If the error handling works as expected it will be marked as pass.
If the error handling does not work as expected it will be marked as fail.

> Enter Name
Error Msg: User must enter a name of at least two characters and it must be all letters.

| Test | Result |
|--|--|
|User tried to enter a name of less than two characters|Not Tested|
|User tried to enter a hyphenated name|Pass|
|User tried to enters an empty string|Pass|
|User tried to enter a name with a space in it|Pass|
|User tried to enter numbers|Fail|

> Enter Mobile Number
Error Msg: Your number needs to be 11 digits. Please enter a valid UK number.

| Test | Result |
|--|--|
|User tried to enter a number less than 11 digits|Pass|
|User tried to enter a letter|Not Tested|
|User tried to enter an empty selection|Pass|
|User tried to enter a symbol|Not Tested|
|User tried to enter a special character|Not Tested|

> Enter Email Address
Error Msg: Various EmailNotValidError messages.

| Test | Result |
|--|--|
|User tried to enter email without @ symbol|Pass|
|User tried to enter email without domain|Not Tested|
|User tried to enter an empty string|Pass|
|User tried to enter email without preceeding name before @ symbol|Pass|
|User tried to enter a special character|Not Tested|

> Enter Property Details
Error Msg: You must provide number of rooms. Please enter 0 if not applicable.

| Test | Result |
|--|--|
|User tried to enter a letter|Not Tested|
|User tried to enter an empty string|Pass|
|User tried to enter a special character|Not Tested|
|User tried to enter a mix of letters and numbers|Not Tested|


### Pep8 Checker tool

> I used the Pep8 checker tool to validate my python code to ensure it was free from errors as shown here:

![Pep8](assets/testing/pep8-checker.png)

> To keep within the length of 79 characters per line, I had to do a lot of re-coding and restructuring.

<a name="bugs"></a>
## **Bugs**

### Notification Message- Details Complete
> Unable to get sequence of notification messages in email validation function working - program currently displays when user email is invalid but not when all details have been entered correctly. **Fixed**

### 
> Unable to convert estimate data type to support appending to current row in worksheet.

### 
> Unable to add validation to name to stop users entering numbers into name field. **Fixed**

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

Multiple resources used to better understand the logic and flow of functions and capabilities of Python.

### [Stack Overflow](https://stackoverflow.com/questions/8022530/how-to-check-for-valid-email-address)
> Useful for learning how to validate email addresses.

### [PyPi](https://pypi.org/project/email-validator/)
> A robust email address syntax validation library installed for use with this project.

### [PyPi](https://pypi.org/project/colorama/)
> Useful for adding ANSI escape character sequences to add color to terminal text.

### [Medium](https://medium.com/hacktive-devs/gspread-automate-google-sheet-with-python-dc1fa7c65c21)
> Useful guide by Sogo Ogundowole on GSpread: Automate Google Sheet with Python. Helped broaden my understanding of GSpread methods and applications.

### [Finxter](https://blog.finxter.com/how-to-print-italic-text-in-python/)
> Useful guide for adding styles to text.


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

<a name="acknowlegements"></a>
## Acknowledgements

### Alan Bushell
> My mentor who provided me with great feedback and guidance at the inception of this project, helping to keep at the forefront the requirements for a successful project.

### Code Community
> Other software developers who gave feedback on their experience whilst interacting with The cleaning Hack Calculator.

### Family
> Special thanks to my family for supporting with user testing and providing feedback on flow and experience.