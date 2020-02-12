import dash
import dash_core_components as dcc
import dash_html_components as html

print(dcc.__version__) # 0.6.0 or above is required

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

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
# PAGES
# ----
page_measurements = html.Div([
  html.H1('Measurements of this Hexapod'),
  html.Div(dcc.Markdown('''
    ### Body Measurements
      - Front: **44** mm
      - Side: **33** mm
      - middle: **100** mm
    ### Leg measurements
      - coxia: **89** mm
      - femur: **72** mm
      - tibia: ** 300** mm
    '''
  ))
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
  dash.dependencies.Output('page-content', 'children'),
  [dash.dependencies.Input('url', 'pathname')]
)
def display_page(pathname):
  return PAGES[pathname]

if __name__ == '__main__':
  app.run_server(debug=True)