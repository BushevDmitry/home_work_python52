from abc import ABC, abstractmethod

class Document(ABC):

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass





class PdfDocument(Document):
    def __init__(self, pdf_filename):
        self.pdf_filename = pdf_filename
        self.file = None


    def open(self):
        self.file = open(self.pdf_filename, 'w+')
        self.file.read()



    def close(self):
        if self.file and not self.file.closed:
            self.file.close()





class WordDocument(Document):
    def __init__(self, word_filename):
        self.word_filename = word_filename
        self.file = None


    def open(self):
        self.file = open(self.word_filename, 'w+')
        self.file.read()
        self.file.read()

    def close(self):
        if self.file and not self.file.closed:
            self.file.close()





class HtmlDocument(Document):
    def __init__(self, html_filename):
        self.html_filename = html_filename
        self.file = None

    def open(self):
        self.file = open(self.html_filename, 'w+')
        self.file.read()

    def close(self):
        if self.file and not self.file.closed:
            self.file.close()





class Application(ABC):
    def __init__(self):
        self.documents = []

    @abstractmethod
    def create_document(self, file):
        pass


    def new_document(self, file):
        doc = self.create_document(file)
        self.documents.append(doc)
        doc.open()

class PdfApplication(Application):
    def create_document(self, file):
        return PdfDocument(file)

class WordApplication(Application):
    def create_document(self, file):
        return WordDocument(file)

class HtmlApplication(Application):
    def create_document(self, file):
        return HtmlDocument(file)


app = WordApplication()


app.new_document("document1.word")
app.new_document("document2.word")
app.new_document("document3.word")

print(f"Создано документов: {len(app.documents)}")