import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/world_fires_1_day.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    lats, lons, brights = [], [], []
    for row in reader:
        lats.append(row[0])
        lons.append(row[1])
        brights.append(float(row[2]))

# mapping data
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [0.02*mag for mag in brights],
        'color': brights,
        'colorscale': 'Reds',
        'reversescale': False,
        'colorbar': {'title': 'Brightness'}
    }
}]
fire_layout = Layout(title='World Fires')

fig = {'data': data, 'layout': fire_layout}
offline.plot(fig, filename='global_fires.html')
