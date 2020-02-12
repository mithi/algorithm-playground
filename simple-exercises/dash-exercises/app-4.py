import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# --------------------
# Slider
# --------------------
slider_year = dcc.Slider(
  id='year-slider',
  value=df['year'].min(),
  min=df['year'].min(),
  max=df['year'].max(),
  marks={
    str(year): str(year) for year in df['year'].unique()
  },
  step=None
)

# --------------------
# App
# --------------------
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
  dcc.Graph(id='graph-with-slider'),
  slider_year
])

# --------------------
# Return a trace dictionary with styling 
#  given a dataframe containing:
#    - gdp per capital
#    - life expectancy
#    - country
# --------------------
def continent_trace(df):
  return {
    'x': df['gdpPercap'],
    'y': df['lifeExp'],
    'text': df['country'],
    'mode': 'markers',
    'opacity': 0.7,
    'marker': {
      'size': 15,
      'line': {
        'width': 0.5, 
        'color': 'white'
      }
    }
  }

# --------------------
# Callback
#   given the year, 
#     display the country's gdp per capita vs life expectancy
#     color the data points by continent
# --------------------
@app.callback(
  Output('graph-with-slider', 'figure'),
  [Input('year-slider', 'value')])
def update_figure(selected_year):
  
  df_year = df[df.year==selected_year]
  traces = []

  for continent in df_year.continent.unique():
    df_year_continent = df_year[df_year['continent']==continent]
    trace = continent_trace(df_year_continent)
    trace['name'] = continent
    traces.append(trace)

  return {
    'data': traces,
    'layout': {
      'xaxis': {
        'type': 'log',
        'title': 'GDP Per Capita',
        'range':[2.3, 4.8]
      },
      'yaxis': {
        'title': 'Life Expectancy', 
        'range': [20, 90]
      },
      'margin': {
        'l': 40,
        'b': 40,
        't': 10,
        'r': 10
      },
      'legend': {
        'x': 0, 
        'y': 1
      },
      'hovermode': 'closest',
      'transition': {
        'duration': 500
      },
    }
  }


if __name__ == '__main__':
  app.run_server(debug=True)