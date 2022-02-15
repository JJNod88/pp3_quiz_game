# Where am I? Quiz

# Contents
* [Introduction](#Introduction)
* [Value](#Value)
* [UX](#UX)
* [Features](#Features)
* [Python-Coding](#Python_Coding)
* [Technologies](#Technologies)
* [Testing](#Testing)
* [Validation](#Validation)
* [Bugs](#Bugs)
* [Deployment](#Deployment)
* [Credits](#Credits)

# Introduction
* Using Python I will create a web-based Quiz that users can run
* The idea of the game will be for educational purposes, whilst providing some enjoyment for users to test their world knowledge 
* I will provide a set of questions with some possible answers. The users will choose which option they believe is the correct answer
* The user will receive a score at the end of the quiz, and have opportunity to provide feedback or new questions
* The quiz is linked to a google sheets so that the information from the quiz is stored and can be used in the future 

![Image-of-design](/assets/images/responsive.png)

# Value
### New User / Target Audience
* Users looking to test their travel and geographical knowledge 
* Users who enjoy testing their knowledge and experience in a quiz game
* Competitive people who like to achieve results and respond positively to results based quiz/games

### Return User
* Users who have previously played the game and would like to try again and score highly
* Who have a new idea for a question that can be added to the quiz
* Who want to provide valuable feedback

### Site Aims
* The Quiz aims to provide an interactive and intuitive quiz experience 
* It provides users:
    * A platform to play an interactive quiz game
    * Opportunity to create a username and be communicated to using the user name
    * Compete against themselves in trying to answer all the questions correctly
    * Opportunity to provide feedback about the quiz
    * Opportunity to recommend new questions to improve the difficulty of the game 

#### How the Site achieves this
* The site is designed to be interactive, intuitive and simple
* It provides clear instructions on how to play
* It is coded to prevent the user from inputting any errors, to ensure the quiz can be completed successfully and is free of bugs
* The code has appropriate spacing in-between the lines and also has colour coding for improved UX
* It has input for the user to interact with the Site
* It has an API linked to Google Sheets to capture the data from the user and allows the quiz owner to collate and utilise the feedback 
* There has been limited CSS and HTML in this quiz to ensure a smooth, effective command line quiz

# UX
### 1. Scope Plane
* My [Values](#Value) highlights the key user goals and how the site aims to achieve this
* I built a process flow on PowerPoint which you can view here []
    * This gave me the foundation of what my quiz was trying to do and the functions needed to achieve it

### 2. Scope Plane
* The Scope plane includes the features needed to provide content, material, access and functionality for Users
* I designed a basic process flow chart to look at how the quiz was going to work, and what functions i needed. There is of course more complexity behind this flow, however it was important to have a foundation to build from:

![Image-of-flow](/assets/images/process_flow.png)

* You can find a detailed list of the features [here](#Features) 
* Because of the project, the command line quiz involves very limited HTML and CSS, as there was a templated html structure already implemented that allowed Heroku to host the quiz
* The content of the quiz was relevant and had a context of 'Where am I?'.
    * Quiz questions were relatable, and their answers were deigned to be difficult for the User to answer
* the game begins with an introduction, provides the User a multitude of opportunities to play the game and also provide feedback for the game 

### 3. Structure Plane
* The project came with a template that allowed GitHub to interact with Heroku, for hosting the game
    * In this case, the html and css structure was not edited - instead, the quiz itself and the content was structured to ensure the correct flow of the game
* To ensure an appropriate structure, the content of the game was purposely ordered:
    * Begins with an introduction and captures the users name
        * This sends information to the google Sheets linked with the quiz
    * Interacts with the user and provides them with the opportunity to progress with the quiz or not
    * Quiz begins
    * Results are provided once all quiz questions have been answered
        * This sends information to the google Sheets linked with the quiz
    * At the point, the user is asked to provide feedback or new question opportunities
        * This sends information to the google Sheets linked with the quiz
    * The user is asked if they want to play again or end the game here

### 4. Skeleton Plane
* A process flow was designed to. Because I stuck with the original template, no additional HTML or CSS was being added, so it was easy to judge what the quiz would look like once on Heroku
    * You can review the WireFrames here [] 

### Navigation
* The quiz being structured appropriately assisted in the navigation of the quiz
* The quiz is navigated through automatically by following the steps provided
    * There are while loops to prevent the user inputting any errors, and reduces the opportunity for bugs in the code
    * There are opportunities for the user to choose when they start and end the quiz

### Functionality
* Six functions were developed to allow the quiz to be completed
    * In order for the site to be intuitive and be able to capture meaningful content, the first function provides both an introduction but also the ability for users to submit their username - This also begins the first meaningful data capture, as this is then sent to the Google Sheets API
        * A while / else loop was implemented to ensure the user had to input a string and not leave it blank
    * To increase the flow of the quiz, a begin function was created that gives the user the opportunity to progress with the quiz or not
        * A while / if / elif loop was created to ensure this function reacted depending on the users input
    * The main_quiz function was the fundamental function for the quiz to be a quiz. It iterated through the list (data model) and provided the scoring and feedback
        * Originally this was iterating through a dictionary however, for improved UX and difficult the dictionary needed to be randomised, which i then imported random and transformed the dictionary into a list to make this doable
        * The scoring incrementation was added to this function also
            * This was also linked to the Goggle Sheets to capture the score for the User
    * You will find the array of dictionary questions which I transformed into a list
    * The next function was the score function
        * This was the function that captured the displayed the score feedback to the user
            * I also linked the Google Sheets here and sent the score information direct to it
    * Following this, was the append recommend function whereby the quiz asks the user for feedback and it transferred directly to the Google Sheets
    * The final function is the restart function
        * This ensured that the game didn't just end abruptly for the user. It provided them with the opportunity to restart the game, or end it 

### 5. Surface Plane
* This plane sets out to the main goals, styling and format

### User Friendly
* The purpose of this quiz is to provide an intuitive, simple, interactive and meaningful experience for both the user and the owner
    * The quiz is complication free for the User
    * They quiz is designed and structured so that the user is taken to through the correct flow of the quiz
    * It has clear instructions
    * It is coded in a way that the user has input and opportunity to play the game at their leisure. It is bug free and has been designed to be simple and effective
    * An import for color has been implemented to improved UX when a user is provided with a result to their answer

### Font color and styling
* '\n' has been used appropriately to ensure the code in the quiz has the right amount of separation so that is clear and easy to read
* Color has been added to the results and feedback content so that is easily readable and separates it from the main wording

# Features
Below is a list of my features and functions that outline what the quiz does and is capable of:
* I am using Heroku to provide the cloud platform to allow users to run the programme
* This allows user input and interactivity and introduces the game
* The quiz asks for the users name, and uses this to interact with the User

![Image-of-heroku_start](/assets/images/start.png)

* From this, the quiz and its instructions is introduced to the user, using their user_name

![Image-of-instructions](/assets/images/intro_yn.png)

* There is a function that asks the User if they are ready to play
    * If they click 'y' or 'Y' it progresses to the game
    * If they click 'n' or 'N' it asks them to press 'y' when ready
    * If they click any other button, it reverts back to the beginning
    * You can find the invalid data handling images [here](#Python_Coding)

* y
![Image-of-ystart](/assets/images/y_start.png)

* n
![Image-of-nstart](/assets/images/n_start.png)

* no then yes

![Image-of-nystart](/assets/images/no_yes_start.png)

* There are multiple choice questions, each with 4 choices
    * 1 answer is correct, 3 are incorrect
    * The programme provides feedback to the user on whether they were correct or not
    * The questions are randomised with no duplicated questions

![Image-of-correcta](/assets/images/correct_answer.png)

![Image-of-incorrecta](/assets/images/incorrect_answer.png)

* Each correct answer increments that collates the score
    * Provides a score at the end of the quiz

![Image-of-score](/assets/images/complete_score.png)

* The user has the opportunity to provide feedback to the site / quiz owner, which send to a Google Sheets
    * You can find what this appends to the google sheets in the [Google_Sheets_section](#Python_Coding)

![Image-of-feedback](/assets/images/complete_score.png)

* The user will have the opportunity to play again or end the game 

![Image-of-restart](/assets/images/restart_yn.png)

* yes

![Image-of-yrestart](/assets/images/yes_restart.png)

* no

![Image-of-nrestart](/assets/images/no_restart.png)

### API to Google Sheets
* The quiz is linked with a google sheets for data capture called pp3_project
* The username at the beginning and feedback later on is captured and appended in a worksheet called userFeedback
* When the quiz is completed and a score provided, this score is then updated adjacent to the users username in the userScore worksheet

* This is the code that directly links to the sheet and worksheet

![Image-of-gssheet](/assets/images/google_sheets_link.png)

* This is the score worksheet being appended automatically from the quiz:

![Image-of-gsscore](/assets/images/google_sheets_score.png)

* The user is asked to provide feedback or updates on the quiz. This updated the user feedback worksheet, adjacent to the username:

![Image-of-gsfeedback](/assets/images/google_sheets_feedback.png)

* The purpose of all of this is for quiz / site improvements, and improved UX and UI

### Future Features
* I would like to provide a user with their highest score. I would need to ensure that when the username is matched, it overwrites the score providing the integer is larger (in google sheets) which is then printed back to the user

# Python Coding
## Data Models
### Dictionary
* A Dictionary was used to store and provide the questions and answers to the quiz
* The dictionary was then converted into a list for additional functionality. Importing random gave the opportunity to then randomise the dictionary questions for improved UX

#### Google Sheets API
* A Google Sheets was incorporated into the quiz to allow the quiz to capture key data that can be:
    * Later used to improve the quiz
    * Utilised to provide additional functionality to the users. For example, with the Google Sheets, a user high score can be capturted and then sent back to the quiz to relate to the user
    * I also added this function to test my skills and learn how a real world application can be used
    * Images of this are in the Features section

### Invalid Data Handling
* To ensure a positive user experience and for the quiz to work effectively and provide valid date to the google sheets, there was data handling implemented to avoid this
* Within a while loop, to avoid the user inputting zero string, i used "" and " " to ensure the user had to input some form of string

![Image-of-invalid_user](/assets/images/invalid_name.png)

* .lower() was used so that in user answers a capital or non capital letter was accepted

![Image-of-capital](/assets/images/capital_accepted.png)

* 'not in' was used to ensure the answers from the user matched with the correct answers in the quiz. If an error was picked up, it would not accept the answer and would request a new input from the user

* If any other answer other than 'y' or 'n' for my loops was inputted, it would provide an error

![Image-of-invalidyn](/assets/images/invalid_yn.png)

* If another character other than a, b, c, or d it provides an error

![Image-of-invalid-answer](/assets/images/invalid_answer.png)

### Imports
* For the quiz, three imports were implemented:
    * Random - This allowed the array of dictionaries to be converted into a list and randomised
    * Colorama - This gave the ability to colour the text in the quiz for improved UX
    * Gspread - Provided the opportunity for data collection via the google api

# Technologies
* For the quiz I have coded in Python.
* Because the project needed to be deployed onto Heroku, I used a templated ReadMe that had built in code that enabled this.

# Testing
### Manual Testing and Expectations
* The quiz went through thorough testing to ensure a great experience for the User. 
* You can find images of the below in effect in the [Features-Section](#Features)
* Name is inputted and reflected in the print
    * If username input field is left blank, it asks the user to re-enter before progressing
    * It appends correctly in to the Google Sheets API
        * Logs a new user_name
* Begin() function is then asked
    * If 'y' or 'Y', progresses as expected
    * If 'n' or 'N', returns as expected
    * If any other button, returns as expected 
* All questions are asked, randomised, and not duplicated
    * If answer doesn't match a, b, c, d it does not let the user progress. It repeats the questions
    * Capital letters of a, b, c and d are all accepted
* The correct answer correctly increment the score
    * It also has the right message
    * It has the font color green
* The incorrect answer correctly does not increment the score
    * It also has the right message
    * It has the font color red
* Once the quiz questions are complete, the user is provided with their score
    * It has the font color of Yellow
* The user is then asked to provide feedback
    * The information is appended to the google sheets in the appropriate column and beside the user_name
* User is asked if they want to play a game
    * If 'y' or 'Y', progresses as expected
    * If 'n' or 'N', returns as expected
    * If any other button, returns as expected 

# Validation
### Pep8
* The code was run through PeP8 to ensure it was written well with no bugs
* It passed with zero bugs or notifications

![Image-of-pep8](/assets/images/pep8.png)

### Lighthouse
* To ensure the quiz was running efficiently, I ran it through Google Developers Lighthouse Function
* It scored well in performance and accessibility

![Image-of-lighthouse](/assets/images/lighthouse.png)

# Bugs
* The first bullet point is the bug. The indented second bullet point = fix:
* I cant use my variable elsewhere
    * Fix - I added global to the variable name in my intro function
* Trying to iterate through my list - says it list object is not callable
    * I had '()' in my quiz_questions, it's not a function. Just removed brackets
* Trying to iterate through my list - removed (), it now says not enough values to unpack
    * I hadn't added the .items() function, which is used to return the keys and values - it also ran for ever as I hadn't closed the while loop
* Added a main_quiz function to provide the multiple choice. When i run, nothing is happening other than the hello function 
    * I didn't add the quiz_questions into the parameter
    * Also - i was using != and == to check for my answers which was causing a problem. I used 'not in' which worked
* My quiz is now running - however, it is not picking up the correct answers. any letter gives a try again
    * I need to add the final if/else to check if the answer was correct
    * i was also missing the 'i' for my iteration
* If i put a capital letter in, it didn't accept the result
    * I added .lower on the user input 
* Have added a score variable that increments when a correct score is answered. Says undefined in the f statement in my result function
    * I was calling the function outside of the main quiz function. I called it with the for statement and it worked
* Imported google sheets for user feedback however error because the sheet is undefined
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
* Restart function stops running after one restart
    * I had return true in the IF statement. Removing this fixed the problem

* There are no remaining Bugs 

### GitPod reccomendation
* In my hello() function, in my while loop, GitPod recommends using break:

![Image-of-break_message](/assets/images/break_message.png)

* When I add the break, I get the following:

![Image-of-break_error](/assets/images/break_error.png)

* Because my Quiz works without the break, I left it blank after searching the web and speaking to my Mentor

# Deployment
* As best practice, deployment was completed at the very beginning to allow testing during the development process
* Please see below instructions on how the project was deployed via Heroku from my GitPod. 

1. Create a GitHub repository
2. Remove any un-used imports from the run.py file
3. In order for input methods to work properly in the deployed mock terminal, add a new line character at the end of the text, inside the input method.
4. when creating a new list of requirements, you type in the terminal:  pip3 freeze > requirements.txt
5. Go to the Heroku website
6. In your Heroku account, click ‘Create New App’ on the Dashboard
7. Select your region (Europe) and give your project a unique name
8. Click ‘Create App’ to create your app
9. Find the setting tab to access and set up 'Config Vars'(this is required if using a creds.json file).
10. Click ‘Add Buildpack’ and select Python - ‘Save Changes’.
11. you will need to select ‘NodeJS’ and save
12. Please note, Buildpacks must be in order, so for this project Python needs to be first, NodeJS second
13. Locate the 'Deploy' tab 
14. Select ‘GitHub' as the deployment method to link to your GitHub repository
15. Search for the required repository and then connect it
16. Click ‘Enable Automatic Deploys’
17. In the 'Manual Deploy Section' select 'main' branch and then select ‘Deploy Branch’ to deploy
18. Now this is deployed you can view your project by clicking ‘view’

# Credits 
* Mentor, dickV_mentor 
    * Spotted that in my append function, i was not providing the google sheets with an array, so I added brackets, and my function worked correctly
    * Highlighted In my restart function that I had a print in the wrong place and to remove 'Return True' in my IF statement so that the game could continue to run
* Love Sandwiches provided material in order for me to set up the quiz
    * The insight into setting up the google sheets was helpful
* Course Material for the correct coding
* Tutor, Ger - Worked with me on converting my Dictionary to a list for randomising. Whilst I solved the code, the tutor gave me the confidence I needed that I was on the right track

### Media & Resources
* [patorjk](http://patorjk.com/) for the ASCII Art and how to implement
* [Am-I-Responsive](http://ami.responsivedesign.is/#) for the introduction image
* [pypi](https://pypi.org/project/colorama/) for my colorama import 
* [Geeks-for-geeks](https://www.geeksforgeeks.org/python-dictionary/) for help with the dictionary