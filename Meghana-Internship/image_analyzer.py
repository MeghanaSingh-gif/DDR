import google.generativeai as genai
from PIL import Image
import time


def analyze_images(
    image_data,
    model
):

    image_analysis = []

    # Analyze only representative images
    # Example:
    # 70 images -> ~14 images

    selected_images = image_data[::5]

    print(
        f"Total Images: {len(image_data)}"
    )

    print(
        f"Images Sent To Gemini: {len(selected_images)}"
    )

    for index, image in enumerate(
        selected_images
    ):

        try:

            print(
                f"Analyzing Image {index+1}/{len(selected_images)}"
            )

            img = Image.open(
                image["path"]
            )

            prompt = """
You are a structural inspection expert.

Analyze this inspection image.

Return ONLY in this format:

AREA: <area>

ISSUE: <issue>

DESCRIPTION: <description>

Possible Areas:

Hall
Common Bedroom
Master Bedroom
Kitchen
Parking Area
Common Bathroom
External Wall

Examples:

AREA: Hall
ISSUE: Dampness
DESCRIPTION: Dampness visible near skirting level.

AREA: External Wall
ISSUE: Crack
DESCRIPTION: Crack observed on external wall surface.

AREA: Parking Area
ISSUE: Seepage
DESCRIPTION: Water seepage visible on ceiling.
"""

            response = model.generate_content(
                [prompt, img]
            )

            result = response.text

            image_analysis.append(
                {
                    "path": image["path"],
                    "page": image["page"],
                    "analysis": result
                }
            )

            print(result)

            # Gemini Free Tier:
            # 5 requests / minute

            if index != len(selected_images) - 1:

                print(
                    "Waiting 12 seconds..."
                )

                time.sleep(12)

        except Exception as e:

            print(
                f"Failed: {image['path']}"
            )

            print(e)

    return image_analysis