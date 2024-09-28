from pdf2image import convert_from_path
from cairosvg import svg2png
from PIL import Image
import io
import PyPDF2
import sys, os, subprocess
import re
import aspose.words as aw

class PdfCrop:
    def __init__(self, input_file, output_file=None):
        self.input_file = input_file
        self.input_base = self.get_base(input_file)
        if output_file is None:
            self.output_file = f"{self.input_base}.pdfcrop.pdf"
            self.output_base = self.input_base
        else:
            self.output_base = self.get_base(output_file)
            self.output_file = output_file

    def get_base(self, filename):
        return filename.split(".")[0]

    def crop(self):
        # Get BBOX of PDF
        bbox_text = str(subprocess.check_output(f"gs -dSAFER -dNOPAUSE -dBATCH -sDEVICE=bbox {self.input_file}", shell=True,
                                                stderr=subprocess.STDOUT, encoding='UTF-8'))
        bbox = re.search("%%HiResBoundingBox: ([\-0-9.]+) ([\-0-9.]+) ([\-0-9.]+) ([\-0-9.]+)", bbox_text)
        xmin = float(bbox.group(1))
        ymin = float(bbox.group(2))
        xmax = float(bbox.group(3))
        ymax = float(bbox.group(4))

        # Crop the PDF
        print(
            f"gs -o {self.output_file} -sDEVICE=pdfwrite -c \"[/CropBox [{xmin} {ymin} {xmax} {ymax}] /PAGES pdfmark\" -f {self.input_file}")
        os.system(
            f"gs -o {self.output_file} -sDEVICE=pdfwrite -c \"[/CropBox [{xmin} {ymin} {xmax} {ymax}] /PAGES pdfmark\" -f {self.input_file}")

    def rotate(self, rotation_angle):
        # Open the input PDF file
        with open(self.input_file, 'rb') as input_pdf_file:
            reader = PyPDF2.PdfReader(input_pdf_file)
            writer = PyPDF2.PdfWriter()

            # Rotate each page
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                page.rotate(rotation_angle)
                writer.add_page(page)

            # Write the rotated PDF to the output file
            with open(self.output_file, 'wb') as output_pdf_file:
                writer.write(output_pdf_file)

    def to_svg(self, page_number=1):
        # Make a subprocess for: inkscape --without-gui
        output_file = f'{self.output_base}.svg'
        subprocess.Popen(['pdf2svg', self.input_file, output_file, str(page_number)])
        return


        # doc = aw.Document(self.input_file)
        # extractedPage = doc.extract_pages(page_number, 1)
        # output_file = f'{self.output_base}.svg'
        # extractedPage.save(output_file)

