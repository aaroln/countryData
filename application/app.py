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

# Getting country list and capitalising it
listCountry = dfPop['Country Name'].tolist()
listCountry = [s.upper() for s in listCountry]


@app.route('/', methods=['GET', 'POST'])
def index():
    user_input = None
    invalid_entry = False
    
    if request.method == 'POST':
        user_input = request.form['user_input'].upper()
        if user_input not in listCountry:
            invalid_entry = True

    return render_template('index.html', user_input=user_input, invalid_entry=invalid_entry)


@app.route('/')
def popChart():

if __name__ == "__main__":
    app.run(debug=True)