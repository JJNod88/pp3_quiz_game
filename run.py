import gspread
from google.oauth2.service_account import Credentials 
import random

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('pp3_project')

user_feedback = SHEET.worksheet('userFeedback')
user_scoring = SHEET.worksheet('userScore')

def hello():
    """
    This is where my Quiz will start.
    Collects users name with an input.
    While loop ensures they type a word in.
    """
    global user_name 
    user_name = input("Hey, please enter your username: ")
    print('\n')

    # If the user name leaves this blank, it prompts them to enter
    while user_name == "" or user_name == " ":
        print('Oops, please enter your name')
        user_name = input("Hey, please enter your name:")
    else: 
        print(f'Hey {user_name}, Lets test your knowledge of the world!')
        print('We have a range of questions for you to asnwer.')
        print("All you have to do is select 'a', 'b', 'c', or 'd'.")
        print('You got this. Good Luck.\n')


def main_quiz(list):
    """
    Main function of the game - this iterates through my quiz questions
    First statement provides the questions and the list to choose from.
    The input allows both lower and upper case choices.
    It then provides feedback on whether the user was correct or not.
    I will add scoring calculator and feedback. 
    """
    score_incriment = 0
    for i in list:
        answer = ''

        while answer not in ['a', 'b', 'c', 'd']:
            print(i['question'])
            for key, value in i['choices'].items():
                print(f' {key} : {value}')

            answer = input('Please pick your answer\n').lower()

            if answer not in i['choices']:
                print('Sorry, only the letters a, b, c, d are accepted. Try again.\n')

        if answer == i['correct_choice']:
            print('Correct! Well done.\n')
            score_incriment += 1
        else:
            print('Oh no, that was incorrect.\n')

    result(score_incriment)


# Dictionary of questions the game will be asking
quiz_questions = [
    {"question": "Location of the tallest human built structure in the world.\nWhere am I?: ",
    "choices": {"a": "Japan",
                "b": "Hong Kong",
                "c": "Dubai",
                "d": "Abu Dhabi"},
                "correct_choice": "c"},
    {"question": "A group of Pyramids beginning with the letter 'G'.\nWhich Country are they in?: ",
    "choices": {"a": "Mexico",
                "b": "placeholder",
                "c": "placeholder",
                "d": "Egypt"},
                "correct_choice": "d"},
    {"question": "I am on the set of Game of Thrones. Which country am I in?: ",
    "choices": {"a": "New Zealand",
                "b": "Ireland",
                "c": "Scotland",
                "d": "Denmark"},
                "correct_choice": "b"},
    {"question": "I am north of Italy, South of Sweden. My Capital City begins with a B.\nWhat City am I in?: ",
    "choices": {"a": "Poland",
                "b": "Germany",
                "c": "Bulgaria",
                "d": "France"},
                "correct_choice": "b"},
    {"question": "I am in the USA. My state is famously known for my Canyon.\nWhat City am I in?: ",
    "choices": {"a": "Arizona",
                "b": "Texas",
                "c": "California",
                "d": "Florida"},
                "correct_choice": "a"},
    {"question": "'Fondue' is famously recognised for which Country?: '",
    "choices": {"a": "Belgium",
                "b": "France",
                "c": "Switzerland",
                "d": "Sweden"},
                "correct_choice": "c"},
    {"question": "If I was sailing between the UK and USA, what Sea am I in?: ",
    "choices": {"a": "Atlantic.",
                "b": "Pacific.",
                "c": "Indian.",
                "d": "Arctic."},
                "correct_choice": "a"},
]


# randomising quiz questions
list = quiz_questions
random.shuffle(list)


def result(score_incriment):
    """
    This will print a thank you, and i will add the score here once i have done
    the coding for it.
    """
    print(f'Well done! You completed the quiz with a score of {score_incriment}!')
    
    userscore_name = (f'{user_name}')
    userscore_score = (f'{score_incriment}')
    update_worksheetTwo = SHEET.worksheet('userScore')
    update_worksheetTwo.append_row([userscore_name, userscore_score])


def append_recommend(user_feedback):
    """
    At the end of the quiz, I will give the user an opportunity to recommend a 
    question or provide feedback.
    It will send the information to a google sheets so i can add these later
    """
    print('Hey, please leave a question recommendation or feedback here.\n')
    user_input_feedback = input('Please enter here.\n') 
    update_worksheet = SHEET.worksheet('userFeedback')
    update_worksheet.append_row([user_input_feedback])


hello()
main_quiz(quiz_questions)
append_recommend('UserFeedback')