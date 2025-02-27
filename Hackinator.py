database = [
    {"name": "Virat Kohli", "human": True, "male": True, "famous": True, "indian": True, "movie": False, "cricketer": True, "scientist": False, "politics": False},
    {"name": "AB De Villiers", "human": True, "male": True, "famous": True, "indian": False, "movie": False, "cricketer": True, "scientist": False, "politics": False},
    {"name": "Smriti Mandhana", "human": True, "male": False, "famous": True, "indian": True, "movie": False, "cricketer": True, "scientist": False, "politics": False},
    {"name": "Ellyse Perry", "human": True, "male": False, "famous": True, "indian": False, "movie": False, "cricketer": True, "scientist": False, "politics": False},
    {"name": "Narendra Modi", "human": True, "male": True, "famous": True, "indian": True, "movie": False, "cricketer": False, "scientist": False, "politics": True},
    {"name": "Droupadi Murmu", "human": True, "male": False, "famous": True, "indian": True, "movie": False, "cricketer": False, "scientist": False, "politics": True},
    {"name": "Donald Trump", "human": True, "male": True, "famous": True, "indian": False, "movie": False, "cricketer": False, "scientist": False, "politics": True},
    {"name": "Jacinda Ardern", "human": True, "male": False, "famous": True, "indian": False, "movie": False, "cricketer": False, "scientist": False, "politics": True},
    {"name": "Yash", "human": True, "male": True, "famous": True, "indian": True, "movie": True, "cricketer": False, "scientist": False, "politics": False},
    {"name": "Sridevi", "human": True, "male": False, "famous": True, "indian": True, "movie": True, "cricketer": False, "scientist": False, "politics": False},
    {"name": "Johnny Depp", "human": True, "male": True, "famous": True, "indian": False, "movie": True, "cricketer": False, "scientist": False, "politics": False},
    {"name": "Angelina Jolie", "human": True, "male": False, "famous": True, "indian": False, "movie": True, "cricketer": False, "scientist": False, "politics": False},
    {"name": "Sir C V Raman", "human": True, "male": True, "famous": True, "indian": True, "movie": False, "cricketer": False, "scientist": True, "politics": False},
    {"name": "B Vijayalakshmi", "human": True, "male": False, "famous": True, "indian": True, "movie": False, "cricketer": False, "scientist": True, "politics": False},
    {"name": "Nikola Tesla", "human": True, "male": True, "famous": True, "indian": False, "movie": False, "cricketer": False, "scientist": True, "politics": False},
    {"name": "Marie Curie", "human": True, "male": False, "famous": True, "indian": False, "movie": False, "cricketer": False, "scientist": True, "politics": False},
]


def get_valid_input(prompt):
    """Function to validate user input (only 'y' or 'n' allowed)"""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "n"):
            return answer == "y"  # Convert 'y' to True and 'n' to False
        print("Invalid input! Please enter 'y' or 'n'.")


def filter_database(property):
    """Filters the database based on user response and removes non-matching characters"""
    global database
    answer = get_valid_input(f"Is your character {property.replace('_', ' ')} (y/n)? ")
    database = [d for d in database if d[property] == answer]

    if len(database) == 1:
        print(f"Your character is {database[0]['name']}! 🎉")
        quit()
    elif len(database) == 0:
        print("No matching character found based on your answers! 😕")
        quit()


# Start the game
print("Welcome to Hackinator! Answer the following Yes/No questions:")

filter_database("human")
filter_database("male")
filter_database("famous")
filter_database("indian")
filter_database("movie")
filter_database("cricketer")
filter_database("scientist")
filter_database("politics")

# If multiple options remain, let the user know
if len(database) > 1:
    print("Hmm... I'm not sure. Here are the possible matches:")
    for character in database:
        print(f"- {character['name']}")
