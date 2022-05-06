import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # reading dates, T max and T min
    dates, highs, lows = [], [], []
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        high = 5.0*(int(row[5]) - 32) / 9
        low = 5.0*(int(row[6]) - 32) / 9
        # high = int(row[5])
        dates.append(date)
        highs.append(high)
        lows.append(low)

# print data to diagram
plt.style.use("seaborn")
fig, ax = plt.subplots(figsize=(15, 6))
ax.plot(dates, highs, c="red")
ax.plot(dates, lows, c="blue")
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

# formatting diagram
plt.title("Daily high and low temperatures - 2018\nSitka", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (С)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
