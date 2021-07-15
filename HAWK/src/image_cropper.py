from PIL import Image
import numpy as np

def getAddressesFromPNG(file_address, output_dir, iterator):

    im = Image.open(file_address).convert('1')
    region = np.asarray(im.crop([220, 192, 581, 2000]))

    # Find the row numbers of the black lines
    i = 0
    row_nums = []
    for row in region:
        if (row < 1).all():
            row_nums.append(i)
        i += 1

    # Get rid of duplicate row numbers
    row_nums = np.asarray(row_nums)
    rows = []
    for numCheck in row_nums:
        diff = row_nums - np.full(row_nums.shape, numCheck)
        diff = diff[diff != 0]

        if -1 not in diff:
            rows.append(numCheck)


    # Crop the images using the row numbers
    croppedImages = []
    i = 0
    for row in rows:

        if not i + 1 >= len(rows):
            croppedImages.append(Image.fromarray(region).crop([0, row + 2, 361, rows[i+1]]))
            i += 1
        else:
            croppedImages.append(Image.fromarray(region).crop([0, row + 2, 361, 1808]))

    # Save the cropped address images
    for image in croppedImages:
        image.save(output_dir + '/address_' + str(iterator) + '.png')
        iterator += 1

    return iterator

if __name__ == '__main__':
    iterator = 1

    output_dir = '../data/tax_books/pngs/readfield_addresses'

    for i in range(1, 9):
        iterator = getAddressesFromPNG('../data/tax_books/pngs/readfield_book/readfield_book-00' + str(i) + '.png', output_dir, iterator)

    for i in range(10, 98):
        iterator = getAddressesFromPNG('../data/tax_books/pngs/readfield_book/readfield_book-0' + str(i) + '.png', output_dir, iterator)
