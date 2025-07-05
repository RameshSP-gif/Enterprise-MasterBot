from flask import Flask, render_template, request
from classifier import classify_query
from bots import hr_bot, finance_bot, marketing_bot, general_bot

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    category = ""
    if request.method == "POST":
        query = request.form["query"]
        category = classify_query(query)
        if category == "hr":
            response = hr_bot(query)
        elif category == "finance":
            response = finance_bot(query)
        elif category == "marketing":
            response = marketing_bot(query)
        else:
            response = general_bot(query)
    return render_template("index.html", response=response, category=category)

if __name__ == "__main__":
    app.run(debug=True)