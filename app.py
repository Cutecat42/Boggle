from flask import Flask, request, render_template, redirect, session
from boggle import Boggle
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

words = []

boggle_game = Boggle()


@app.route("/")
def starting():
    """Button to start game"""
    return render_template("/start.html")


@app.route("/start")
def new_boggle():
    """Creates new baord and starts timer"""
    board = boggle_game.make_board()
    session["board"] = board
    return render_template("/board.html", board=board, words=words)


@app.route("/check-word")
def word_check():
    """Checks if word is correct as well as if it's already been guessed"""
    inp = request.args["word"].lower()
    if inp in words:
        return "guessed"
    if boggle_game.check_valid_word(session['board'], inp) == "ok":
        words.append(inp)
    return boggle_game.check_valid_word(session['board'], inp)
