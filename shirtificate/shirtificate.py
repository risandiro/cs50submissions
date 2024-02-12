from fpdf import FPDF

name = input("Name: ")
pdf = PDF(name)
pdf.save("shirtificate.pdf")

