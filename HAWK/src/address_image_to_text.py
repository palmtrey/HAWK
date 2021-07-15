import pytesseract
from tqdm import tqdm
import numpy as np
import pdfminer.high_level as hl
import re


# This function takes in a directory containing
def getAddressText(dir, numAddresses):


    addresses = []
    for i in tqdm(range(1, numAddresses)):

        if i == 341 or i == 342:
            continue

        string = pytesseract.image_to_string(dir + '/address_' + str(i) + '.png')
        string = string.replace(',','')

        string = string.split('\n')
        local = ''
        i = 0
        zip_idx = -1

        # find the zipcode index
        for item in string:
            num_idx = -1
            j = 0

            # find a number in the item
            for char in item:
                if char.isnumeric():
                    num_idx = j
                    break

                j += 1

            # if there is a number in the item, see if it matches a zip code
            if num_idx != -1 and i > 1:
                if re.search('\s?[0-9]{5}(?:-[0-9]{1,4})?(\s.*)?$', item):
                    zip_idx = i
            i += 1
        assert zip_idx != -1

        # check for out of country addresses and fix
        for item in string[zip_idx+1:]:
            if not item or re.search('GERMANY', item):
                zip_idx += 1
            else:
                break

        billing = ''
        local = ''

        i = 0
        for item in string:

            if len(item) > 4 and ((item[0].isnumeric() and item[1].isnumeric() and item[2].isnumeric() and item[3] == '-') or (item[0].isnumeric() and item[1].isnumeric() and item[2].isnumeric() and item[3].isnumeric() and item[4] == '-')) :
                billing = string[0:i-2]
                local = string[zip_idx+1:i]
            i += 1
        billing = ' '.join(billing)
        local = ' '.join(local)

        if local == '':
            continue

        temp = {
            'billing': billing,
            'local': local
        }

        addresses.append(temp)
    csvout = 'Billing Address, Local Address\n'

    # Write out the billing and local addresses to a file
    with open('../data/tax_books/tax_book_csvs/readfield.csv', 'w') as file:
        for address in addresses:
            csvout += address['billing'] + ',' + address['local'] + '\n'
        file.write(csvout)


if __name__ == '__main__':
    total_files = 574
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    getAddressText('../data/tax_books/pngs/readfield_addresses', total_files + 1)
