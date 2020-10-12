import argparse
from pathlib import Path

from PyPDF2 import PdfFileReader, PdfFileWriter

from .utils import CustomHelpFormatter


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate a partial PDF file from a PDF file.",
        add_help=True,
        formatter_class=CustomHelpFormatter,
    )

    parser._action_groups.pop()
    required = parser.add_argument_group("required arguments")

    required.add_argument(
        "-i",
        "--input",
        required=True,
        help="The path to the PDF file to be partialized.",
        metavar="PATH",
        type=str,
        dest="input_path",
    )

    required.add_argument(
        "-p",
        "--remove-pages",
        required=True,
        help="The pages to be excluded from the original PDF file. The page numbers The numbers follow the one-page numbering in an inclusive way.",
        metavar="PP",
        type=str,
    )

    args = parser.parse_args()

    return args


def main():
    args = parse_args()

    input_path = Path(args.input_path)
    output_path = Path(input_path.parent) / f"p{input_path.name}"

    input_pdf = PdfFileReader(str(input_path))
    output_pdf = PdfFileWriter()

    # Zero-based numbering
    for page_number in range(input_pdf.getNumPages()):
        if page_number not in [24, 25, 26, 27, 28]:
            output_pdf.addPage(input_pdf.getPage(page_number))

    with output_path.open(mode="wb") as output_file:
        output_pdf.write(output_file)


if __name__ == "__main__":
    main()
