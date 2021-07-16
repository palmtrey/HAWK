import re
from tqdm import tqdm

def cross_reference(tax_dir, waterfront_dir, zip):

    waterfront_file = open(waterfront_dir)

    town_addresses = []
    csvout = 'Billing Address, Local Address, Zipcode, Longitude, Latitude\n'
    for waterfront_address in tqdm(waterfront_file):
        tax_file = open(tax_dir)
        if re.search(zip, waterfront_address):
            temp = ' '.join(waterfront_address.split(',')[0:2])
            temp = re.sub(' Shore Rd', ' Shore', temp)
            temp = re.sub('N Campers Point Rd', 'North Campers Point', temp)
            temp = re.sub(' Rd', ' Road', temp)
            temp = re.sub(' Dr', ' Drive', temp)
            temp = re.sub(' Ln', ' Lane', temp)
            temp = re.sub(' St', ' Street', temp)
            temp = re.sub('\s', '', temp)
            temp = temp.upper()
            for address in tax_file:

                if re.search('^' + temp + '$', re.sub('\s', '', address.split(',')[1].upper())):
                    csvout += address.split(',')[0] + ',' + waterfront_address.split(',')[0] + ' ' + waterfront_address.split(',')[1] + ',' + waterfront_address.split(',')[3] + ',' + waterfront_address.split(',')[4] + ',' + re.sub('\n', '', waterfront_address.split(',')[5]) + '\n'

    tax_file.close()
    waterfront_file.close()
    with open('final-04355.csv', 'w+') as file:
        file.write(csvout)
            #print(temp)


if __name__ == '__main__':
    cross_reference('../data/tax_books/tax_book_csvs/readfield.csv', '../data/waterfront-address-csvs/maranacook_lake.csv', '04355')
