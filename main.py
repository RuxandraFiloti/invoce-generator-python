import pandas as pd
import glob 
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

#load the excel files into df
for filepath in filepaths:
   
   # print(df)
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    #extract the invoice number and date from the file name
    filename = Path(filepath).stem
    invoice_number, date = filename.split("-") #returns a list -> each variable has an item from the list 

    #set font for the pdf
    pdf.set_font(family="Arial", size=16, style="B")

    #add invoice no. in pdf doc
    pdf.cell(w=50, h=8, txt=f"Invoice no.{invoice_number}", ln=1)

    #set font for the pdf
    pdf.set_font(family="Arial", size=16, style="B")

    #add date in pdf doc
    pdf.cell(w=50, h=8, txt=f"Date: {date}", ln=1)

    #load the excel file into a dataframe
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    #add the header columns
    header_columns = df.columns
    header_columns = [item.replace("_", " ").title() for item in header_columns]  # replace underscores with spaces and capitalize
    pdf.set_font(family="Arial", size=10, style="B")
    pdf.set_text_color(80, 80, 80)    
    pdf.cell(w=30, h=8, txt=header_columns[0], border=1)
    pdf.cell(w=50, h=8, txt=header_columns[1], border=1)
    pdf.cell(w=35, h=8, txt=header_columns[2], border=1)
    pdf.cell(w=35, h=8, txt=header_columns[3], border=1)
    pdf.cell(w=35, h=8, txt=header_columns[4], border=1, ln=1)

    #add rows of the excel  
    for index, row in df.iterrows():
        pdf.set_font(family="Arial", size=10)
        pdf.set_text_color(80, 80, 80)    
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=50, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=35, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=35, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=35, h=8, txt=str(row["total_price"]), border=1, ln=1) #ln=1 prints the next row
    
    #calculate the total price and add it to the pdf
    total_sum = df["total_price"].sum()
    pdf.set_font(family="Arial", size=10)
    pdf.set_text_color(80, 80, 80)    
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=50, h=8, txt="", border=1)
    pdf.cell(w=35, h=8, txt="", border=1)
    pdf.cell(w=35, h=8, txt="", border=1)
    pdf.cell(w=35, h=8, txt=str(total_sum), border=1, ln=1) #ln=1 prints the next row
    
    #add a line with the total price
    pdf.set_font(family="Arial", size=10, style="B")
    pdf.cell(w=30, h=8, txt=f"The total price is {total_sum}", ln=1)

    #add a company logo (image)
    pdf.set_font(family="Arial", size=12, style="B")
    pdf.cell(w=35, h=8, txt=f"CompanyName")
    pdf.image("company.png", w=10)

    #folder that saves the pdf
    pdf.output(f"PDFs/{filename}.pdf")
