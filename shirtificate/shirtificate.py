from fpdf import FPDF

class PDF():
    def __init__(self, name):
        self._pdf = FPDF(orientation="portrait", format="A4")
        self._pdf.add_page()
        self._pdf.set_font("helvetica", "B", 40)
        self._pdf.cell(0, 60, "CS50 Shirtificate", border=0, align="C")

    def save(self, title):
        self._pdf.output(title)




name = input("Name: ")
pdf = PDF(name)
pdf.save("shirtificate.pdf")

