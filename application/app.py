from flask import Flask, render_template, request
import pandas as pd
import json
import plotly
import plotly.express as px

app = Flask(__name__)

# Datasets
dfPop = pd.read_csv('population.csv')
dfLandCover = pd.read_csv('landCover.csv')
dfUrbanLand = pd.read_csv('urbanLand.csv')
dfUrbanPop = pd.read_csv('urbanPop.csv')


@app.route('/', methods=['GET', 'POST'])
def index():
    user_input = None
    
    if request.method == 'POST':
        user_input = request.form['user_input']
    
    return render_template('index.html', user_input=user_input)

if __name__ == "__main__":
    app.run(debug=True)