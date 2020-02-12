# one output, multiple inputs

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#-------------
# Data
#-------------

DF = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')
AVAILABLE_INDICATORS = DF['Indicator Name'].unique()

#-------------
# Input components
#-------------

# choose indicator for x axis 
dropdown_indicator_x = dcc.Dropdown(
  id='indicator-x',
  options=[{'label': indicator, 'value': indicator} for indicator in AVAILABLE_INDICATORS],
  value='Fertility rate, total (births per woman)',
  )

# choose either to display linear or log for x axis
radio_items_type_x = dcc.RadioItems(
  id='type-x',
  options=[{'label': axis_type, 'value': axis_type} for axis_type in ['Linear', 'Log']],
  value='Linear',
  labelStyle={'display': 'inline-block'}
)

# choose indicator for y axis
dropdown_indicator_y = dcc.Dropdown(
  id='indicator-y',
  options=[{'label': indicator, 'value': indicator} for indicator in AVAILABLE_INDICATORS],
  value='Life expectancy at birth, total (years)'
)

# choose either to display linear or log for y axis
radio_items_type_y = dcc.RadioItems(
  id='type-y',
  options=[{'label': axis_type, 'value': axis_type} for axis_type in ['Linear', 'Log']],
  value='Linear',
  labelStyle={'display': 'inline-block'}
)

# choose to display data of which year
slider_year = dcc.Slider(
  id='slider-year',
  min=DF['Year'].min(),
  max=DF['Year'].max(),
  value=DF['Year'].max(),
  marks={str(year): str(year) for year in DF['Year'].unique()},
  step=None
)

#-------------
# App
#-------------
STYLE_DIV_INPUTS = {'width': '47%', 'display': 'inline-block', 'marginLeft': '1.5%', 'marginRight': '1.5%', 'marginTop': 10, 'marginBottom': 10}

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
  html.Div([
    html.Div([dropdown_indicator_x, radio_items_type_x], style=STYLE_DIV_INPUTS),
    html.Div([dropdown_indicator_y, radio_items_type_y], style=STYLE_DIV_INPUTS)
  ]),

  dcc.Graph(id='indicator-graphic'),
  html.Div([slider_year], style={'width': '95%', 'display': 'inline-block', 'marginLeft': '2.5%', 'marginRight': '2.5%', 'marginTop': 10, 'marginBottom': 10})
])

#-------------
# Callback to change graph
#-------------
@app.callback(
  Output('indicator-graphic', 'figure'),
  [
    Input('indicator-x', 'value'),
    Input('indicator-y', 'value'),
    Input('type-x', 'value'),
    Input('type-y', 'value'),
    Input('slider-year', 'value')
  ]
)
def update_graph(
  indicator_x,
  indicator_y,
  type_x, 
  type_y,
  year):

  df_year = DF[DF['Year'] == year]
  x_values = df_year[df_year['Indicator Name'] == indicator_x]['Value']
  y_values = df_year[df_year['Indicator Name'] == indicator_y]['Value']
  country_names = df_year[df_year['Indicator Name'] == indicator_y]['Country Name']
  
  return {
    'data': [{
      'x': x_values,
      'y': y_values,
      'text': country_names,
      'mode': 'markers',
      'marker': {
        'size': 15,
        'opacity': 0.5,
        'line': {'width': 0.5, 'color': 'white'}
      }
    }],
    
    'layout': {
      'xaxis': {
        'title': indicator_x,
        'type': 'linear' if type_x == 'Linear' else 'log'
      },
      'yaxis': {
        'title': indicator_y,
        'type': 'linear' if type_y == 'Linear' else 'log'
      },
      'margin': {'l': 40, 'b': 40, 't': 10, 'r': 0},
      'hovermode': 'closest'
    }
  }

if __name__ == '__main__':
    app.run_server(debug=True)