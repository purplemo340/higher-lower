from flask import Flask
import random
ans=7
app = Flask(__name__)
def make_bold(function):
    def bold():
        output=function()
        output=(f"<b>{output}</b>")
        return output
    return bold
def make_em(function):
    def em():
        output=function()
        output=(f"<em>{output}</em>")
        return output
    return em
def make_underline(function):
    def underline():
        output=function()
        output=(f"<u>{output}</u>")
        return output
    return underline

@app.route("/")
@make_bold
@make_em
@make_underline
def hello():
    return "Guess a number between 0 and 9"
def rand():
    number = random.randint(9)
    return number
@app.route("/<int:guess>")
def answer(guess):
    if guess==ans:
        return ('<h1>You Found Me!</h1>'
                '<iframe src="https://giphy.com/embed/9Y6n9TR7U07ew" width="480" height="480" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/dancing-happy-food-9Y6n9TR7U07ew">via GIPHY</a></p>')
    elif guess<ans:
        return ('<h1>Too Low, try again!</h1>'
                '<iframe src="https://giphy.com/embed/3aJr6ausLWdry" width="480" height="314" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/winnie-the-pooh-3aJr6ausLWdry">via GIPHY</a></p>')
    elif guess>ans:
        return ('<h1>Too high, try again! </h1>'
                '<iframe src="https://giphy.com/embed/777Aby0ZetYE8" width="480" height="259" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/cute-think-pooh-777Aby0ZetYE8">via GIPHY</a></p>')