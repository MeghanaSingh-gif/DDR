import fitz
import os
from PIL import Image


def extract_images(pdf_path, output_folder):

    os.makedirs(output_folder, exist_ok=True)

    doc = fitz.open(pdf_path)

    image_data = []

    for page_index in range(len(doc)):

        page = doc[page_index]

        images = page.get_images(full=True)

        for img_index, img in enumerate(images):

            xref = img[0]

            base_image = doc.extract_image(xref)

            image_bytes = base_image["image"]

            image_ext = base_image["ext"]

            image_name = (
                f"page_{page_index+1}_img_{img_index+1}.{image_ext}"
            )

            image_path = os.path.join(
                output_folder,
                image_name
            )

            with open(image_path, "wb") as f:
                f.write(image_bytes)

            try:

                pil_img = Image.open(image_path)

                width, height = pil_img.size

                # Skip logos / tiny icons
                if width < 300 or height < 300:
                    continue

                image_data.append(
                    {
                        "page": page_index + 1,
                        "path": image_path
                    }
                )

            except:
                pass

    return image_data