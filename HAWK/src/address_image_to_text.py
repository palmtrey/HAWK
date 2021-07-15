import pytesseract
from tqdm import tqdm
import numpy as np



#print(pytesseract.image_to_string(r'../data/tax_books/pngs/wayne_addresses/address_97.png'))


def getAddressText(dir, numAddresses):


    addresses = []
    for i in tqdm(range(1, numAddresses)):
        string = pytesseract.image_to_string(r'../data/tax_books/pngs/wayne_addresses/address_' + str(i) + '.png')

        string = string.split('\n')
        local = ''
        i = 0
        for item in string:
            if len(item) > 4 and item[0].isnumeric() and item[1].isnumeric() and item[2].isnumeric() and item[3] == '-':
                billing = string[0:i-1]
                local = string[i-1]
            i += 1

        billing = ' '.join(billing)

        temp = {
            'billing': billing,
            'local': local
        }
        addresses.append(temp)
        csvout = 'Billing Address, Local Address\n'

    with open('addresses.csv', 'w') as file:
        for address in addresses:
            csvout += address['billing'] + ',' + address['local'] + '\n'
        file.write(csvout)


if __name__ == '__main__':
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    getAddressText('../data/tax_books/pngs/wayne_addresses', 1194)
