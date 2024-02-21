from pdfmine import pdfmine
from generate import generateModel

pdf = pdfmine()
text = pdf.getinfo('/home/user/projects/pdf-summarizer/documents/Ethics_of_Artificial_Intelligence_Research_Challenges_and_Potential_Solutions.pdf')
print(text)

model = generateModel()
print(model.generateModel_content(text))

model.generateModel_chat(text)