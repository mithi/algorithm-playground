import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

  dcc.Input(
    id='input-number',
    type='number',
    value=5
  ),

  html.Table([
    html.Tr([
      html.Td(['x', html.Sup(2)]), 
      html.Td(id='square')
    ]),

    html.Tr([
      html.Td(['x', html.Sup(3)]),
      html.Td(id='cube')
    ]),

    html.Tr([
      html.Td(['2', html.Sup('x')]), 
      html.Td(id='two-to-the-power-of')
    ]),

    html.Tr([
      html.Td(['3', html.Sup('x')]), 
      html.Td(id='three-to-the-power-of')
    ]),

    html.Tr([
      html.Td(['x', html.Sup('x')]),
      html.Td(id='x-raised-to-x')
    ]),
  ])
])


# item
# first argument is the component id 
# second argument is which property of the component we want to update
@app.callback(
  [
    Output('square', 'children'),
    Output('cube', 'children'),
    Output('two-to-the-power-of', 'children'),
    Output('three-to-the-power-of', 'children'),
    Output('x-raised-to-x', 'children')
  ],
  [Input('input-number', 'value')]
)
def compute_function_results(x):
  if isinstance(x, int):
    return x**2, x**3, 2**x, 3**x, x**x
  else:
    return 'N/A', 'N/A', 'N/A', 'N/A', 'N/A',

if __name__ == '__main__':
    app.run_server(debug=True)