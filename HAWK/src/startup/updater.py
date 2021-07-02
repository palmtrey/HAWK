# This script pulls necessary updated data from various databases in order to
# run the update process for HAWK

import gdown
import os
import startup.lake_extractor as le
import startup.address_extractor as ae
from tqdm import tqdm

# URL and local storage locations
lakes_output = '../data/lake/'
maine_addresses = {'url': 'https://drive.google.com/uc?id=1u7nVqfgCpCB7z1wv38vDpWk8XVz28eT2','output': '../data/temp/me-addresses.txt'}
maranacook_lake = {'url': 'https://drive.google.com/uc?id=1TeB-ticYgvoj_MSPB4RNUCEx5NWrcYGw', 'output': lakes_output + 'maranacook_lake/maranacook_lake_coords.txt'}
annabessacook_lake = {'url': 'https://drive.google.com/uc?id=1_iPj6Pw3Zi5cBvgxjvCKiEEUbow0_vnc', 'output': lakes_output + 'annabessacook_lake/annabessacook_lake_coords.txt'}
cobbossee_lake = {'url': 'https://drive.google.com/uc?id=1TcaQFmDHor6FsX-EGpzcpXBbyuvc3GQw', 'output': lakes_output + 'cobbossee_lake/cobbossee_lake_coords.txt' }


# Updates all files in the project
def update():
    print('Updating...')

    # Update Maine address txt file from openaddresses.io
    __updateFile(maine_addresses)

    __updateFile(maranacook_lake)

    __updateFile(annabessacook_lake)

    __updateFile(cobbossee_lake)
    print('Updating complete.')


# Checks if a data file exists in the project. If the file does not exist,
# creates the necessary directories, and downloads the file from url
# and stores it in the directory output
def __updateFile(pair):

    outSplit = pair['output'].split('/')
    directory = ''

    for dir in outSplit[0:len(outSplit) - 1]:
        directory += dir + '/'
        if not os.path.isdir(directory):
            os.mkdir(directory)

    if not os.path.isfile(pair['output']):
        gdown.download(pair['url'], pair['output'])
        if (pair == maine_addresses):
            __extractMaineAddresses()
        else: # If the file updated is a lake polygon file
            __extractLakeCoordinates(pair)


def __extractMaineAddresses():
    print('Extracting watershed addresses from downloaded file...')
    zips = open('startup/zips.txt')
    for zip in tqdm(zips):
        ae.extractAddresses(zip.split('\n')[0])

    print('Address extraction complete.')


def __extractLakeCoordinates(lake_pair):
    print('Extracting lake polygon coordinates from downloaded file...')
    le.extractPolygons('/'.join(lake_pair['output'].split('/')[0:len(lake_pair['output'].split('/')) -1]))
    print('Lake polygon coordinate extraction complete.')
