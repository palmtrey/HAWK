import pdfminer.layout as pl
import pdfminer.high_level as hl

format = pl.LAParams(char_margin = 10, all_texts = True)
text = hl.extract_text('../data/tax_books/wayne_book.pdf', page_numbers = [2])
file = open('out.txt', 'w+')
file.write(text)
