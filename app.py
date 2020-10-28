from flask import Flask
from random import randint
app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal too!'

@app.route('/dessert/<users_dessert>')
def favorite_deserts(users_dessert):
    return f'How did you know I liked {users_dessert}'

@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun):
    return f'The {adjective} {noun} ate my mother!'

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    test1 = number1.isdigit()
    test2 = number2.isdigit()
    if (test1 == True) and (test2 == True):
        total = int(number1) * int(number2)
        return f'{number1} times {number2} is {total}.'
    else: 
        return f'Invalid inputs, please try again by entering 2 numbers!'

@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    new_string = (word + " ")
    string_multiplied = new_string * int(n)
    return string_multiplied

@app.route('/strangecaps/<strange_word>')

@app.route('/reverse/<reverse_word>')
def reverse(reverse_word):
    return reverse_word[::-1]


@app.route('/dicegame')
def roll_dice():
    luck = randint(1,7)
    if luck < 6:
        return f'You rolled a {luck}. You lost!'
    else:
        return f'You rolled a {luck}. You Won!'

if __name__ == '__main__':
    app.run(debug=True)
