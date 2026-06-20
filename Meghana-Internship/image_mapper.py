def map_images_to_areas(
    page_data,
    image_data
):

    area_image_map = {}

    known_areas = [
        "Hall",
        "Common Bedroom",
        "Master Bedroom",
        "Kitchen",
        "Parking Area",
        "Common Bathroom",
        "External Wall"
    ]

    for image in image_data:

        page_num = image["page"]

        page_text = ""

        for page in page_data:

            if page["page"] == page_num:

                page_text = page["text"]

                break

        matched_area = None

        for area in known_areas:

            if area.lower() in page_text.lower():

                matched_area = area
                break

        if matched_area:

            if matched_area not in area_image_map:

                area_image_map[matched_area] = []

            area_image_map[matched_area].append(
                image["path"]
            )

    return area_image_map