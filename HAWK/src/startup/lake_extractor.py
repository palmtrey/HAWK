# Extractor for lake polygon coordinate data. Main function
# extractPolygons(lake_dir)

import numpy as np


# extractPolygons(lake_dir) takes in a string with the directory of a specific
# lake (ex. ../../data/lake/maranacook_lake). Takes a .txt file detailing a
# polygon created as a .kml file in Google Earth, and interprets that file
# in terms of a main lake polygon, and 0-infinity island polygon(s). These are
# then written out to separate csv files, one containing the main lake polygon,
# and multiple for the island polygon(s).
def extractPolygons(lake_dir):

    # Extract the lake's name (ex. maranacook_lake) from lake_dir
    lake_name = lake_dir.split('/')[len(lake_dir.split('/')) - 1]

    # Open the coordinate file
    with open(lake_dir + '/' + lake_name + '_coords.txt') as file:

        lines = file.readlines()

        num_writes = 0  # Number of csv files written so far
        output_suffix = ''  # suffix to add to output csv file. Ex. '_is1' for maranacook_lake_is1.csv
        coordinates = ''  # last line surrounded by <coordinates> tags
        coordinates_line = -1  # line num of above

        # iterate through the lines of the file
        for count, line in enumerate(lines):
            # Ensure the file is properly encoded
            if count == 0:
                assert line == '<?xml version="1.0" encoding="UTF-8"?>\n', 'Improper encoding found in lake polygon file.'
            # Format output suffix
            if (num_writes != 0):
                output_suffix = '_is' + str(num_writes)

            # If <coordinates> tag is in the line
            if line.find('<coordinates>') != -1:
                # Record the line containing the coordinates, grab the coords
                coordinates_line = count + 1
                coordinates = lines[coordinates_line]

                # Write the coordinates to a file
                processAndWriteToCSV(coordinates_line + 1, lake_dir + '/' + lake_name + '_coords.txt', lake_dir + '/' + lake_name + output_suffix + '.csv')
                num_writes = num_writes + 1



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
