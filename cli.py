import os
import sys
import logging
from converter import extract_tables, save_to_excel


logging.basicConfig(
    filename="converter.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():

    if len(sys.argv) < 2:
        print("Usage: python cli.py <pdf_folder>")
        sys.exit()

    folder = sys.argv[1]

    if not os.path.exists(folder):
        print("Folder not found")
        sys.exit()

    all_tables = []

    for file in os.listdir(folder):

        if file.endswith(".pdf"):

            path = os.path.join(folder, file)

            print(f"Processing {file}...")
            logging.info(f"Processing {file}")

            try:

                tables = extract_tables(path)
                all_tables.extend(tables)

            except Exception as e:

                print(f"Error processing {file}: {e}")
                logging.error(f"Error processing {file}: {e}")

    if not all_tables:

        print("No tables found")
        logging.warning("No tables extracted")
        sys.exit()

    save_to_excel(all_tables, "output.xlsx")

    print("Saved data to output.xlsx")
    logging.info("Excel file created")


if __name__ == "__main__":
    main()
