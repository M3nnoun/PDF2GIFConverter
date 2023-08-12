# PDF2GIFConverter
Easily convert PDF documents into animated GIFs using this Python script. This tool leverages the PyMuPDF and Pillow (PIL) libraries to extract pages from PDFs, convert them to images, and then combine them to create engaging animated GIFs.

# PDF to GIF Converter

Converts a PDF document into an animated GIF using PyMuPDF and PIL libraries.

## 📖 Overview

This script converts a PDF document into an animated GIF. It extracts the pages from the PDF, converts each page to an image, and then combines the images to create an animated GIF.

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- PyMuPDF
- Pillow (PIL)

### Installation

1. Clone this repository to your local machine.
2. Install the required libraries using the following command:
```bash
pip install PyMuPDF Pillow
```


### Usage

1. Open a terminal or command prompt.
2. Navigate to the directory containing the script (`pdf_to_gif_converter.py`).
3. Run the script by entering the following command, replacing `input.pdf` with the path to your input PDF file:

```bash
python pdf_to_gif_converter.py input.pdf
```
The output GIF file will be generated in the same directory as the input PDF file, with the same name but a .gif extension.

💡 Notes
The script uses the fitz library (PyMuPDF) to extract pages from the PDF and the Pillow (PIL) library to process images.
You can adjust the animation properties (duration and loop) by modifying the script's parameters.
In case of any errors during the conversion process, an error message will be displayed.
Make sure that the input PDF file is in the same directory as the script or provide the full path to the input file.

Feel free to contribute to this repository by submitting pull requests or creating issues. If you have any questions or need assistance, please reach out!


