import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# reformat json to readable view
# filename = 'data/eq_11_05_2022_1_day.json'
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'data/readable_eq_data_1_day_m1.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data['features']
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

# mapping data
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [4 * mag for mag in mags],
        'color': mags,
        'colorscale': 'Hot',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'}
    }
}]
eq_layout = Layout(title=all_eq_data['metadata']['title'])

fig = {'data': data, 'layout': eq_layout}
offline.plot(fig, filename='global_earthquakes_30days.html')
