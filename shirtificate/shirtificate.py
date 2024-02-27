from fpdf import FPDF

class Shirt():
    def __init__(self, name):
        self._shirt = FPDF(orientation="portrait", format="A4")
        self._shirt.add_page()
        self._shirt.set_font("helvetica", "", 40)
        self._shirt.cell(0, 40, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")
        self._shirt.image("../shirtificate/shirtificate.png", w=self._shirt.epw, y=60)

        self._shirt.set_font_size(25)
        self._shirt.set_text_color(255, 255, 255)
        self._shirt.cell(self.shirt.epw, 160, f"{name} took CS50", border=0, align='C')

    def save(self, title):
        self._shirt.output(title)

def main():
    name = input("Name: ")
    pdf = Shirt(name)
    pdf.save("shirtificate.pdf")

if __name__ == "__main__":
    main()
