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
        self.shirt.multi_cell(w=self.shirt.epw, text=f"{name} took CS50", new_x="LEFT", fill=True, align="C")
        # self.shirt.text(x=57.5, y= 130, text=f"{name} took CS50")

    def save(self, title):
        self.shirt.output(title)


def main():
    name = input("Name: ")
    pdf = Shirt(name)
    pdf.save("shirtificate.pdf")

if __name__ == "__main__":
    main()
