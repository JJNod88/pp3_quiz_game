# Quiz Game - Where Am I
* Using Python I will create a web-based Quiz that users can run
* The idea of the game will be for educational purposes, whilst providing some enjoyment  
* I will provide a set of questions with some possible answers. The users will choose which option they believe is the correct answer.


# Functions
* I am using heroku to provide the cloud platform to allow users to run the programme
    * This allows user input and interactivity
* The quiz asks for the users name, and uses this to interact with the User
* There are multiple choice questions, each with 4 choices
    * 3. Could store the dictionary in Google Sheets and add the new code in the questions (idea)
    * 1 answer is correct, 3 are incorrect
    * The programme provides feedback to the user on whether they were correct or not

* 1. Randomise questions and make it so only one answer can be asked per round (idea)

* There is a score incrimentor that collates the score, and provides feedback to the User

    * 2. Keep track of score per user (idea)
    * new work sheet 
    * google sheets finds the username
    * updates worksheet

* TBC - The user is then prompted to recommend a new question or provide feedback
    * this will then API through to a google sheets for quiz improvements 
* The user will have the opportunity to play again or end the game 


# Bugs
* I cant use my variable elsewhere
    * Fix - I added global to the variable name in my intro function
* Trying to iterate through my list - says it list object is not callable
    * I had '()' in my quiz_questions, its not a function. Just removed brackets
* Trying to iterate through my list - removed (), it now says not enough values to unpack
    * I hadnt added the .items() function, which is used to return the keys and values - it also ran for ever as I hadnt closed the while loop
* Added a main_quiz function to provide the mulptiple choice. When i run, nothing is happening other than the hello function. 
    * I didnt add the quiz_questions into the paramenet
    * Also - i was using != and == to check for my answers which was causing a problem. I used 'not in' which worked
* My quiz is now running - however, it is not picking up the correct answers. any ketter gives a try again
    * I need to add the final if/else to check if the answer was correct
    * i was also missing the 'i' for my iteration. 
* If i put a capital letter in, it didnt accept the result
    * I added .lower on the user input 
* Have added a score variable that incriments when a correct score is answered. Says undefined in the f statement in my result function.
    * I was calling the function outside of the main quiz function. I called it with the for statement and it worked
* Imported google sheets for user feedback however error because the sheet is underfined
    * I hadn't linked the worksheet, i had duplicated the name of the actual Google Sheets
* In my append function - Input is working fine, however the append is not working, no attribute 'append'
    *   In my function, my code to append the user input was correct, however i was not providing the input information as an array. So, i added brackets to create an array and it worked:
    update_worksheet.append_row( *[* user_input_feedback *]* )



# Credits 
* Mentor, dickV_mentor - Spotted that in my append function, i was not providing the google sheets with an array, so i added brackets, and my function worked correctly. 



