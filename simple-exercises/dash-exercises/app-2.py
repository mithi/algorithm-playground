import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

# --------------
# Load files
# --------------
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
df_agriculture_exports = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')
df_life_expectancy_vs_gdp = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

# --------------
# Styles
# --------------

margin_style = {'marginLeft': 30, 'marginRight': 30, 'marginTop': 30, 'marginBottom': 30}

# --------------
# Table generator
# --------------
def generate_table(dataframe, max_rows=10):
  header = [html.Tr([html.Th(col) for col in dataframe.columns])]

  body = [
    html.Tr([html.Td(dataframe.iloc[row][col]) for col in dataframe.columns]) \
    for row in range(min(len(dataframe), max_rows))
  ]

  return html.Table(header + body)

# --------------
# Graph: Life expectancy vs GDP 
# --------------

def life_vs_gdp_data_points(df, continent):
  return {
    'name': continent,
    'x': df[df['continent'] == continent]['gdp per capita'],
    'y': df[df['continent'] == continent]['life expectancy'],
    'text' : df[df['continent'] == continent]['country'],
    'mode': 'markers',
    'opacity': 0.7,
    'marker': {
      'size': 15,
      'line': {'width': 0.5, 'color': 'white'}
    }
  }

life_vs_gdp_layout = {
  'xaxis': {'type': 'log', 'title': 'GDP Per Capita'},
  'yaxis': {'title': 'Life Expectancy'},
  'margin': {'l': 40, 'b': 40, 't': 10, 'r': 10},
  'legend': {'x': 0, 'y': 1},
  'hovermode':'closest'
}

life_vs_gdp_data = [life_vs_gdp_data_points(df_life_expectancy_vs_gdp, continent) \
  for continent in df_life_expectancy_vs_gdp.continent.unique()
]

# --------------
# Text
# --------------
markdown_text = '''

# ...
### Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!
# ...

'''

# --------------
# Examples: Other components
# --------------

# DROPDOWN
example_dropdown =  dcc.Dropdown(
  options=[
    {'label': 'New York City', 'value': 'NYC'},
    {'label': 'Montreal', 'value': 'MTL'},
    {'label': 'San Francisco', 'value': 'SF'}
  ],
  value='MTL'
)

# DROPDOWN - MULTISELECT
example_dropdown_multiselect = dcc.Dropdown(
  options=[
    {'label': 'New York City', 'value': 'NYC'},
    {'label': 'Montreal', 'value': 'MTL'},
    {'label': 'San Francisco', 'value': 'SF'}
  ],
  value=['MTL', 'SF'],
  multi=True
)

# RADIO ITEMS
example_radio_items = dcc.RadioItems(
  options=[
    {'label': 'New York City', 'value': 'NYC'},
    {'label': u'Montréal', 'value': 'MTL'},
    {'label': 'San Francisco', 'value': 'SF'},
    {'label': 'Philippines', 'value': 'PH'}

  ],
  value='MTL'
)

# CHECKBOXES
example_checkboxes = dcc.Checklist(
  options=[
    {'label': 'New York City', 'value': 'NYC'},
    {'label': 'Montreal', 'value': 'MTL'},
    {'label': 'San Francisco', 'value': 'SF'},
    {'label': 'Philippines', 'value': 'PH'}
  ],
  value=['MTL', 'SF']
)

# TEXT INPUT
example_text_input = dcc.Input(value='MTL', type='text')

# SLIDER
example_slider = dcc.Slider(
  min=0,
  max=9,
  marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
  value=5,
)

# --------------------
# HTML Division
# --------------------

# Helper for input components
def make_component_html_div(label, component):
  return html.Div([
    html.Label(dcc.Markdown('### ' + label)),
    component
    ], style=margin_style)

# Agriculture exports table
section_exports = html.Div([
  html.H1('US Agriculture Exports (2011)'),
  generate_table(df_agriculture_exports),
], style={'width': 700})

# Life Expectancy vs GDP
section_life_vs_gdp = html.Div([
  html.H1('Life Expectancy vs GDP'),
  dcc.Graph(
    id='life-vs-gdp',
    figure={
      'data': life_vs_gdp_data, 
      'layout': life_vs_gdp_layout
    }
  )
], style=margin_style)

# Examples of input components
section_example_components = html.Div([
  html.H1(dcc.Markdown('# INPUT COMPONENTS')),
  make_component_html_div('Dropdown', example_dropdown),
  make_component_html_div('Dropdown Multiselect', example_dropdown_multiselect),
  make_component_html_div('Text Input', example_text_input),
  make_component_html_div('Slider', example_slider),
  make_component_html_div('Radio Items', example_radio_items),
  make_component_html_div('Checkboxes', example_checkboxes),
], style={'columnCount': 2, 'marginLeft': 10, 'marginRight': 10, 'marginTop': 10, 'marginBottom': 10})

# --------------
# App specification
# --------------
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
  section_life_vs_gdp,
  dcc.Markdown('# .'),
  section_example_components,
  section_exports,
  dcc.Markdown(markdown_text)
])

if __name__ == '__main__':
  app.run_server(debug=True)