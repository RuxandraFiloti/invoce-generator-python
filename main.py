import pandas as pd
import glob 
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

#load the excel files into df
for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
   # print(df)
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    #extract the invoice number from the file name
    filename = Path(filepath).stem
    invoice_number = filename.split("-")[0] #returns a list -> index is the first element

    #set font for the pdf
    pdf.set_font(family="Arial", size=16, style="B")

    #add text in pdf doc
    pdf.cell(w=50, h=8, txt=f"Invoice no.{invoice_number}")

    #folder that saves the pdf
    pdf.output(f"PDFs/{filename}.pdf")
