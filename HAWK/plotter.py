import cartopy.crs as ccrs
import cartopy
import matplotlib.pyplot as plt
import numpy as np
import csv


# Imports address coordinates from a csv file, inputdir.
# Returns these coordinates as a pair of lists, lons and lats
def importAddressCoordinates(inputdir):
    lons = []
    lats = []

    with open(inputdir, newline='\n') as csvfile:
        i = 0

        # Go though each line in the csv file and pull the coordinates for each
        # address
        for line in csvfile:
            if i != 0:
                attributes = line.split(',')
                attributes[5] = attributes[5].split('\r')

                lons.append(float(attributes[4]))
                lats.append(float(attributes[5][0]))
            i = i + 1
    return lons, lats


# A function for coordinate importing from CSV files created by the extractor
# Takes in the directory of the csv file to import coordinates from, and returns
# two lists containing longitude and latitude of the coordinates
def importLakeCoordinates(inputdir):
    lons = []
    lats = []

    with open(inputdir, newline='\n') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        i = 0
        for row in csvreader:
            if i != 0:  # Skip the first line, the header line
                lons.append(float(row[0].split(',')[0]))
                lats.append(float(row[0].split(',')[1]))
            i = i + 1
    return lons, lats


def plotAddresses(ax, coloring):
    lons, lats = importAddressCoordinates('data/waterfront-address-csvs/maranacook.csv')
    ax.scatter(lons, lats, s = 5, marker = 'o', color = 'red')


# Plots Maranacook Lake
# Takes in an axes object, ax, to plot on, and a color, coloring, to plot in
def plotMaranacookLake(ax, coloring):
    # Import coordinates of lake
    lonsLake, latsLake = importLakeCoordinates('data/lake/maranacook_lake/maranacook_lake.csv')

    # Plot imported lake
    ax.plot(lonsLake, latsLake, color = coloring)



# Plots Maranacook Lake's islands
# Takes in an axes object, ax, to plot on, and a color, coloring, to plot in
def plotMaranacookIslands(ax, coloring):
    # Import coordinates of islands
    lonsIs1, latsIs1 = importLakeCoordinates('data/lake/maranacook_lake/maranacook_lake_is1.csv')
    lonsIs2, latsIs2 = importLakeCoordinates('data/lake/maranacook_lake/maranacook_lake_is2.csv')
    lonsIs3, latsIs3 = importLakeCoordinates('data/lake/maranacook_lake/maranacook_lake_is3.csv')
    lonsIs4, latsIs4 = importLakeCoordinates('data/lake/maranacook_lake/maranacook_lake_is4.csv')
    lonsIs5, latsIs5 = importLakeCoordinates('data/lake/maranacook_lake/maranacook_lake_is5.csv')
    lonsIs6, latsIs6 = importLakeCoordinates('data/lake/maranacook_lake/maranacook_lake_is6.csv')
    lonsIs7, latsIs7 = importLakeCoordinates('data/lake/maranacook_lake/maranacook_lake_is7.csv')
    lonsIs8, latsIs8 = importLakeCoordinates('data/lake/maranacook_lake/maranacook_lake_is8.csv')

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
plotAddresses(ax, 'red')
print(type(44.324883))
plt.show()
