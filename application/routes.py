from application import app
from flask import render_template, request
import pandas as pd
import json
import plotly
import plotly.express as px


@app.route('/', methods=['GET', 'POST'])
def index():
    user_input = None
    
    if request.method == 'POST':
        user_input = request.form['user_input']
    
    return render_template('index.html', user_input=user_input)