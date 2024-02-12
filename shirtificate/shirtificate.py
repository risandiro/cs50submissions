from fpdf import FPDF

class Shirt():
    def __init__(self, name):
        self.pdf = FPDF(orientation="portrait", format="A4")
        self.pdf.add_page()
        self.pdf.set_font("helvetica", "", 40)
        self.pdf.cell(0, 40, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")
        self.pdf.image("../shirtificate/shirtificate.png", w=self.pdf.epw, y=60)

        self.pdf.set_font_size(25)
        self.pdf.set_text_color(255, 255, 255)
        self.pdf.cell(self.pdf.epw, 160, f"{name} took CS50", border=0, align='C')

    def save(self, title):
        self.pdf.output(title)


name = input("Name: ")
pdf = PDF(name)
pdf.save("shirtificate.pdf")
