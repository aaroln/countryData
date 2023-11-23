import io
import random
from flask import Flask, Response, request, render_template
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backends.backend_svg import FigureCanvasSVG
import pandas as pd


from matplotlib.figure import Figure


app = Flask(__name__)

dfPop = pd.read_csv('population.csv')
dfLandCover = pd.read_csv('landCover.csv')
dfUrbanLand = pd.read_csv('urbanLand.csv')
dfUrbanPop = pd.read_csv('urbanPop.csv')


@app.route("/")
def index():
    value = int(request.args.get("value", 0))
    return render_template("index.html", value=value)


@app.route("/matplot-as-image-<int:value>.png")
def plot_png(value=0):
    """ renders the plot on the fly.
    """

    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)

    xValuesPop = dfPop.columns.values[1:]
    yValuesPop = (dfPop.iloc[value].to_numpy()[1:]) / 1000000
    
    axis.plot(xValuesPop, yValuesPop)


    output = io.BytesIO()
    FigureCanvasAgg(fig).print_png(output)
    return Response(output.getvalue(), mimetype="image/png")


@app.route("/matplot-as-image2-<int:value>.png")
def plot_png2(value=0):
    """ renders the plot on the fly.
    """

    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)

    xValuesCover = dfLandCover.columns.values[1:]
    yValuesCover = (dfLandCover.iloc[value].to_numpy()[1:]) 
    
    axis.plot(xValuesCover, yValuesCover)

    output = io.BytesIO()
    FigureCanvasAgg(fig).print_png(output)
    return Response(output.getvalue(), mimetype="image/png")


@app.route("/matplot-as-image3-<int:value>.png")
def plot_png3(value=0):
    """ renders the plot on the fly.
    """

    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)

    xValuesUrban = dfUrbanLand.columns.values[1:]
    yValuesUrban = (dfUrbanLand.iloc[value].to_numpy()[1:]) 
    
    axis.plot(xValuesUrban, yValuesUrban)

    output = io.BytesIO()
    FigureCanvasAgg(fig).print_png(output)
    return Response(output.getvalue(), mimetype="image/png")


@app.route("/matplot-as-image4-<int:value>.png")
def plot_png4(value=0):
    """ renders the plot on the fly.
    """

    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)

    xValuesUrbanPop = dfUrbanPop.columns.values[1:]
    yValuesUrbanPop = (dfUrbanPop.iloc[value].to_numpy()[1:]) 
    
    axis.plot(xValuesUrbanPop, yValuesUrbanPop)

    output = io.BytesIO()
    FigureCanvasAgg(fig).print_png(output)
    return Response(output.getvalue(), mimetype="image/png")


if __name__ == "__main__":
   
    app.run(debug=True, port=8080)