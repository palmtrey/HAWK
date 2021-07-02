import pdfminer.layout as pl
import pdfminer.high_level as hl

format = pl.LAParams(char_margin = 10, all_texts = True)
text = hl.extract_text('book.pdf', format)
file = open('out1.txt', 'w+')
file.write(text)
