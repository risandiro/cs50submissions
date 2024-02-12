from fpdf import FPDF

class Shirt():
    def __init__(self, name):
        self.shirt = FPDF(orientation="portrait", format="A4")
        self.shirt.add_page()
        self.shirt.set_font("helvetica", "", 40)
        self.shirt.cell(0, 40, "CS50 Shirtificate", align="C")
        self.shirt.image("../shirtificate/shirtificate.png", w=160, h=150, x=25, y=60)

        self.shirt.set_font_size(40)
        self.shirt.set_text_color(255, 255, 255)
        self.shirt.text(x=42, y= 120, txt={name})

    def save(self, title):
        self.shirt.output(title)




name = input("Name: ")
pdf = Shirt(name)
pdf.save("shirtificate.pdf")

