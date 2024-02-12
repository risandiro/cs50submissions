from fpdf import FPDF

class Shirt():
    def __init__(self, name):
        self.shirt = FPDF(orientation="portrait", format="A4")
        self.shirt.add_page()
        self.shirt.set_font("helvetica", "", 40)
        self.shirt.cell(0, 60, "CS50 Shirtificate", align="C")
        self.shirt.image("../shirtificate/shirtificate.png", w=150, h=150, x=32, y=60)

    def save(self, title):
        self.shirt.output(title)




name = input("Name: ")
pdf = Shirt(name)
pdf.save("shirtificate.pdf")

