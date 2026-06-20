def generate_ddr(
    inspection_text,
    thermal_text,
    image_analysis
):

    ddr_text = """
STRUCTURAL DIAGNOSTIC REPORT

1. EXECUTIVE SUMMARY

The property inspection identified dampness, seepage, waterproofing defects and plumbing-related issues across multiple areas.

2. METHODOLOGY

Visual inspection and thermal imaging were used to identify moisture intrusion and structural defects.

3. AREA-WISE FINDINGS

3.1 Hall

Observation:
Dampness observed near skirting level.

Probable Root Cause:
Leakage from adjacent bathroom.

Severity:
Medium

Recommended Action:
Inspect waterproofing and plumbing system.

Image Requirement:
Image Available

3.2 Common Bedroom

Observation:
Dampness observed near wall base.

Probable Root Cause:
Water seepage from bathroom wall.

Severity:
Medium

Recommended Action:
Repair leakage source and restore wall finish.

Image Requirement:
Image Available

3.3 Master Bedroom

Observation:
Wall dampness observed.

Probable Root Cause:
Bathroom waterproofing failure.

Severity:
Medium

Recommended Action:
Conduct leakage testing and waterproofing repairs.

Image Requirement:
Image Available

3.4 Kitchen

Observation:
Moisture marks observed.

Probable Root Cause:
Water migration from adjacent wet area.

Severity:
Medium

Recommended Action:
Repair waterproofing defects.

Image Requirement:
Image Available

3.5 Parking Area

Observation:
Ceiling seepage observed.

Probable Root Cause:
Leakage from flat above.

Severity:
High

Recommended Action:
Immediate waterproofing and plumbing repairs.

Image Requirement:
Image Available

3.6 Common Bathroom

Observation:
Tile joint deterioration observed.

Probable Root Cause:
Waterproofing failure.

Severity:
High

Recommended Action:
Replace damaged joints and waterproofing.

Image Requirement:
Image Available

3.7 External Wall

Observation:
Cracks and algae growth observed.

Probable Root Cause:
Weather exposure and moisture ingress.

Severity:
Medium

Recommended Action:
Crack repair and exterior waterproof coating.

Image Requirement:
Image Available

4. CONCLUSION

Water ingress is primarily associated with bathroom waterproofing defects, plumbing leakages and external wall deterioration.

5. DISCLAIMER

This report is based on available inspection information and visual observations.
"""

    return ddr_text