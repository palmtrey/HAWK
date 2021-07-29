import pytesseract
from tqdm import tqdm
import numpy as np
import pdfminer.high_level as hl
import re


# This function takes in a directory containing
def getAddressText(dir, numAddresses):

    ignored_nums = []

    addresses = []
    for iterator in tqdm(range(1, numAddresses)):

        string = pytesseract.image_to_string(dir + '/address_' + str(iterator) + '.png')

        string = string.replace(',','')

        string = string.split('\n')

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
        #print(zip_idx)
        if zip_idx == -1:
            ignored_nums.append(iterator)
            continue
        #assert zip_idx != -1

        # check for out of country addresses and fix
        for item in string[zip_idx+1:]:
            if not item or re.search('GERMANY', item):
                zip_idx += 1
            else:
                break

        billing = ''
        local = ''

        i = 0
        #print(string)
        for item in string:

            # finding the stopping point after the local address
            if re.search('^[0-9]{2,4}-', item) or re.search('^[RU][0-9O]+-', item):
                billing = string[0:i-2]
                local = string[zip_idx+1:i]
                #print('yeet')

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
        #print(billing)
    csvout = 'Billing Address, Local Address\n'

    # Write out the billing and local addresses to a file
    with open('../data/tax_books/tax_book_csvs/monmouth.csv', 'w') as file:
        for address in addresses:
            csvout += address['billing'] + ',' + address['local'] + '\n'
        file.write(csvout)

    print('File written. Ignored address numbers: ')
    print(ignored_nums)


if __name__ == '__main__':
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    total_files = 2753
    getAddressText('../data/tax_books/pngs/monmouth_addresses', total_files + 1)
