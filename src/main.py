from flask import Flask, render_template, request

app = Flask(__name__)

# Global variables for game state
number_to_guess = None
attempts = 0

@app.route("/", methods=["GET", "POST"])
def index():
    global number_to_guess, attempts

    if number_to_guess is None:
        from random import randint
        number_to_guess = randint(1, 100)
        attempts = 0

    message = ""
    if request.method == "POST":
        try:
            guess = int(request.form["guess"])
            attempts += 1

            if guess < number_to_guess:
                message = "Too low! Try again."
            elif guess > number_to_guess:
                message = "Too high! Try again."
            else:
                message = f"Congratulations! You guessed it in {attempts} attempts."
                number_to_guess = None  # Reset the game
        except ValueError:
            message = "Invalid input. Please enter a number."

    return render_template("index.html", message=message, attempts=attempts)

if __name__ == "__main__":
    app.run(debug=True) 
