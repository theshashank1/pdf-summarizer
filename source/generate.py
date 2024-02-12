import pathlib
import textwrap
import os
import markdown2

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


class generateModel:

    def __init__(self):

        genai.configure( api_key = os.getenv('GOOGLE_API_KEY') )
        self.model = genai.GenerativeModel('gemini-pro')

    def to_markdown(self, text):

        text = text.replace('•', '  *')
        return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True)).data

    def generateModel_content(self,text):

        response = self.model.generate_content(text)
        return response.text

    # def chat_on_text(history[]):


if __name__ == '__main__':
    obj = generateModel()
    x = obj.generateModel_content(text = 'What is os?')
    x = obj.to_markdown(x)
    print(x)




# # def to_markdown(text):
# #   text = text.replace('•', '  *')
# #   return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True)).data

# def to_plain_text(text):
#     text = text.replace('•', '  *')
#     markdown_text = textwrap.indent(text, '> ', predicate=lambda _: True)
#     plain_text = markdown2.markdown(markdown_text, extras=["fenced-code-blocks"])
#     return plain_text

# key = os.getenv('GOOGLE_API_KEY')
# genai.configure( api_key = key )

# model = genai.GenerativeModel('gemini-pro')

# q = input()

# response = model.generate_content(q)
# x = response.text
# mark = to_plain_text(x)
# print(mark)