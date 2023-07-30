from flask import Flask 

app = Flask(__name__)

@app.route('/')
def homapage():
    return "hell0"

if __name__ == "__main__":
    app.run(debug= True)