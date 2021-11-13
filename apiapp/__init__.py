from flask import Flask

app = Flask(__name__)

import apiapp.views
import apiapp.countries
