# callback(One output - many inputs)
#  components are simply properties
# Output
# [Input]
# Input is the 'value' property of component with id 'my-id'
# Output is the 'children' property of component with id 'my-div'
# Whenever input is changed, the callback will be called
# component_id, component_property keywords are optional
# dash.dependencies.Input is the callback
# dash_core_components.Input is the actual component
# we don't set the value of my-div in the layout, 
# because the callback is called upon startup of the app
# "reactive programming"
# we can update the 'children' property, but we can also update 'style' for example!
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
  dcc.Input(id='my-id', value='initial value', type='text'),
  html.Div(id='my-div')
])


@app.callback(
  Output(component_id='my-div', component_property='children'),
  [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
  return 'You\'ve entered "{}"'.format(input_value)


if __name__ == '__main__':
  app.run_server(debug=True)