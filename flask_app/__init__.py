from flask import Flask
app = Flask(__name__)
app.secret_key="Clovs247"

import logging

logging.basicConfig(filename='record.log', level=logging.ERROR)