import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

print(dcc.__version__) # 0.6.0 or above is required

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Since we're adding callbacks to elements that don't exist in the app.layout,
# Dash will raise an exception to warn us that we might be
# doing something wrong.
# In this case, we're adding the elements through a callback, so we can ignore
# the exception.
app.config.suppress_callback_exceptions = True


app.layout = html.Div([
  # represents the URL bar, doesn't render anything
  dcc.Location(id='url', refresh=False),

  dcc.Link('Root', href='/'),
  html.Br(),
  dcc.Link('Measurements', href='/measurements'),
  html.Br(),

  dcc.Link('Pose: Kinematics', href='/kinematics'),
  html.Br(),

  dcc.Link('Pose: Inverse Kinematics', href='/inverse-kinematics'),
  html.Br(),

  # content will be rendered in this element
  html.Div(id='page-content')
])

# ----
# INPUTS
# ----

input_measure_front = dcc.Input(
  id='input-measure-front',
  type='number',
  value=15
)

input_measure_side = dcc.Input(
  id='input-measure-side',
  type='number',
  value=25
)

input_measure_mid = dcc.Input(
  id='input-measure-mid',
  type='number',
  value=50
)
# ----
# PAGES
# ----

# Measurements 
div_hexapod_measurements = html.Div(id='div-hexapod-measurements')

page_measurements = html.Div([
  div_hexapod_measurements,
  html.H1('Please Input measurements of this Hexapod'),
  html.H4(["Front: ", input_measure_front]),
  html.H4(["Middle: ", input_measure_mid]),
  html.H4(["Side: ", input_measure_side]),
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
    raise dash.exceptions.PreventUpdate
  if side is None:
    raise dash.exceptions.PreventUpdate
  if mid is None:
    raise dash.exceptions.PreventUpdate

  front = max(0, front)
  side = max(0, side)
  mid = max(0, mid)

  return dcc.Markdown('''
    ### front: {}
    ### side: {}
    ### middle: {}
    '''.format(front, side, mid))

@app.callback(
  Output('page-content', 'children'),
  [Input('url', 'pathname')]
)
def display_page(pathname):
  try:
    return PAGES[pathname]
  except KeyError:
    return html.Div([dcc.Markdown('# 404')])

if __name__ == '__main__':
  app.run_server(debug=True)