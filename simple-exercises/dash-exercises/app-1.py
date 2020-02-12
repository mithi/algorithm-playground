# Dash parts
# - layout: describes what the application looks like
# - interactivity
# Dash provides Python classes for all the visual components
# - dash_core_components
# - dash_html_components
#   - has a component for every html tag
# - you can make your own components with Javascript and React.js
# - components described entirely through keyword attributes (declarative)
# - children attribute (special) - always the first attribute
#  - html.H1(children='Hello Dash') is the same as html.H1('Hello Dash')
#    - it can contain a string, a single number or a list of components
# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# --------------------
# General styling
# --------------------
colors = {
  'background': '#111111',
  'text': '#7FDBFF'
}

text_style = {
  'textAlign': 'center',
  'color': colors['text']
}

# --------------------
# Graph properties
# --------------------

# data
graph_data = [
  {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
  {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Montreal'},
]

# styling
graph_layout = {
  'title': 'Dash Data Visualization',
  'plot_bgcolor': colors['background'],
  'paper_bgcolor': colors['background'],
  'font': {
    'color': colors['text']
  }
}



app.layout = html.Div(
  style = {'backgroundColor': colors['background']},
  children = [

    html.H1('Hello Dash', style = text_style),

    html.Div(
      '''
      Dash: A web application framework for Python.
      ''',
      style = text_style
    ),

    dcc.Graph(
      id = 'example-graph',
      figure = {
        'data': graph_data,
        'layout': graph_layout
      }
    )
  ])

if __name__ == '__main__':
  app.run_server(debug=True)
