import fitz


def extract_text(pdf_path):

    doc = fitz.open(pdf_path)

    full_text = ""

    page_data = []

    for page_num in range(len(doc)):

        page = doc[page_num]

        text = page.get_text()

        page_data.append(
            {
                "page": page_num + 1,
                "text": text
            }
        )

        full_text += text

    return full_text, page_data