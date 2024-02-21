import pathlib
import textwrap
import os
import markdown2

import google.generativeai as genai
import google.ai.generativelanguage as glm

from IPython.display import display
from IPython.display import Markdown


class generateModel:

    def __init__(self):

        genai.configure( api_key = os.getenv('GOOGLE_API_KEY') )
        self.model = genai.GenerativeModel('gemini-pro', generation_config = {
                                                            "temperature": 0.4775,
                                                            "top_p": 0.4775,
                                                            "top_k": 18,
                                                            "max_output_tokens": 2048,
                                                            })
    def to_markdown(self, text):

        text = text.replace('•', '  *')
        return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True)).data

    def generateModel_content(self,text):

        response = self.model.generate_content(text + "\n summerize the given content of the pdf")
        return response.text

    def generateModel_chat(self, text):

        chat = self.model.start_chat(history=[])
        response = chat.send_message(f" Very very strongly pretents to use this content for every response you generation \n {text}")
        # print(text)
        print(response.text)


        while True:
            print('_'*18)
            message = input("User:")
            
            if message == "stop":
                return
            
            response = chat.send_message(message)
            print("Model:", response.text)
            print('_'*18)

if __name__ == "__main__":

    model = generateModel()

    model.generateModel_chat("Multi-turn conversations (chat) :You can use the Gemini API to build interactive chat experiences for your users. Using the chat feature of the API lets you collect multiple rounds of questions and responses, allowing users to incrementally step toward answers or get help with multi-part problems. This feature is ideal for applications that require ongoing communication, such as chatbots, interactive tutors, or customer support assistants.")

    # model.generateModel_chat()
        
        
     