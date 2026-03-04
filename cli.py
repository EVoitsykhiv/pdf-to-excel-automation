import os
import sys
from converter import extract_tables, save_to_excel

if len(sys.argv) < 2:

    print("Usage: python cli.py <pdf_folder>")
    sys.exit()

folder = sys.argv[1]

all_tables = []

for file in os.listdir(folder):

    if file.endswith(".pdf"):

        path = os.path.join(folder, file)

        tables = extract_tables(path)

        all_tables.extend(tables)

if not all_tables:

    print("No tables found")
    sys.exit()

save_to_excel(all_tables, "output.xlsx")

print("Saved data to output.xlsx")  
