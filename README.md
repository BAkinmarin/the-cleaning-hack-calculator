# The Cleaning Hack Calculator


## A Python command line calculator
> This application is a Python based calculation for a real cleaning company, The Cleaning Hack, which is used to produce a free cleaning estimate for potential clients. The application requires the user to enter their name, mobile number and email which is validated prior to entering the details required to produce an estimate such as number of bedrooms, bathrooms, living spaces.

### - By Bola Akinmarin

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
> When the user loads the program, they are presented with a welcome message and instructions as seen:
![Welcome Page](https://)

> The user will then be asked to enter their name, mobile and email which will be validated before moving on to the next stage:
![User Details](https://)

> If validation fails, the user will be shown the following error messages depending on exception raised:
![Missing Details](https://)

![Invalid Mobile Number](https://)

![Invalid Email](https://)

> Next, the user will be asked to provide number of bedrooms, bathrooms, etc:
![No. of Bedrooms](https://)

![No. of Bathrooms](https://)

![No. of Livingrooms](https://)

![Any other rooms](https://)

> The user will then be asked to enter any additional information:
![Additional Information](https://)

> The details provided will be displayed and the user will be asked to confirm accuracy:
![Confirm Details](https://)

> If the user selects the choice indicating the details are incorrect, they will be able to start over from the number of bedrooms question:
![Re-enter Property Details](https://)

> If the user selects the choice indicating the details are correct, they will be shown their estimate and asked if they want to get another estimate or exit the program:
![Estimate](https://)

<a name="left"></a>

### Features left to implement

> Functionality to prompt user to enter only the specific piecce of information which fails validation.


<a name="tech"></a>
# Technology Used
### Python
Used to create the application

### Heroku
Used to deploy and host the application

### Github
Used to store the code

### Gitpod
IDE used for creating the application

### Git
Used for version control

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
>  

### 
> 

<a name="deployment"></a>
## Deployment

####
Navigate to heroku.com & log in.

Click "new" and create a new App.

Give the application a name and then choose your region and Click "Create app".

On the next page click on the Settings tab to adjust the settings.

Click on the 'config vars' button.

Supply a KEY of PORT and it's value of 8000. Then click on the "add" button.

Buildpacks now need to be added. 

These install future dependancies that we need outside of the requirements file.

Select Python first and then node.js and click save. 

**Make sure they are in this order.**

Then go to the deploy section and choose your deployment method. 

To connect with github select github and confirm.

Search for your repository select it and click connect.

You can choose to either deploy using automatic deploys which means heroku will rebuild the app everytime you push your changes. 

For this option choose the branch to deploy and click enable automatic deploys. 

This can be changed at a later date to manual. 

Manual deployment deploys the current state of a branch.

Click deploy branch.

We can now click on the open App button above to view our application.

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

<a name="content"></a>
## Content and Resources

### w3 schools
> Used to reference Python Structure.

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
> My mentor in the CI who provided me with great feedback and guidance at the inception of this project.

### External Community
> 