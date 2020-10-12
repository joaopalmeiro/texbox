from pathlib import Path

from PyPDF2 import PdfFileReader, PdfFileWriter


def parse_args():
    pass


def main():
    input_path = Path("MevaL.pdf")
    input_pdf = PdfFileReader(str(input_path))

    output_pdf = PdfFileWriter()

    # Zero-based numbering
    for page in input_pdf.pages[0:1]:
        output_pdf.addPage(page)

    with Path("pMevaL.pdf").open(mode="wb") as output_file:
        output_pdf.write(output_file)


if __name__ == "__main__":
    main()
