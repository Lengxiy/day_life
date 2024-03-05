from PIL import Image, ImageSequence
from reportlab.pdfgen import canvas
import os
import concurrent.futures
import threading

def process_image(img_path, pdf, lock):
    img = Image.open(img_path)
    width, height = img.size

    with lock:
        pdf.drawInlineImage(img, 0, 0, width, height)
        pdf.showPage()

def convert_images_to_pdf(images_folder, output_pdf):
    image_paths = sorted([os.path.join(images_folder, img) for img in os.listdir(images_folder) if img.endswith(('.png', '.jpg', '.jpeg'))])

    # 获取图片的最大宽度和高度
    max_width = max(Image.open(img).width for img in image_paths)
    max_height = max(Image.open(img).height for img in image_paths)

    with open(output_pdf, "wb") as pdf_file:
        pdf = canvas.Canvas(pdf_file, pagesize=(max_width, max_height))
        lock = threading.Lock()

        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(lambda path: process_image(path, pdf, lock), image_paths)

        pdf.save()

# 使用示例
convert_images_to_pdf("E:\\桌面\\1\\img\\img", "output.pdf")
