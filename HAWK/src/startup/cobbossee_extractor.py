# This script extracts polygon coordinate data from
# 'data/lake/maranacook_lake/cobbossee_lake_coords.txt and separates
# coordinate data into csv files, one for the lake itself, and several for
# the islands.

import numpy as np


# A function to retrieve a specific line from a text file.
# Returns the line in a string format given at line linenum, from file filedir
def getLine(linenum, filedir):
    mylines = []
    with open(filedir, 'rt') as myfile:
        for myline in myfile:
            mylines.append(myline)
    return mylines[linenum - 1]


def processAndWriteToCSV(linenum, inputdir, outputdir):
    # Separate coordinates into three variables, each containing longitudes,
    # latitudes, and altitudes
    lonlatalt = getLine(linenum, inputdir)

    lons = []  # A list of floats to contain all longitudes of points
    lats = []  # A list of floats to contain all latitudes of points
    alts = []  # A list of floats to contain all altitudes of points

    for triad in lonlatalt.split(' '):
        triadsep = triad.split(',')
        if len(triadsep) == 3:
            lons.append(float(triadsep[0]))
            lats.append(float(triadsep[1]))
            alts.append(float(triadsep[2]))

    # Recombine data into triads of double data type
    triads = np.zeros((len(lons), 3))

    for i in range(0, len(lons)):
        triads[i][0] = lons[i]
        triads[i][1] = lats[i]
        triads[i][2] = alts[i]

    # Prepare data for csv write
    csvstring = "Longitude,Latitude,Altitude\n"

    for i in range(0, len(triads)):
        for j in range(0, 3):
            csvstring += str(round(triads[i][j], 6))
            if j == 0 or j == 1:
                csvstring += ","
        csvstring += "\n"

    # Writing the data to a csv file
    with open(outputdir, 'w+') as file:
        file.write(csvstring)


# Extract lake and write to CSV
processAndWriteToCSV(77, 'data/lake/maranacook_lake/maranacook_lake_coords.txt'
                     , 'data/lake/maranacook_lake/maranacook_lake.csv')

# Extract islands and write to CSV
processAndWriteToCSV(100, 'data/lake/maranacook_lake/maranacook_lake_coords.txt', 'data/lake/maranacook_lake/maranacook_lake_is1.csv')
processAndWriteToCSV(123, 'data/lake/maranacook_lake/maranacook_lake_coords.txt', 'data/lake/maranacook_lake/maranacook_lake_is2.csv')
processAndWriteToCSV(146, 'data/lake/maranacook_lake/maranacook_lake_coords.txt', 'data/lake/maranacook_lake/maranacook_lake_is3.csv')
processAndWriteToCSV(169, 'data/lake/maranacook_lake/maranacook_lake_coords.txt', 'data/lake/maranacook_lake/maranacook_lake_is4.csv')
processAndWriteToCSV(192, 'data/lake/maranacook_lake/maranacook_lake_coords.txt', 'data/lake/maranacook_lake/maranacook_lake_is5.csv')
processAndWriteToCSV(215, 'data/lake/maranacook_lake/maranacook_lake_coords.txt', 'data/lake/maranacook_lake/maranacook_lake_is6.csv')
processAndWriteToCSV(238, 'data/lake/maranacook_lake/maranacook_lake_coords.txt', 'data/lake/maranacook_lake/maranacook_lake_is7.csv')
processAndWriteToCSV(261, 'data/lake/maranacook_lake/maranacook_lake_coords.txt', 'data/lake/maranacook_lake/maranacook_lake_is8.csv')
