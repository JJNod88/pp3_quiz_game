

Welcome JJNod88,


# Quiz Game - Where Am I
* Using Python I will create a web-based Quiz that users can run
* The idea of the game will be for educational purposes, whilst providing some enjoyment  
* I will provide a set of questions with some possible answers. The users will choose which option they believe is the correct answer.
* 








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

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!