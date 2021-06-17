# Takes in a string, line, with address information in it, and returns that information
# in proper CSV format
def extractData(line):

    # Extract the street number from the line and store it in streetNum
    streetNum = -1
    streetNumIndex = line.find('"number":') + 10

    lineSliced = line[streetNumIndex:]
    streetNum = lineSliced.partition('"')[0]

    # Extract the street name from the line and store it in streetName
    streetName = -1
    streetNameIndex = line.find('"street":') + 10
    lineSliced = line[streetNameIndex:]
    streetName = lineSliced.partition('"')[0]

    # Extract the county from the line and store it in countyName
    countyName = -1
    countyNameIndex = line.find('"district":') + 12
    lineSliced = line[countyNameIndex:]
    countyName = lineSliced.partition('"')[0]

    # Extract the postcode and store it in zipcode
    zipcode = -1
    zipcodeIndex = line.find('"postcode":') + 12
    lineSliced = line[zipcodeIndex:]
    zipcode = lineSliced.partition('"')[0]

    # Extract the longitude and store in lon, and the latitude and store in lat
    lon = -1
    lat = -1
    lonIndex = line.find('"coordinates":[') + 15
    lineSliced = line[lonIndex:]
    lon = lineSliced.partition(',')[0]
    lat = lineSliced.partition(',')[2].partition(']')[0]

    return streetNum + "," + streetName + "," + countyName + "," + zipcode + "," + lon + "," + lat

csvOut = "Number,Street,County,Zipcode,Longitude,Latitude\n"
searchfile = open("data/temp/me-addresses.txt", "r")
for line in searchfile:
    if '"04343"' in line:
        csvOut += extractData(line)
        csvOut += "\n"

searchfile.close()

print(csvOut)

with open("Address CSVs\\04343.csv", 'w+') as file:
    file.write(csvOut)

