import os
import requests
import pdfplumber
import fitz  # PyMuPDF
import argparse
import arxiv
from PIL import Image
import pytesseract
from pdf2image import convert_from_path

def download_arxiv_pdf(arxiv_id, output_folder):
    # Create a subfolder for each arxiv_id
    output_folder = os.path.join(output_folder, arxiv_id)
    os.makedirs(output_folder, exist_ok=True)

    search = arxiv.Search(id_list=[arxiv_id])

    for result in search.results():
        pdf_url = result.pdf_url
        response = requests.get(pdf_url)

        if response.status_code == 200:
            output_path = os.path.join(output_folder, f"{arxiv_id}.pdf")
            with open(output_path, 'wb') as f:
                f.write(response.content)
            print(f"PDF downloaded at {output_path}")
            return output_path
        else:
            print(f"Failed to download PDF for {arxiv_id}")
            return None


def convert_pdf_to_text(pdf_path, output_folder="."):
    # Convert the PDF to images
    images = convert_from_path(pdf_path)

    base = os.path.splitext(os.path.basename(pdf_path))[0]
    text_file_path = os.path.join(output_folder, f"{base}.txt")

    with open(text_file_path, 'w') as f:
        for i, image in enumerate(images):
            # Use Tesseract to do OCR on the image
            text = pytesseract.image_to_string(image)

            # Write the result to the text file
            f.write(text)

    return text_file_path


def extract_images_from_pdf(pdf_path, output_folder="."):
    doc = fitz.open(pdf_path)
    base = os.path.splitext(os.path.basename(pdf_path))[0]
    for i in range(len(doc)):
        for img in doc.get_page_images(i):
            xref = img[0]
            pix = fitz.Pixmap(doc, xref)
            if pix.n < 5:  # this is GRAY or RGB
                pix.save(os.path.join(output_folder, f"{base}_{i}.png"), "png")
            else:  # CMYK: convert to RGB first
                pix1 = fitz.Pixmap(fitz.csRGB, pix)
                pix1.save(os.path.join(output_folder, f"{base}_{i}.png"), "png")
                pix1 = None
            pix = None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download, convert and extract images from an arxiv PDF.')
    parser.add_argument('--arxiv_id', type=str, required=True, help='The arxiv ID of the paper.')
    parser.add_argument('--output_folder', type=str, default="../papers", help='The output folder for the PDF and extracted images.')
    
    args = parser.parse_args()

    pdf_path = download_arxiv_pdf(args.arxiv_id, args.output_folder)
    output_folder = os.path.join(args.output_folder, args.arxiv_id)
    text = convert_pdf_to_text(pdf_path, output_folder)
    extract_images_from_pdf(pdf_path, output_folder)

