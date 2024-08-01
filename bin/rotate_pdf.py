import PyPDF2

import sys

def rotate_pdf(input_pdf_path, output_pdf_path, rotation_angle):
    # Open the input PDF file
    with open(input_pdf_path, 'rb') as input_pdf_file:
        reader = PyPDF2.PdfFileReader(input_pdf_file)
        writer = PyPDF2.PdfFileWriter()

        # Rotate each page
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            page.rotateClockwise(rotation_angle)
            writer.addPage(page)

        # Write the rotated PDF to the output file
        with open(output_pdf_path, 'wb') as output_pdf_file:
            writer.write(output_pdf_file)

if __name__ == '__main__':
    input_pdf_path = sys.argv[1]  # Path to the input PDF
    rotation_angle = 90  # Rotation angle (90, 180, 270)
    rotate_pdf(input_pdf_path, input_pdf_path, rotation_angle)
    print(f"Rotated PDF saved to '{input_pdf_path}'")
