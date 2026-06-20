import os


def build_html_report(
    ddr_text,
    area_image_map,
    thermal_images
):

    os.makedirs("outputs", exist_ok=True)

    report_html = ""

    inserted_areas = set()

    known_areas = [
        "Hall",
        "Common Bedroom",
        "Master Bedroom",
        "Kitchen",
        "Parking Area",
        "Common Bathroom",
        "External Wall"
    ]

    lines = ddr_text.split("\n")

    for line in lines:

        report_html += f"{line}<br>"

        matched_area = None

        for area in known_areas:

            if area.lower() in line.lower():

                matched_area = area
                break

        if matched_area and matched_area not in inserted_areas:

            inserted_areas.add(matched_area)

            images = area_image_map.get(
                matched_area,
                []
            )

            report_html += """
            <div class="image-grid">
            """

            if images:

                for img in images:

                    absolute_img_path = os.path.abspath(img)
                    absolute_img_path = absolute_img_path.replace("\\", "/")

                    report_html += f"""
                    <div class="image-card">
                        <img src="file:///{absolute_img_path}">
                        <p>{matched_area}</p>
                    </div>
                    """

            else:

                report_html += """
                <div class="image-card">
                    <p><b>Image Not Available</b></p>
                </div>
                """

            report_html += """
            </div>
            <hr>
            """

    html = f"""
    <html>

    <head>

    <title>Detailed Diagnostic Report</title>

    <style>

    body {{
        font-family: Arial, sans-serif;
        background: #f5f7fa;
        margin: 0;
        padding: 30px;
    }}

    .container {{
        max-width: 1200px;
        margin: auto;
        background: white;
        padding: 40px;
        border-radius: 12px;
        box-shadow: 0px 0px 12px rgba(0,0,0,0.1);
    }}

    .header {{
        text-align: center;
        margin-bottom: 30px;
        border-bottom: 3px solid #1f4e79;
        padding-bottom: 20px;
    }}

    .header h1 {{
        color: #1f4e79;
    }}

    .report-content {{
        line-height: 1.8;
        font-size: 15px;
    }}

    .image-grid {{
        display: flex;
        flex-wrap: wrap;
        gap: 15px;
        margin-top: 15px;
        margin-bottom: 15px;
    }}

    .image-card {{
        width: 280px;
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 10px;
        background: white;
        text-align: center;
    }}

    .image-card img {{
        width: 100%;
        border-radius: 5px;
    }}

    hr {{
        margin-top: 25px;
        margin-bottom: 25px;
    }}

    </style>

    </head>

    <body>

    <div class="container">

        <div class="header">
            <h1>Detailed Diagnostic Report</h1>
            <p>AI Generated Structural Assessment</p>
        </div>

        <div class="report-content">

            {report_html}

        </div>

    </div>

    </body>

    </html>
    """

    output_path = "outputs/generated_report.html"

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(html)

    return output_path