from pdf2image import convert_from_path

# Specify the path to the Poppler binaries directory
poppler_path = r'C:\Program Files (x86)\poppler-24.02.0\Library\bin'

# Store Pdf with convert_from_path function
images = convert_from_path('imm.pdf', poppler_path=poppler_path)

for i, image in enumerate(images):
    # Save pages as images in the pdf
    image.save(f'page_{i+1}.jpg', 'JPEG')