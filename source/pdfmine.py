from pdfminer.high_level import extract_text



class pdfmine:
    def __init__(self) -> None:

        self.text = None

    def getinfo(self, path) -> str:

        self.text = extract_text(path)
        print(type(self.text))

        return self.text


if __name__ == '__main__':

    obj = pdfmine()
    print(obj.getinfo('/home/user/projects/pdf-summarizer/documents/Ethics_of_Artificial_Intelligence_Research_Challenges_and_Potential_Solutions.pdf'))