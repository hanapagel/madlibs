"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    """Play a game with the user."""

    game = request.args.get("game")

    if game == "True":
        return render_template("game.html")
    elif game == "False":
        return render_template("goodbye.html")

# TODO: Does a checkbox return a boolean? A string? What's the default
# value of radio buttons and checkboxes?


@app.route('/madlib')
def show_madlib():
    """Display the final MadLib."""

    person = request.args.get('person')
    color = request.args.get('color')
    noun = request.args.get('noun')
    adjective = request.args.get('adjective')

    return render_template("madlib.html", person=person, color=color,
                           noun=noun, adjective=adjective)

# TODO: How to pass {{name}} variable from hello page to greet and madlib?


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
