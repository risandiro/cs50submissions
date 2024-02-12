from fpdf import FPDF

class PDF():
    def __init__(self, name):
        self._pdf = FPDF()



name = input("Name: ")
pdf = PDF(name)
pdf.save("shirtificate.pdf")

