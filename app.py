import io
import random
from flask import Flask, Response, request, render_template, jsonify
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backends.backend_svg import FigureCanvasSVG
import pandas as pd
import plotly.express as px

from matplotlib.figure import Figure


app = Flask(__name__)


# Datasets
dfPop = pd.read_csv('population.csv')
dfLandCover = pd.read_csv('landCover.csv')
dfUrbanLand = pd.read_csv('urbanLand.csv')
dfUrbanPop = pd.read_csv('urbanPop.csv')

@app.route("/")
def index():

    countryName = str(request.args.get("country"))
    return render_template("index.html", countryName=countryName)

@app.route("/population-<string:countryName>.svg")
def plot_svg(countryName):

    xValuesPop = dfPop.columns.values[1:]

    for i in range(len(dfPop['Country Name'].values)):
        if dfPop['Country Name'].values[i].lower() == countryName.lower():
            yValuesPop = (dfPop.iloc[0].to_numpy()[1:]) / 1000000
            fig = Figure()
            axis = fig.add_subplot(1, 1, 1)
            axis.plot(xValuesPop, yValuesPop)

            output = io.BytesIO()
            FigureCanvasAgg(fig).print_svg(output)

            return Response(output.getvalue(), mimetype="image/svg+xml")
       
    return "Country not found", 404


if __name__ == "__main__":

    app.run(debug=True, port=8080)