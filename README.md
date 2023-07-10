# arxiv scraper

This repository contains a Python script for scraping text and images from a specific arxiv paper given its arxiv ID. It first downloads the paper in PDF format, extracts the text and images, and then saves the images to the desired output folder.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.10 or later.
- You have installed Anaconda or Miniconda for creating and managing Conda environments.
- You have installed Tesseract on your computer. You can install it by following the instructions [here](https://tesseract-ocr.github.io/tessdoc/Installation.html).
- You have installed the necessary Python libraries, which include `arxiv`, `pdfplumber`, `PyMuPDF (fitz)`, `Pillow (PIL)`, `requests`, `pdf2image`, and `pytesseract`. You can install them using pip:
  ```
  pip install arxiv pdfplumber PyMuPDF pillow requests pdf2image pytesseract
  ```

## Using arxiv scraper

This script will download the PDF, convert it to text, and save images from the PDF into PNG files.

To use arxiv scraper, follow these steps:

1. Clone this repository.
2. In the command line, run `cd arxiv_scraper`
3. Create a new conda environment with Python 3.10 and activate it:
   `conda create --name arxiv_scraper python=3.10`
   `conda activate arxiv_scraper`
4. Install the required libraries in your conda environment:
   `pip install -r requirements.txt`.
5. cd into src `cd src`
6. Run `python arxiv_scraper.py --arxiv_id="desired_arxiv_id"`.

Optionally, you can specify a different output folder by adding --output_folder="your_output_folder" to the command.

The script will create a new folder in output_folder for each arxiv_id, and both the PDF and its extracted images will be saved there. For example, if output_folder is ./papers and the arxiv_id is 2104.15000, the PDF will be saved as ./papers/2104.15000/2104.15000.pdf, and the images will be saved as ./papers/2104.15000/2104.15000_0.png, ./papers/2104.15000/2104.15000_1.png, etc.

## Disclaimer

Scraping ArXiv should respect their [robots.txt](https://arxiv.org/robots.txt) file and policies, and consider that the excessive download of articles may be prohibited. Please contact arxiv to get explicit permission to scrape their articles if you plan on doing so on a larger scale.

## License

This project uses the following license: [MIT](https://choosealicense.com/licenses/mit/).
