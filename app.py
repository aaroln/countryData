from flask import Flask, render_template, request, session, Response
from matplotlib.backends.backend_agg import FigureCanvasAgg
import io
import pandas as pd
from matplotlib.figure import Figure

app = Flask(__name__)

app.secret_key = '099ff9bc6835c551515f6f449cb4c01530dc9d8d5d78881f'

# Datasets
dfPop = pd.read_csv('population.csv')
dfLandCover = pd.read_csv('landCover.csv')
dfUrbanLand = pd.read_csv('urbanLand.csv')
dfUrbanPop = pd.read_csv('urbanPop.csv')

# Getting country list and capitalizing it
countries = dfPop['Country Name'].tolist()
listCountry = [s.upper() for s in countries]

@app.route('/', methods=['GET', 'POST'])
def index():
    user_input = None
    invalid_entry = False
    idx = None
    
    if request.method == 'POST':
        user_input = request.form['user_input'].upper()
        if user_input not in listCountry:
            invalid_entry = True
        else:
            idx = listCountry.index(user_input)
            session['user_input'] = user_input
            session['idx'] = idx

    return render_template('index.html', user_input=user_input, invalid_entry=invalid_entry, idx=idx)

@app.route("/matplot-as-imagePop.png")
def pop_png():
    idx = session.get('idx', None)
    user_input = session.get('user_input', None)

    if idx is not None and user_input is not None:
        fig = Figure()
        axis = fig.add_subplot(1, 1, 1)

        xValuesPop = dfPop.columns.values[1:]
        yValuesPop = (dfPop.iloc[idx].to_numpy()[1:]) / 1000000

        # Adjusting visual settings
        axis.plot(xValuesPop, yValuesPop, color='blue', linestyle='-')

        # Title and labels
        axis.set_title(f'Population Growth of {user_input} from 1960 to 2020 (Ages 15-65)')
        axis.set_xlabel('Year')
        axis.set_ylabel('Population (in millions)')
        axis.set_xticks(xValuesPop[::5])
        axis.set_xticklabels(xValuesPop[::5])

        # Adjusting the size of the figure
        fig.set_size_inches(8, 4)

        output = io.BytesIO()
        FigureCanvasAgg(fig).print_png(output)
        return Response(output.getvalue(), mimetype="image/png")
    else:
        return "User input not available"
    

@app.route("/matplot-as-imageUPop.png")
def Upop_png():
    idx = session.get('idx', None)
    user_input = session.get('user_input', None)

    if idx is not None and user_input is not None:
        fig = Figure()
        axis = fig.add_subplot(1, 1, 1)

        xValuesPop = dfUrbanPop.columns.values[1:]
        yValuesPop = (dfUrbanPop.iloc[idx].to_numpy()[1:])

        # Adjusting visual settings
        axis.plot(xValuesPop, yValuesPop, color='orange', linestyle='-')

        # Title and labels
        axis.set_title(f'Urban Population Percentage in {user_input} from 1960 to 2020')
        axis.set_xlabel('Year')
        axis.set_ylabel('Population (%)')
        axis.set_xticks(xValuesPop[::5])
        axis.set_xticklabels(xValuesPop[::5])

        # Adjusting the size of the figure
        fig.set_size_inches(8, 4)

        output = io.BytesIO()
        FigureCanvasAgg(fig).print_png(output)
        return Response(output.getvalue(), mimetype="image/png")
    else:
        return "User input not available"
    

@app.route("/matplot-as-imageLandA.png")
def LandA_png():
    idx = session.get('idx', None)
    user_input = session.get('user_input', None)

    if idx is not None and user_input is not None:
        fig = Figure()
        axis = fig.add_subplot(1, 1, 1)

        xValuesPop = dfUrbanLand.columns.values[1:]
        yValuesPop = (dfUrbanLand.iloc[idx].to_numpy()[1:])

        # Adjusting visual settings
        axis.plot(xValuesPop, yValuesPop, color='red', linestyle='-')

        # Title and labels
        axis.set_title(f'Total Urban Land Area in {user_input} from 1990 to 2015')
        axis.set_xlabel('Year')
        axis.set_ylabel('Area (sqKm^2)')

        # Adjusting the size of the figure
        fig.set_size_inches(8, 4)

        output = io.BytesIO()
        FigureCanvasAgg(fig).print_png(output)
        return Response(output.getvalue(), mimetype="image/png")
    else:
        return "User input not available"
    

@app.route("/matplot-as-imageLandP.png")
def LandP_png():
    idx = session.get('idx', None)
    user_input = session.get('user_input', None)

    if idx is not None and user_input is not None:
        fig = Figure()
        axis = fig.add_subplot(1, 1, 1)

        xValuesPop = dfLandCover.columns.values[1:]
        yValuesPop = (dfLandCover.iloc[idx].to_numpy()[1:])

        # Adjusting visual settings
        axis.plot(xValuesPop, yValuesPop, color='black', linestyle='-')

        # Title and labels
        axis.set_title(f'Percentage of Urban Land in {user_input} from 1992 to 2019')
        axis.set_xlabel('Year')
        axis.set_ylabel('Urban Land (%)')

        # Adjusting the size of the figure
        fig.set_size_inches(8, 4)

        output = io.BytesIO()
        FigureCanvasAgg(fig).print_png(output)
        return Response(output.getvalue(), mimetype="image/png")
    else:
        return "User input not available"

if __name__ == "__main__":
    app.run(debug=True)
