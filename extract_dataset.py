import re

class Dataset:
    #atributos
    file_name = "_0.txt"
    lists_texts = []
    texts = []


    #construtor
    def __init__(self):
        pass


    #metodos 
    def extract_content(self):
        for i in range(100,1100):
            self.myfile = open(f"dataset/{i}{self.file_name}", "r")
            self.lists_texts.append(self.myfile.readlines())
            self.myfile.close()
  
        for list_text in self.lists_texts:
            self.texts.extend(list_text)
       
        return self.texts

