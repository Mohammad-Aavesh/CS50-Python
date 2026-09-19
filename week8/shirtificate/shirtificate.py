from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.image("./shirtificate.png" ,15,70,200)
        self.set_font("helvetica", size=40)
        self.cell(0, 50, "CS50 Shirtificate", align ="C")

def main():
    name = input("Name: ")
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("helvetica", size=25)
    pdf.set_text_color(255,255,255)
    pdf.cell(-180, 250, f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
