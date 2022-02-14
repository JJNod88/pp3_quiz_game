import gspread
from google.oauth2.service_account import Credentials
import random
import colorama
from colorama import Fore
colorama.init(autoreset=True)


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
    print(
        """
 _    _ _                                       _____ ___    _____       _
| |  | | |                                     |_   _|__ \  |  _  |     (_)
| |  | | |__   ___ _ __ ___    __ _ _ __ ___     | |    ) | | | | |_   _ _ ____
| |/\| | '_ \ / _ \ '__/ _ \  / _` | '_ ` _ \    | |   / /  | | | | | | | |_  /
\  /\  / | | |  __/ | |  __/ | (_| | | | | | |  _| |_ |_|   \ \/' / |_| | |/ /
 \/  \/|_| |_|\___|_|  \___|  \__,_|_| |_| |_|  \___/ (_)    \_/\_\\__,_|_/___|

        """)

    print("Welcome to the 'WHERE AM I?' Quiz\n")
    global user_name
    user_name = input("Please enter your username: ")
    print('\n')

    # If the user name leaves this blank, it prompts them to enter
    while user_name == "" or user_name == " ":
        print('Oops, please enter your name')
        user_name = input("Hey, please enter your name:")
    else:
        print(f"Hey {user_name}, Let's test your knowledge of the world!")
        print('We have a range of questions for you to answer.\n')
        print("All you have to do is select 'a', 'b', 'c', or 'd'.")
        print('You got this. Good Luck.\n')


def begin():
    """
    Give the user the option to start the game or not
    """
    print(f'{Fore.BLUE}So {user_name}, are you ready to play?\n')
    start = True
    while start:
        start_game = input('Please type "y" or "n"\n').lower()

        if start_game == 'y':
            print("Great, let's begin\n")
            break
        elif start_game == 'n':
            print('No problem, in your own time')
        else:
            print('Oops, please choose "y" or "n"\n')


def main_quiz(list):
    """
    Main function of the game - this iterates through my quiz questions
    First statement provides the questions and the list to choose from.
    The input allows both lower and upper case choices.
    It then provides feedback on whether the user was correct or not.
    It incriments the score depending on the users answer.
    """
    score_incriment = 0
    # code to randomise my quiz_questions / add both solutions in ReadMe
    for i in list:

        answer = ''

        while answer not in ['a', 'b', 'c', 'd']:
            print(i['question'])
            for key, value in i['choices'].items():
                print(f'{key} : {value}')

            answer = input('Please pick your answer\n').lower()

            if answer not in i['choices']:
                print(Fore.RED + 'Sorry, only the letters a, b, c, d\
 are accepted. Try again.\n')

        if answer == i['correct_choice']:
            print(f'{Fore.GREEN}Correct! Well done.\n')
            score_incriment += 1
        else:
            print(f'{Fore.RED}Oh no, that was incorrect.\n')

    result(score_incriment)


# Dictionary of questions the game will be asking.
# Questions and Choices have been used in my main quiz to iterate through them
# This dictionary has been converted into a list for randomising
quiz_questions = [
    {"question": "I'm on top of the tallest built structure in the world.\
 Where am I?:",
        "choices":
            {"a": "Japan",
                "b": "Hong Kong",
                "c": "Dubai",
                "d": "Abu Dhabi"},
        "correct_choice": "c"},
    {"question": "A group of Pyramids beginning with the letter 'G'. Which\
 Country are they in?:",
        "choices":
            {"a": "Mexico",
                "b": "Cairo",
                "c": "Turkey",
                "d": "Egypt"},
        "correct_choice": "d"},
    {"question": "I am on the set of Game of Thrones. Which country\
 am I in?: ",
        "choices":
            {"a": "New Zealand",
                "b": "Ireland",
                "c": "Scotland",
                "d": "Denmark"},
        "correct_choice": "b"},
    {"question": "I am north of Italy, South of Sweden. My Capital City begins\
 with a B. What City am I in?:",
        "choices":
            {"a": "Poland",
                "b": "Germany",
                "c": "Bulgaria",
                "d": "France"},
        "correct_choice": "b"},
    {"question": "I am in the USA. My state is famously known for my Canyon.\
 What City am I in?:",
        "choices":
            {"a": "Arizona",
                "b": "Texas",
                "c": "California",
                "d": "Florida"},
        "correct_choice": "a"},
    {"question": "'Fondue' is famously recognised for which Country?:",
        "choices":
            {"a": "Belgium",
                "b": "France",
                "c": "Switzerland",
                "d": "Sweden"},
        "correct_choice": "c"},
    {"question": "If I was sailing between the UK and USA,\
 what Sea would I be in?:",
        "choices":
            {"a": "Atlantic.",
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
    This provides the user with their score following the quiz.
    It also sends the username and their score to Google sheets
    which will be used for future functionality.
    """
    print(Fore.YELLOW + f'Well done! You completed the quiz with a score of\
 {score_incriment} out of 7!')
    userscore_name = (f'{user_name}')
    userscore_score = (f'{score_incriment}')
    update_worksheet_two = SHEET.worksheet('userScore')
    update_worksheet_two.append_row([userscore_name, userscore_score])


def append_recommend(user_feedback):
    """
    At the end of the quiz, the user is prompted to recommend a
    question or provide feedback.
    This feeds back into the pp3 google sheets for data capture
    """
    print('Hey, please leave a question recommendation or feedback here.\n')
    user_input_feedback = input('Please enter here:\n')
    update_worksheet = SHEET.worksheet('userFeedback')
    update_worksheet.append_row([user_name, user_input_feedback])


# function to restart game, play again
def restart():
    """
    Gives the user the option to restart the game or not
    """

    restart = True
    while restart:
        print(f'{user_name}, would you like to play again?\n')
        restart_game = input('Please type "y" or "n"\n').lower()
        if restart_game == 'y':
            begin()
            main_quiz(quiz_questions)
            append_recommend('UserFeedback')
            print('Hope you enjoyed the game')
        elif restart_game == 'n':
            print('No problem, thanks for playing.')
            return False
        else:
            print('Oops, please choose "y" or "n"\n')


hello()
begin()
main_quiz(quiz_questions)
append_recommend('UserFeedback')
restart()
