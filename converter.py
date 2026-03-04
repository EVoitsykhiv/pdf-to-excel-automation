import pdfplumber
import pandas as pd


def extract_tables(pdf_path):

    tables = []

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            extracted = page.extract_table()

            if extracted:
                df = pd.DataFrame(extracted[1:], columns=extracted[0])
                tables.append(df)

    return tables


def save_to_excel(tables, output_file):

    with pd.ExcelWriter(output_file) as writer:

        for i, table in enumerate(tables):

            table.to_excel(writer, sheet_name=f"table_{i}", index=False)
