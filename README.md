# Where am I? Quiz

# Contents
* [Introduction](#Introduction)
* [Value](#Value)
* [UX](#UX)
* [Accessibility](#Accessibility)
* [Responsiveness](#Responsiveness)
* [Features](#Features)
* [Technologies](#Technologies)
* [Validation](#Validation)
* [Testing](#Testing)
* [Deployment](#Deployment)
* [Credits](#Credits)

# Introduction
* Using Python I will create a web-based Quiz that users can run
* The idea of the game will be for educational purposes, whilst providing some enjoyment  
* I will provide a set of questions with some possible answers. The users will choose which option they believe is the correct answer.

# Value / UX
### New User / Target Audience
### Return User
### Site Aims
#### How the Site achieves this


# Accessibility

# Responsiveness

# Features
Below is a list of my features and functions that outline what the quiz does and is capable of:
* I am using heroku to provide the cloud platform to allow users to run the programme
    * This allows user input and interactivity
* The quiz asks for the users name, and uses this to interact with the User
* There is a function that asks the User if they are ready to play
    * If they click 'y' or 'Y' it progresses to the game
    * If they click 'n' or 'N' it asks them to press 'y' when ready
    * If they click any other button, it reverts back to the beginning
* There are multiple choice questions, each with 4 choices
    * 1 answer is correct, 3 are incorrect
    * The programme provides feedback to the user on whether they were correct or not
    * The questions are randomised with no duplicated questions
* There is a score incrimentor that collates the score
    * Provides a score at the end of the quiz
* The user has the opportunity to provide feedback to the site / quiz owner
* The user will have the opportunity to play again or end the game 

### API to Google Sheets
* The quiz is linked with a google sheets for data capture
    * The username at the beginning is captured and stored in a worksheet called userFeedback & userScore
    * When the quiz is completed and a score provided, this score is then updated adjacent to the users username in the userScore worksheet
    * The user is asked to provide feedback or updates on the quiz. This updated the userfeedback worksheet, adjacent to the username
* The purpose of all of this is for quiz / site improvements, and improved UX and UI

### Future Features
* I would like to provide a user with their highest score. I would need to ensure that when the username is matched, it overwrites the score providing the integer is larger (in google sheets) which is then printed back to the user. 

# Technologies


# Validation

# Testing
* Name is inputted and reflected in the print
* If username input field is left blank, it asks the user to re-enter before progressing
* begin() function
    * If 'y' or 'Y', progresses as expected
    * If 'n' or 'N', returns as expected
    * If any other button, returns as expected 
* All questions are asked, randomised, and not duplicated
    * If answer doesnt match a, b, c, d it does not let the user progress. It repeats the questions
* The correct answer correctly incriment the score
    * It also has the right message
* the incorrect answer correctly does not incriment the score
    * It also has the right message

## Bugs and Fixes
* I cant use my variable elsewhere
    * Fix - I added global to the variable name in my intro function
* Trying to iterate through my list - says it list object is not callable
    * I had '()' in my quiz_questions, its not a function. Just removed brackets
* Trying to iterate through my list - removed (), it now says not enough values to unpack
    * I hadnt added the .items() function, which is used to return the keys and values - it also ran for ever as I hadnt closed the while loop
* Added a main_quiz function to provide the mulptiple choice. When i run, nothing is happening other than the hello function 
    * I didnt add the quiz_questions into the paramenet
    * Also - i was using != and == to check for my answers which was causing a problem. I used 'not in' which worked
* My quiz is now running - however, it is not picking up the correct answers. any ketter gives a try again
    * I need to add the final if/else to check if the answer was correct
    * i was also missing the 'i' for my iteration
* If i put a capital letter in, it didnt accept the result
    * I added .lower on the user input 
* Have added a score variable that incriments when a correct score is answered. Says undefined in the f statement in my result function
    * I was calling the function outside of the main quiz function. I called it with the for statement and it worked
* Imported google sheets for user feedback however error because the sheet is underfined
    * I hadn't linked the worksheet, i had duplicated the name of the actual Google Sheets
* In my append function - Input is working fine, however the append is not working, no attribute 'append'
    *   In my function, my code to append the user input was correct, however i was not providing the input information as an array. So, i added brackets to create an array and it worked:
    update_worksheet.append_row( *[* user_input_feedback *]* )
* Appending my score to the new worksheet userScore. I am getting the bug to say invalid values
    * I changed to an f statement and captured the data from the global user_name which gets input at beginning
* Trying to append two bits of information in two columns, at the moment, my score is being appending in the row below the name, i want them side by side
    * I was putting brackets round both variables, i removed the duplication and put them in the same array
* I have imported Colorama to add some color and improve UX. When adding the color, it changes the entire next question to the same color i am changing the print too
    * I needed to add init(autoreset=True)


# Deployment

# Credits 
* Mentor, dickV_mentor - Spotted that in my append function, i was not providing the google sheets with an array, so I added brackets, and my function worked correctly
* Course Material - linking my worksheet with GoogleSheets 
* Tutor, Ger - Worked with me on converting my Dictionary to a list for randomising. Whilst i solved the code, the tutor gave me the confidence I needed that I was on the right track
* pypi for colorama import https://pypi.org/project/colorama/