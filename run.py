def hello():
    """
    This is where my Quiz will start.
    Collects users name with an input.
    While loop ensures they type a word in.
    """
    global user_name 
    user_name = input("Hey, please enter your name:")

    while user_name == "" or user_name == " ":
        print('Oops, please enter your name')
        user_name = input("Hey, please enter your name:")
    else: 
        print(f'Hey {user_name}, Lets test your knowledge of the world')
        print('We have a range of questions for you to go at')
        print("All you have to do is select 'a', 'b', 'c', or 'd'")
        print('You got this. Good Luck')


def main_quiz(quiz_questions):
    """
    Main function of the game - this iterates through my quiz questions
    """
    for i in quiz_questions:
        answer = ''
        while answer not in ['a', 'b', 'c', 'd']:
            for key, value in i['choices'].items():
                print(f' {key} : {value}')

            answer = input('Please pick your answer\n').lower()

            if answer not in i['choices']:
                print('Sorry, only the letters a, b, c, d are accepted\n')

        if answer == i['correct_choice']:
            print('Correct! Well done.\n')

        else:
            print('Oh no, that was incorrect.\n')
            
# dictionary of questions the game will be asking

quiz_questions = [
    {"Question": "Location of the tallest human built structure in the world.\nWhere am I?: ",
    "choices": {"a": "Japan",
                "b": "Hong Kong",
                "c": "Dubai",
                "d": "Abu Dhabi"},
    "correct_choice": "c"},
    {"Question": "A group of Pyramids beginning with the letter 'G'.\nWhich Country are they in?: ",
    "choices": {"a": "Mexico",
                "b": "placeholder",
                "c": "placeholder",
                "d": "Egypt"},
    "correct_choice": "d"},
    {"Question": "I am on the set of Game of Thrones. Which country am I in?: ",
    "choices": {"a": "New Zealand",
                "b": "Ireland",
                "c": "Scotland",
                "d": "Denmark"},
    "correct_choice": "b"},
    {"Question": "I am north of Italy, South of Sweden. My Capital City begins with a B.\nWhat City am i in?: ",
    "choices": {"a": "Poland",
                "b": "Germany",
                "c": "Bulgaria",
                "d": "France"},
    "correct_choice": "b"},
    {"Question": "I am in the USA. My state is famously known for my Canyon.\nWhat City am I in?: ",
    "choices": {"a": "Arizona",
                "b": "Texas",
                "c": "California",
                "d": "Florida"},
    "correct_choice": "a"},
    {"Question": "'Fondue' is famously recognised for which Country?: '",
    "choices": {"a": "Belgium",
                "b": "France",
                "c": "Switzerland",
                "d": "Sweden"},
    "correct_choice": "c"},
    {"Question": "If I was sailing between the UK and USA, what Sea am i in?: ",
    "choices": {"a": "Atlantic.",
                "b": "Pacific.",
                "c": "Indian.",
                "d": "Arctic."},
    "correct_choice": "a"},
]




def append_reccomend():
    """
    At the end of the quiz, i will give the user an opportunity to recommend a question or provide feedback
    """


hello()
main_quiz(quiz_questions)