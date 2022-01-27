def main_quiz():
    """
    This is where my Quiz will start.
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
        print('You got thios. Good Luck)')




def answers():
    """
    I will include my answers here and link to my main game
    """
    pass


# dictionary of questions the game will be asking,

quiz_questions = [
    {"Question": "Location of the tallest human built structure in the world.\nWhere am I?: ",
    "Answers": {"a": "Japan",
                "b": "Hong Kong",
                "c": "Dubai",
                "d": "Abu Dhabi"},
    "correct Answer": "c"},
    {"Question": "A group of Pyramids beginning with the letter 'G'.\nWhich Country are they in?: ",
    "Answers": {"a": "Mexico",
                "b": "placeholder",
                "c": "placeholder",
                "d": "Egypt"},
    "correct Answer": "d"},
    {"Question": "I am on the set of Game of Thrones. Which country am I in?: ",
    "Answers": {"a": "New Zealand",
                "b": "Ireland",
                "c": "Scotland",
                "d": "Denmark"},
    "correct Answer": "b"},
    {"Question": "I am north of Italy, South of Sweden. My Capital City begins with a B.\nWhat City am i in?: ",
    "Answers": {"a": "Poland",
                "b": "Germany",
                "c": "Bulgaria",
                "d": "France"},
    "correct Answer": "b"},
    {"Question": "I am in the USA. My state is famously known for my Canyon.\nWhat City am I in?: ",
    "Answers": {"a": "Arizona",
                "b": "Texas",
                "c": "California",
                "d": "Florida"},
    "correct Answer": "a"},
    {"Question": "'Fondue' is famously recognised for which Country?: '",
    "Answers": {"a": "Belgium",
                "b": "France",
                "c": "Switzerland",
                "d": "Sweden"},
    "correct Answer": "c"},
    {"Question": "If I was sailing between the UK and USA, what Sea am i in?: ",
    "Answers": {"a": "Atlantic.",
                "b": "Pacific.",
                "c": "Indian.",
                "d": "Arctic."},
    "correct Answer": "a"},
]