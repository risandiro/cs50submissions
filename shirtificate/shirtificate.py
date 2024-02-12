from fpdf import FPDF

class Shirt():
    def __init__(self, name):
        self.shirt = FPDF(orientation="portrait", format="A4")
        self.shirt.add_page()
        self.shirt.set_font("helvetica", "", 40)
        self.shirt.cell(0, 40, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")
        self.shirt.image("../shirtificate/shirtificate.png", w=self.shirt.epw, y=60)

        self.shirt.set_font_size(25)
        self.shirt.set_text_color(255, 255, 255)
        self.shirt.cell(self.shirt.epw, 160, f"{name} took CS50", border=0, align='C')

    def save(self, title):
        self.shirt.output(title)

def main():
    name = input("Name: ")
    pdf = Shirt(name)
    pdf.save("shirtificate.pdf")

if __name__ == "__main__":
    main()
