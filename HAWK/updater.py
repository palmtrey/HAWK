# This script pulls necessary updated data from various databases in order to
# run the update process for HAWK

import gdown
import os


class Updater:
    # Updates all files in the project
    def update(self):
        print('Updating necessary files for address mapping...')

        # Update Maine address txt file from openaddresses.io
        self.updateFile('https://drive.google.com/uc?id=1u7nVqfgCpCB7z1wv38vDpW\
k8XVz28eT2', 'data/temp/me-addresses.txt')

        self.updateFile('https://drive.google.com/uc?id=1TeB-ticYgvoj_MSPB4RNUC\
Ex5NWrcYGw', 'data/lake/maranacook_lake/maranacook_lake_coords.txt')

        print('Updating complete.')

    # Checks if a data file exists in the project. If the file does not exist,
    # creates the necessary directories, and downloads the file from url
    # and stores it in the directory output
    def updateFile(self, url, output):

        outSplit = output.split('/')
        directory = ''

        for dir in outSplit:
            # if the item is not the last item in the list, append it to
            # directory
            if not (len(outSplit) == (outSplit.index(dir) + 1)):
                directory += dir
                directory += '/'

        if not os.path.isdir(directory):
            os.mkdir(directory)
        if not os.path.isfile(output):
            gdown.download(url, output)
            if (output == 'data/temp/me-addresses.txt'):
                self.updateExtractedAddresses()
            if (output == 'data/lake/maranacook_lake/maranacook_lake_coords.txt'):
                self.updateExtractedCoordinates()

    def updateExtractedAddresses(self):
        print('Extracting addresses from downloaded file...')
        os.system('extract_addresses.bat')
        print('Address extraction complete.')

    def updateExtractedCoordinates(self):
        print('Extracting lake polygon coordinates from downloaded file...')
        os.system('python maranacook_extractor.py')
        print('Lake polygon coordinate extraction complete.')
