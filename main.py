from pdfminer.high_level import extract_text

text = extract_text('path/to/your/pdf/file.pdf')
print(text)