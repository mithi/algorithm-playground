import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

COUNTRY_TO_CITIES_DICT = {
  'America': ['New York City', 'San Francisco', 'Cincinnati'],
  'Canada': ['Montreal', 'Toronto', 'Ottawa']
}

#---------------
# APP AND COMPONENTS
#---------------

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

radio_items_countries = dcc.RadioItems(
  id='radio-items-countries',
  options=[{'label': country, 'value': country} for country in COUNTRY_TO_CITIES_DICT.keys()],
  value='America'
)

app.layout = html.Div([
  radio_items_countries,
  html.Hr(),
  dcc.RadioItems(id='radio-items-cities'),
  html.Hr(),
  html.Div(id='display-selected-items')
])

#---------------
# CALLBACKS
#---------------

# Given the selected country
# the radio items you can choose from should be cities of that country
@app.callback(
  Output('radio-items-cities', 'options'),
  [Input('radio-items-countries', 'value')]
)
def set_cities_options(selected_country):
  cities = COUNTRY_TO_CITIES_DICT[selected_country]
  return [{'label': city, 'value': city} for city in cities]

# Make the default option the first city
# in the cities you can choose from
@app.callback(
  Output('radio-items-cities', 'value'),
  [Input('radio-items-cities', 'options')]
)
def set_default_city(cities_options):
  return cities_options[0]['value']

# Display the selected city and selected country 
# in a sentence
@app.callback(
  Output('display-selected-items', 'children'),
  [
    Input('radio-items-countries', 'value'),
    Input('radio-items-cities', 'value')
  ]
)
def set_display_selected_items(selected_country, selected_city):
  return dcc.Markdown(
    ' **{}** is a city in **{}**'.format(selected_city, selected_country)
  )

if __name__ == '__main__':
  app.run_server(debug=True)