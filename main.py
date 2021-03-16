import matplotlib.pyplot as plt
from traffic.data.samples import quickstart
import pandas as pd

from traffic.core.projection import Lambert93
from traffic.drawing import countries

flight1 = quickstart["RYR3YM"]
flight2 = quickstart["AFR27GH"]
flight3 = quickstart["RAM667"]
flight4 = quickstart["HOP87DJ"]

#task 2

with plt.style.context("traffic"):
    fig = plt.figure()

    ax0 = fig.add_subplot(111, projection=Lambert93())
    ax1 = fig.add_subplot(111, projection=Lambert93())
    ax2 = fig.add_subplot(111, projection=Lambert93())
    ax3 = fig.add_subplot(111, projection=Lambert93())
    ax4 = fig.add_subplot(111, projection=Lambert93())

#print(flight1.data['timestamp'].describe())

ax0.add_feature(countries())
# Maximum extent for the map
ax0.set_global()
# Remove border and set transparency for background
ax0.outline_patch.set_visible(False)
ax0.background_patch.set_visible(False)


flight1.plot(ax1, label='flight 1')
flight2.plot(ax2, label='flight 2')
flight3.plot(ax3, label='flight 3')
flight4.plot(ax4, label='flight 4')
plt.legend()
#plt.show()


with plt.style.context("traffic"):
    fig, ax = plt.subplots(figsize=(10, 7))
    flight1.plot_time(ax, y=["altitude", "groundspeed"], secondary_y=["groundspeed"])
    plt.title("Flight 1")

    fig, ax = plt.subplots(figsize=(10, 7))
    flight2.plot_time(ax, y=["altitude", "groundspeed"], secondary_y=["groundspeed"])
    plt.title("Flight 2")

    fig, ax = plt.subplots(figsize=(10, 7))
    flight3.plot_time(ax, y=["altitude", "groundspeed"], secondary_y=["groundspeed"])
    plt.title("Flight 3")

    fig, ax = plt.subplots(figsize=(10, 7))
    flight4.plot_time(ax, y=["altitude", "groundspeed"], secondary_y=["groundspeed"])
    plt.title("Flight 4")

plt.show()
'''



'''
#task 3

flight1_radar = flight1.data[['timestamp', 'latitude', 'longitude']]
#since there is one messurment every secon we can just use every 10th entry
flight1_radar = flight1_radar.iloc[::10, :]

flight2_radar = flight2.data[['timestamp', 'latitude', 'longitude']].iloc[::10, :]
flight3_radar = flight3.data[['timestamp', 'latitude', 'longitude']].iloc[::10, :]
flight4_radar = flight4.data[['timestamp', 'latitude', 'longitude']].iloc[::10, :]