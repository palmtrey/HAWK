import sys
import re

# Takes in a file directory and returns an array with each item beginning with <div> and ending with </div>
def splitIntoDivs(file_dir):
    outputArray = []
    with open(file_dir, 'r') as file:
        file_content = ''

        # Combine all lines into one string
        for line in file:
            file_content += line
        outputArray = findDivs(file_content)
    #print(outputArray)
    return outputArray


def findDivs(string):
    divArray = []
    openLoc = string.find('<div')
    closeLoc = string.find('</div>')

    # continues until one tag isn't found
    while openLoc != -1 and closeLoc != -1:
        divArray.append(string[openLoc:closeLoc + len('</div>')])
        string = string[closeLoc + len('</div>'):-1]
        openLoc = string.find('<div')
        closeLoc = string.find('</div>')

    return divArray



# Begin execution
if __name__ == '__main__':
    sys.setrecursionlimit(20000)
    import pdfminer.high_level as hl
    import sys
    if sys.version_info > (3, 0):
         from io import StringIO
    else:
        from io import BytesIO as StringIO
    from pdfminer.layout import LAParams

    output_string = StringIO()
    #with open('../data/tax_books/richmond_book.pdf', 'rb') as fin:
        #hl.extract_text_to_fp(fin, output_string, output_type = 'html', laparams=LAParams(), codec=None)

    #with open('../richmond_test-form.txt', 'w') as fin:
        #fin.write(output_string.getvalue())

    outArray = splitIntoDivs('../wayne_test-form.txt')

    output = ''
    lines_content = []
    for division in outArray:
        if division == '':
            continue

        if division.find('font-size:8px') == -1:
            continue


        temp = division.replace('\n', '', 50)



        line_content = ''
        line_content_iterator = 0
        inContent = False
        foundClosing = True
        for char in temp:
            if char == '<':
                inContent = False
                if not foundClosing:
                    line_content += ','
                else:
                    foundClosing = False

            elif char == '>':
                foundClosing = True
                inContent = True
                continue

            if inContent == True:
                line_content += char
                foundClosing = False




        output += temp + '\n'
        lines_content.append(line_content)

    just_content_output = ''
    for content in lines_content:

        # Only include content that has letters in it
        if re.search('[a-zA-Z]', content):
            just_content_output += content
            just_content_output += '\n'



    with open('../wayne_test-split.txt', 'w') as file:
        file.write(just_content_output)
