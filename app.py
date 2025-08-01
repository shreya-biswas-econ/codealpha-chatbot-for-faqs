from flask import Flask, request, render_template
from chatbot_engine import get_best_answer

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_input = request.form["question"]
        response = get_best_answer(user_input)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
