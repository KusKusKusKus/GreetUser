import json

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("What is your name: ")
    filename = 'username.json'
    with open(filename, 'w+') as f:
        json.dump(username, f)
    return username

def check_username():
    username = get_stored_username()
    answer = input(f"Your name: {username}?"
                   "\nYes or No\n")
    allowed_answers = ['yes', 'no']
    while answer.casefold() not in allowed_answers:
        answer = input("Please write Yes or No\n")
    if answer.title().casefold() == 'yes'.casefold():
        return username
    elif answer.title().casefold() == 'no'.casefold():
        return get_new_username()


def greet_user():
    username = check_username()
    if username:
        print(f"Your name: {username}")
    else:
        print(f"We'll remember you name: {username}")

greet_user()