import streamlit as st

from pdf_parser import extract_text
from image_extractor import extract_images
from image_mapper import map_images_to_areas
from ddr_generator import generate_ddr
from report_builder import build_html_report

st.set_page_config(
    page_title="DDR AI Generator",
    layout="wide"
)

st.title("AI Powered DDR Generator")

inspection_pdf = st.file_uploader(
    "Upload Inspection Report",
    type=["pdf"]
)

thermal_pdf = st.file_uploader(
    "Upload Thermal Report",
    type=["pdf"]
)

if inspection_pdf and thermal_pdf:

    if st.button("Generate DDR"):

        with st.spinner(
            "Processing Reports..."
        ):

            inspection_path = "inspection.pdf"
            thermal_path = "thermal.pdf"

            with open(
                inspection_path,
                "wb"
            ) as f:

                f.write(
                    inspection_pdf.read()
                )

            with open(
                thermal_path,
                "wb"
            ) as f:

                f.write(
                    thermal_pdf.read()
                )

            inspection_text, inspection_pages = extract_text(
                inspection_path
            )

            thermal_text, thermal_pages = extract_text(
                thermal_path
            )

            inspection_images = extract_images(
                inspection_path,
                "extracted/inspection_images"
            )

            thermal_images = extract_images(
                thermal_path,
                "extracted/thermal_images"
            )

            area_image_map = map_images_to_areas(
                inspection_pages,
                inspection_images
            )

            image_analysis = []

            ddr = generate_ddr(
                inspection_text,
                thermal_text,
                image_analysis
            )

            report_path = build_html_report(
                ddr,
                area_image_map,
                thermal_images
            )

            st.session_state["ddr"] = ddr
            st.session_state["inspection_images"] = inspection_images
            st.session_state["thermal_images"] = thermal_images
            st.session_state["report_path"] = report_path

            st.success(
                "DDR Generated Successfully"
            )

if "report_path" in st.session_state:

    with open(
        st.session_state["report_path"],
        "r",
        encoding="utf-8"
    ) as f:

        html_content = f.read()

    st.success(
        "DDR Generated Successfully"
    )

    st.download_button(
        label="📄 Download DDR Report",
        data=html_content,
        file_name="DDR_Report.html",
        mime="text/html"
    )