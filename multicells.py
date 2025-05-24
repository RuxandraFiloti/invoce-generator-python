from fpdf import FPDF
 
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
# Set the title of the PDF
pdf.set_font(family="Arial", size=16, style="B")    

content = """
Lorem ipsum dolor sit amet, consectetur adipiscing 
elit, sed do eiusmod tempor incididunt ut labore 
et dolore magna aliqua. Ut enim ad minim veniam, 
quis nostrud exercitation ullamco.
"""
 
pdf.set_font(family="Times", size=12)
pdf.multi_cell(w=0, h=6, txt=content) #the method multi_cell() allows text to wrap within the cell
pdf.output("output.pdf")