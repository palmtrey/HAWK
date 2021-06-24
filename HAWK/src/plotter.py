import cartopy.crs as ccrs
import csv
import math
import matplotlib.pyplot as plt
import os
from tqdm import tqdm


class Plotter:

    def findWaterfront(self):
        addressFileLoc = ["data/address-csvs/04343.csv", "data/address-csvs/04364.csv", "data/address-csvs/04355.csv"]
        addressFile = [open(addressFileLoc[0]), open(addressFileLoc[1]), open(addressFileLoc[2])]
        csvOut = "Number,Street,County,Zipcode,Longitude,Latitude\n"

        i = 0
        for zip in addressFile:
            print("Now sorting addresses from file: " + addressFileLoc[i])
            i = i + 1
            for fileLine in tqdm(zip):
                if fileLine.startswith('N'):
                    continue
                test = self.determineWaterfront(fileLine, 100)
                if test:
                    csvOut += fileLine

        if not os.path.exists("data/waterfront-address-csvs"):
            os.mkdir("data/waterfront-address-csvs")

        with open("data/waterfront-address-csvs/maranacook.csv", 'w+') as file:
            file.write(csvOut)

    def determineWaterfront(self, line, distance):
        EARTHRADIUS_M = 6371000
        PI = math.pi
        attributes = line.split(',')
        attributes[5] = attributes[5].split('\n')
        lon = attributes[4]
        lat = attributes[5][0]

        lakeFile = open("data/lake/maranacook_lake/maranacook_lake.csv")
        for lakeLine in lakeFile:
            # Skip the first line
            if lakeLine.startswith("L"):
                continue
            attrLake = lakeLine.split(',')
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
                lakeFile.close()
                return True
        lakeFile.close()
        return False

    # Imports address coordinates from a csv file, inputdir.
    # Returns these coordinates as a pair of lists, lons and lats
    def importAddressCoordinates(self, inputdir):
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
    def importLakeCoordinates(self, inputdir):
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
    def plotAddresses(self, ax, coloring):
        lons, lats = self.importAddressCoordinates('data/waterfront-address-csvs/\
maranacook.csv')
        ax.scatter(lons, lats, s=5, marker='o', color=coloring)

    # Plots Maranacook Lake
    # Takes in an axes object, ax, to plot on, and a color, coloring, to plot in
    def plotMaranacookLake(self, ax, coloring):
        # Import coordinates of lake
        lonsLake, latsLake = self.importLakeCoordinates('data/lake/maranacook_lake/maranacook_lake.csv')

        # Plot imported lake
        ax.plot(lonsLake, latsLake, color=coloring)

    # Plots Maranacook Lake's islands
    # Takes in an axes object and a color
    def plotMaranacookIslands(self, ax, coloring):
        # Import coordinates of islands
        lonsIs1, latsIs1 = self.importLakeCoordinates('data/lake/maranacook_la\
ke/maranacook_lake_is1.csv')
        lonsIs2, latsIs2 = self.importLakeCoordinates('data/lake/maranacook_la\
ke/maranacook_lake_is2.csv')
        lonsIs3, latsIs3 = self.importLakeCoordinates('data/lake/maranacook_la\
ke/maranacook_lake_is3.csv')
        lonsIs4, latsIs4 = self.importLakeCoordinates('data/lake/maranacook_la\
ke/maranacook_lake_is4.csv')
        lonsIs5, latsIs5 = self.importLakeCoordinates('data/lake/maranacook_la\
ke/maranacook_lake_is5.csv')
        lonsIs6, latsIs6 = self.importLakeCoordinates('data/lake/maranacook_la\
ke/maranacook_lake_is6.csv')
        lonsIs7, latsIs7 = self.importLakeCoordinates('data/lake/maranacook_la\
ke/maranacook_lake_is7.csv')
        lonsIs8, latsIs8 = self.importLakeCoordinates('data/lake/maranacook_la\
ke/maranacook_lake_is8.csv')

        # Plot imported islands
        ax.fill(lonsIs1, latsIs1, color=coloring)
        ax.fill(lonsIs2, latsIs2, color=coloring)
        ax.fill(lonsIs3, latsIs3, color=coloring)
        ax.fill(lonsIs4, latsIs4, color=coloring)
        ax.fill(lonsIs5, latsIs5, color=coloring)
        ax.fill(lonsIs6, latsIs6, color=coloring)
        ax.fill(lonsIs7, latsIs7, color=coloring)
        ax.fill(lonsIs8, latsIs8, color=coloring)
