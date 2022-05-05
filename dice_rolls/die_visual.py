from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die1 = Die()
die2 = Die()
die3 = Die()

results = [die1.roll() + die2.roll() + die3.roll() for _ in range(50000)]

# results analysis
max_res = die1.num_sides + die2.num_sides + die3.num_sides
frequencies = [results.count(value) for value in range(3, max_res + 1)]

# results visualisation
x_values = list(range(3, max_res + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling three D6 50000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6_d6.html')
