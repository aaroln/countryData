from flask import Flask, config, render_template, request
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
countries = dfPop['Country Name'].tolist()
listCountry = [s.upper() for s in countries]

@app.route('/callback', methods=['POST', 'GET'])
def cb():
    return gm(request.args.get('data'))
   
@app.route('/')
def index():
    return render_template('index.html',  graphJSON=gm())

def gm():
    

    fig = px.line(df[df['country']==country], x="year", y="gdpPercap")
    
    
    

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    print(fig.data[0])
    #fig.data[0]['staticPlot']=True
    
    return graphJSON