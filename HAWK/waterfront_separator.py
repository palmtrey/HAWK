import math
import numpy as np
import os
from tqdm import tqdm

EARTHRADIUS_M = 6371000
PI = math.pi

addressFileLoc = ["data/address-csvs/04343.csv", "data/address-csvs/04364.csv"]

addressFile = [open(addressFileLoc[0]), open(addressFileLoc[1])]

csvOut = "Number,Street,County,Zipcode,Longitude,Latitude\n"


def determineWaterfront(line, distance):
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


i = 0
for zip in addressFile:
    print("Now sorting addresses from file: " + addressFileLoc[i])
    i = i + 1
    for fileLine in tqdm(zip):
        if fileLine.startswith('N'):
            continue
        test = determineWaterfront(fileLine, 25)
        if test:
            csvOut += fileLine


if not os.path.exists("data/waterfront-address-csvs"):
    os.mkdir("data/waterfront-address-csvs")

with open("data/waterfront-address-csvs/maranacook_04364.csv", 'w+') as file:
    file.write(csvOut)
