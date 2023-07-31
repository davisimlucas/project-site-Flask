
import os
from flask import Flask, render_template 

app = Flask(__name__)

app.template_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)))
app.static_folder = 'src/static'

@app.route('/')
def homepage():
    return render_template("src/templates/homepage.html")

if __name__ == "__main__":
    app.run(debug= True)
