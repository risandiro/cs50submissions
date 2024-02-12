from fpdf import FPDF

class Shirt():
    def __init__(self, name):
        self._pdf = FPDF(orientation="portrait", format="A4")
        self._pdf.add_page()
        self._pdf.set_font("helvetica", "", 40)
        self._pdf.cell(0, 60, "CS50 Shirtificate", align="C")

    def save(self, title):
        self._pdf.output(title)




name = input("Name: ")
pdf = Shirt(name)
pdf.save("shirtificate.pdf")

