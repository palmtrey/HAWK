import cartopy.crs as ccrs
import csv
import math
import matplotlib.pyplot as plt
import os
from tqdm import tqdm


# Finds the waterfront properties given a lake name and list of zip codes to search
def findWaterfront(lake_name, zips:list, distance_from = 100):
    addressFileLoc = []
    addressFile = []
    for zip in zips:
        addressFileLoc.append('../data/address-csvs/' + zip + '.csv')
        addressFile.append(open('../data/address-csvs/' + zip + '.csv'))

    csvOut = "Number,Street,County,Zipcode,Longitude,Latitude\n"

    i = 0

    for zip in addressFile:
        print("Now sorting addresses from file: " + addressFileLoc[i])
        i = i + 1
        for fileLine in tqdm(zip):
            if fileLine.startswith('N'): # if the line is the first line in the file
                continue
            test = determineWaterfront(fileLine, distance_from, '../data/lake/' + lake_name + '/' + lake_name + '.csv')
            if test:
                csvOut += fileLine

    if not os.path.exists("../data/waterfront-address-csvs"):
        os.mkdir("../data/waterfront-address-csvs")

    with open('../data/waterfront-address-csvs/' + lake_name + '.csv', 'w+') as file:
        file.write(csvOut)

def determineWaterfront(line, distance, lake_file_loc):
    EARTHRADIUS_M = 6371000
    PI = math.pi
    attributes = line.split(',')
    attributes[5] = attributes[5].split('\n')
    lon = attributes[4]
    lat = attributes[5][0]

    file = open(lake_file_loc)

    for line in file:
        # Skip the first line
        if line.startswith("L"): # if line is the first line in the lake file
            continue
        attrLake = line.split(',')
        lakeLon = attrLake[0]
        lakeLat = attrLake[1]

        lon1 = float(lon) * PI/180
        lon2 = float(lakeLon) * PI/180
        lat1 = float(lat) * PI/180
        lat2 = float(lakeLat) * PI/180

        deltaLon = lon2 - lon1
        deltaLat = lat2 - lat1

        a = math.sin(deltaLat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(deltaLon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        d = EARTHRADIUS_M * c

        if(d < distance):
            return True
    return False

# Imports address coordinates from a csv file, inputdir.
# Returns these coordinates as a pair of lists, lons and lats
def importAddressCoordinates(inputdir):
    lons = []
    lats = []

    with open(inputdir, newline='\n') as csvfile:
        i = 0

        # Go though each line in the csv file and pull the coordinates for
        # each address
        for line in csvfile:
            if i != 0:
                attributes = line.split(',')
                attributes[5] = attributes[5].split('\r')

                lons.append(float(attributes[4]))
                lats.append(float(attributes[5][0]))
            else:
                i = i + 1
    return lons, lats

# Imports lake polygon coordinates from a csv file, inputdir.
# Returns these coordinates as a pair of lists, lons and lats
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

# Plots the addresses on Maranacook Lake
def plotAddresses(ax, coloring, lake_name):
    lons, lats = importAddressCoordinates('../data/waterfront-address-csvs/' + lake_name + '.csv')
    ax.scatter(lons, lats, s=5, marker='o', color=coloring)

# Plots Maranacook Lake
# Takes in an axes object, ax, to plot on, and a color, coloring, to plot in
def plotMaranacookLake(ax, coloring, lake_name):
    # Import coordinates of lake
    lonsLake, latsLake = importLakeCoordinates('../data/lake/' + lake_name + '/' + lake_name + '.csv')

    # Plot imported lake
    ax.plot(lonsLake, latsLake, color=coloring)

# Plots Maranacook Lake's islands
# Takes in an axes object and a color
def plotMaranacookIslands(ax, coloring, lake_name):
    # Import coordinates of islands
    lonsIs1, latsIs1 = importLakeCoordinates('../data/lake/maranacook_lake/maranacook_lake_is1.csv')
    lonsIs2, latsIs2 = importLakeCoordinates('../data/lake/maranacook_lake/maranacook_lake_is2.csv')
    lonsIs3, latsIs3 = importLakeCoordinates('../data/lake/maranacook_lake/maranacook_lake_is3.csv')
    lonsIs4, latsIs4 = importLakeCoordinates('../data/lake/maranacook_lake/maranacook_lake_is4.csv')
    lonsIs5, latsIs5 = importLakeCoordinates('../data/lake/maranacook_lake/maranacook_lake_is5.csv')
    lonsIs6, latsIs6 = importLakeCoordinates('../data/lake/maranacook_lake/maranacook_lake_is6.csv')
    lonsIs7, latsIs7 = importLakeCoordinates('../data/lake/maranacook_lake/maranacook_lake_is7.csv')
    lonsIs8, latsIs8 = importLakeCoordinates('../data/lake/maranacook_lake/maranacook_lake_is8.csv')

    # Plot imported islands
    ax.fill(lonsIs1, latsIs1, color=coloring)
    ax.fill(lonsIs2, latsIs2, color=coloring)
    ax.fill(lonsIs3, latsIs3, color=coloring)
    ax.fill(lonsIs4, latsIs4, color=coloring)
    ax.fill(lonsIs5, latsIs5, color=coloring)
    ax.fill(lonsIs6, latsIs6, color=coloring)
    ax.fill(lonsIs7, latsIs7, color=coloring)
    ax.fill(lonsIs8, latsIs8, color=coloring)
