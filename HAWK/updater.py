# This script pulls necessary updated data from various databases in order to run
# the update process for HAWK

import gdown
import os

url = 'https://drive.google.com/uc?id=1u7nVqfgCpCB7z1wv38vDpWk8XVz28eT2'
output = 'data/temp/me-addresses.txt'
if not os.path.isfile(output):
    os.mkdir('data/temp')
    gdown.download(url, output)