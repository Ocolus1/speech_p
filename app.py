from flask import Flask
import os


app = Flask(__name__)
app.config.update(
    SECRET_KEY=os.urandom(24),
    DEBUG = True
)

from routes import *

if __name__ == "__main__":
    app.run()