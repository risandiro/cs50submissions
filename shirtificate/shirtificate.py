from fpdf import FPDF 

class PDF():
    def __init__(self, name):



name = input("Name: ")
pdf = PDF(name)
pdf.save("shirtificate.pdf")

