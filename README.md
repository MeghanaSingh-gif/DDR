# AI Powered DDR Generator

## Overview

AI Powered DDR Generator is a document intelligence application that automates the creation of **Detailed Diagnostic Reports (DDR)** from property inspection documents.

The system processes:

* Inspection Reports (PDF)
* Thermal Reports (PDF)
* Embedded Inspection Images
* Embedded Thermal Images

Using AI-driven analysis, the application generates a structured and professional Structural Diagnostic Report that highlights observations, probable causes, severity levels, recommended actions, and supporting image evidence.

---
<img width="1920" height="1080" alt="Screenshot (499)" src="https://github.com/user-attachments/assets/dc7df383-9a3c-41fa-88f5-c45107804ff3" />

<img width="1920" height="1080" alt="Screenshot (501)" src="https://github.com/user-attachments/assets/64b09cea-9e43-49c8-85d5-0c4410e274b0" />

<img width="1920" height="1080" alt="Screenshot (503)" src="https://github.com/user-attachments/assets/a6a1ce63-bba1-4431-99fd-3064ef402d16" />

<img width="1920" height="1080" alt="Screenshot (505)" src="https://github.com/user-attachments/assets/142348bb-358e-44c7-8874-fa2ff2b27e34" />

<img width="1920" height="1080" alt="Screenshot (506)" src="https://github.com/user-attachments/assets/44141fa1-8f85-4130-9d82-3e5b2a4ed1fc" />



## Features

### PDF Processing

* Extracts textual content from inspection and thermal reports
* Processes multi-page PDF documents

### Image Extraction

* Extracts embedded images from inspection reports
* Extracts thermal images from thermal reports
* Filters out small icons and irrelevant graphics

### AI-Powered Report Generation

* Uses Google Gemini API
* Generates professional engineering-style diagnostic reports
* Identifies:

  * Observations
  * Root Causes
  * Severity Levels
  * Recommended Actions

### Image Mapping

* Maps extracted images to inspection areas
* Associates visual evidence with corresponding findings

### Automated HTML Report Generation

* Creates a downloadable HTML report
* Professional report layout
* Area-wise findings with image evidence
* Thermal image section

---

## Technology Stack

### Frontend

* Streamlit

### Backend

* Python

### AI Model

* Google Gemini 2.5 Flash

### Libraries Used

* PyMuPDF (fitz)
* Pillow (PIL)
* Streamlit
* Google Generative AI SDK
* Python Dotenv

---

## Project Structure

```text
DDR-AI-Generator/
│
├── app.py
├── ddr_generator.py
├── image_mapper.py
├── image_extractor.py
├── image_analyzer.py
├── pdf_parser.py
├── report_builder.py
│
├── extracted/
│   ├── inspection_images/
│   └── thermal_images/
│
├── outputs/
│   └── generated_report.html
│
├── .env
├── requirements.txt
└── README.md
```


### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

### Run Application

```bash
streamlit run app.py
```

---

## Usage

1. Upload Inspection Report PDF
2. Upload Thermal Report PDF
3. Click **Generate DDR**
4. Wait for processing
5. Download generated HTML report

---

## Sample Output

The generated report contains:

* Executive Summary
* Methodology
* Area-wise Findings
* Observation Analysis
* Severity Assessment
* Recommended Actions
* Supporting Image Evidence
* Thermal Inspection Images

---

## Future Improvements

* Direct image understanding using Gemini Vision
* Better image-to-observation matching
* PDF report export
* Area detection using computer vision
* Interactive dashboard analytics
* Multi-property report generation

---

## Author

**Meghana Singh**

Computer Science Engineering Student

AI/ML Internship Assignment Project
