from fpdf import FPDF
from PIL import Image

thename = input("Name: ")
class PDF:
    def __init__(self, name):
        self.pdf = FPDF()
        self.pdf.add_page()
        self.pdf.set_font("helvetica", "B", 16)
        self.pdf.cell(60, 10, 'CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')
        self.pdf.image("shirtificate.png", w=self.pdf.epw)
        self.pdf.set_font_size(20)
        self.pdf.set_text_color(255,255,255)
        self.pdf.text(x = 50, y = 142, txt=f"{name} took CS50")

    def save(self, name):
        self.pdf.output(name)

pd = PDF(thename)
pd.save("shirtificate.pdf")