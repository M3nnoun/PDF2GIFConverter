import sys
import os
import fitz  # PyMuPDF
from PIL import Image

def pdf_to_gif(pdf_path, gif_filename):
    try:
        pdf_document = fitz.open(pdf_path)
        images = []

        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            pixmap = page.get_pixmap()
            img = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)
            images.append(img)

        gif_path = os.path.join(os.getcwd(), gif_filename)
        images[0].save(
            gif_path,
            save_all=True,
            append_images=images[1:],
            duration=1000,  # Change the duration (in milliseconds) between frames as needed
            loop=0,  # Set loop to 0 for infinite loop, otherwise specify the desired number of loops
        )

        pdf_document.close()
        print(f"Conversion successful. GIF saved at {gif_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py input_pdf_path")
    else:
        pdf_file = sys.argv[1]
        gif_filename = os.path.splitext(os.path.basename(pdf_file))[0] + ".gif"
        pdf_to_gif(pdf_file, gif_filename)
