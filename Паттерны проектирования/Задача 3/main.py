'''Задача 3'''
class OldPrinter:

    def printMessage(self, text):
        print(text)

class IModernPrinter:

    def print(self,text):
        print(text)

class PrinterAdapter:

    def __init__(self, oldPrinter: OldPrinter):
        self.oldPrinter = oldPrinter

    def print(self, text):
        self.oldPrinter.printMessage(text)


def main():
    oldPrinter = OldPrinter()

    printerAdapter = PrinterAdapter(oldPrinter)
    printerAdapter.print('Привет')

if __name__ == "__main__":
    main()
