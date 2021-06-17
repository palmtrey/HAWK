import cartopy.crs as ccrs
import cartopy
import matplotlib.pyplot as plt
import numpy as np
import csv


# A function for coordinate importing from CSV files created by the extractor
# Takes in the directory of the csv file to import coordinates from, and returns
# two lists containing longitude and latitude of the coordinates
def importCoordinates(inputdir):
    lons = []
    lats = []

    with open(inputdir, newline='\n') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        i = 0
        for row in csvreader:
            if i != 0: # Skip the first line, the header line
                lons.append(float(row[0].split(',')[0]))
                lats.append(float(row[0].split(',')[1]))
            i = i + 1
    return lons, lats

# Plots Maranacook Lake
# Takes in an axes object, ax, to plot on, and a color, coloring, to plot in
def plotMaranacookLake(ax, coloring):
    # Import coordinates of lake
    lonsLake, latsLake = importCoordinates('FOCW Mapping\Water Body CSV Coordinate Point Files\maranacook.csv')

    # Plot imported lake
    ax.plot(lonsLake, latsLake, color = coloring)

# Plots Maranacook Lake's islands
# Takes in an axes object, ax, to plot on, and a color, coloring, to plot in
def plotMaranacookIslands(ax, coloring):
    # Import coordinates of islands
    lonsIs1, latsIs1 = importCoordinates('FOCW Mapping\Water Body CSV Coordinate Point Files\maranacook_is1.csv')
    lonsIs2, latsIs2 = importCoordinates('FOCW Mapping\Water Body CSV Coordinate Point Files\maranacook_is2.csv')
    lonsIs3, latsIs3 = importCoordinates('FOCW Mapping\Water Body CSV Coordinate Point Files\maranacook_is3.csv')
    lonsIs4, latsIs4 = importCoordinates('FOCW Mapping\Water Body CSV Coordinate Point Files\maranacook_is4.csv')
    lonsIs5, latsIs5 = importCoordinates('FOCW Mapping\Water Body CSV Coordinate Point Files\maranacook_is5.csv')
    lonsIs6, latsIs6 = importCoordinates('FOCW Mapping\Water Body CSV Coordinate Point Files\maranacook_is6.csv')
    lonsIs7, latsIs7 = importCoordinates('FOCW Mapping\Water Body CSV Coordinate Point Files\maranacook_is7.csv')
    lonsIs8, latsIs8 = importCoordinates('FOCW Mapping\Water Body CSV Coordinate Point Files\maranacook_is8.csv')

    # Plot imported islands
    ax.fill(lonsIs1, latsIs1, color = coloring)
    ax.fill(lonsIs2, latsIs2, color = coloring)
    ax.fill(lonsIs3, latsIs3, color = coloring)
    ax.fill(lonsIs4, latsIs4, color = coloring)
    ax.fill(lonsIs5, latsIs5, color = coloring)
    ax.fill(lonsIs6, latsIs6, color = coloring)
    ax.fill(lonsIs7, latsIs7, color = coloring)
    ax.fill(lonsIs8, latsIs8, color = coloring)

plt.figure()
ax = plt.axes(projection=ccrs.Orthographic())
plotMaranacookLake(ax, 'blue')
plotMaranacookIslands(ax, 'green')
plt.show()
