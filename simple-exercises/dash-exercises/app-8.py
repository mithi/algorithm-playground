import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import flask

print(dcc.__version__) # 0.6.0 or above is required

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# ----
# INPUTS
# ----
input_measure_front = dcc.Input(
  id='input-measure-front',
  type='number',
  value=15,
  min=0
)

input_measure_side = dcc.Input(
  id='input-measure-side',
  type='number',
  value=25,
  min=0
)

input_measure_mid = dcc.Input(
  id='input-measure-mid',
  type='number',
  value=50,
  min=0
)

# ----
# PARTIAL PAGES
# ----

# Navigation 
div_nav = html.Div(
  id='nav',
  children=[
  dcc.Link('Root', href='/'),
  html.Br(),
  dcc.Link('Measurements', href='/measurements'),
  html.Br(),

  dcc.Link('Pose: Kinematics', href='/kinematics'),
  html.Br(),

  dcc.Link('Pose: Inverse Kinematics', href='/inverse-kinematics'),
  html.Br(),
])

# Measurements 
div_hexapod_measurements = html.Div(id='div-hexapod-measurements')

# basic page layout
div_basic = html.Div([
  # represents the URL bar, doesn't render anything
  dcc.Location(id='url', refresh=False),
  # navigation bar
  div_nav,
  # content will be rendered in this element
  html.Div(id='page-content')
])

div_inputs = html.Div([
  html.H1('Input Hexapod measurements:'),
  html.H4(["Front: ", input_measure_front]),
  html.H4(["Middle: ", input_measure_mid]),
  html.H4(["Side: ", input_measure_side])
])
# ----
# PAGES
# ----

page_measurements = html.Div([
  html.Div([
    div_hexapod_measurements,
    div_inputs], style={'columnCount': 2})
])

page_kinematics = html.Div([
  html.H1('Kinematics'),
  html.Div('You can specify the angles of your hexapod here, and see the plot change in real time')
])

page_inverse_kinematics = html.Div([
  html.H1('Inverse Kinematics'),
  html.Div('You can specify the translations rotation of the body here to compute the angles of the pose')
])

page_root = html.Div([
  html.H1('Hello world! Check out the navigation above')
])

PAGES = {
  '/measurements': page_measurements,
  '/kinematics': page_kinematics,
  '/inverse-kinematics': page_inverse_kinematics,
  '/': page_root
}

# ----
# THE APP :) 
# ----
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

def serve_layout():
  if flask.has_request_context():
    return div_basic
  
  return html.Div([
    div_basic,
    page_root, 
    page_measurements,
    page_kinematics,
    page_inverse_kinematics
  ])

app.layout = serve_layout

# ----
# CALLBACKS
# ----

# display the leg measurements as they are changed
@app.callback(
  Output('div-hexapod-measurements', 'children'),
  [
    Input('input-measure-front', 'value'),
    Input('input-measure-side', 'value'),
    Input('input-measure-mid', 'value')
  
  ]
)
def display_measurements(front, side, mid):
  if front is None:
    front = 0
  if side is None:
    side = 0
  if mid is None:
    mid = 0

  return dcc.Markdown('''
    # Hexapod Measurements
    ### front: {}
    ### side: {}
    ### middle: {}
    '''.format(front, side, mid))


# display the page content when link is clicked
@app.callback(
  Output('page-content', 'children'),
  [Input('url', 'pathname')]
)
def display_page(pathname):
  try:
    return PAGES[pathname]
  except KeyError:
    return html.Div([dcc.Markdown('# 404')])

# ----
# RUN SERVER
# ----
if __name__ == '__main__':
  app.run_server(debug=True)