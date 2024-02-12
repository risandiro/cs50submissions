from fpdf import FPDF

class PDF():
    def __init__(self, name):
        self._pdf = FPDF(orientation="portrait", format="A4")
        self._pdf.add_page()
        self._pdf.set_font("helvetica", "B", 50)



name = input("Name: ")
pdf = PDF(name)
pdf.save("shirtificate.pdf")

