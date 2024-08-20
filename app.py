from flask import Flask, render_template, request
from backend.app.yllm import yi_generate  
import json
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
# os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_query = request.form["meditation_query"]

        # Generate meditation instructions using your existing function
        meditation = yi_generate(user_query)  

        return render_template("index.html", meditation=meditation)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)