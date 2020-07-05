from flask import Flask
import config

app = Flask(__name__)
app.config.from_object(config)

@app.route("/")
def main():
    return "Hello World"
