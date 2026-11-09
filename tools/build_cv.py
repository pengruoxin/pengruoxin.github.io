from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

OUTPUT = Path(__file__).resolve().parents[1] / "assets/pdf/peng-ruoxin-cv.pdf"

NAVY = colors.HexColor("#102A43")
BLUE = colors.HexColor("#315A7D")
INK = colors.HexColor("#17212B")
MUTED = colors.HexColor("#536575")
LINE = colors.HexColor("#D8E0E7")


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.5)
    canvas.line(doc.leftMargin, 13 * mm, A4[0] - doc.rightMargin, 13 * mm)
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(MUTED)
    canvas.drawString(doc.leftMargin, 8.5 * mm, "Peng Ruoxin · Academic Curriculum Vitae")
    page_text = f"Page {doc.page}"
    canvas.drawString(A4[0] - doc.rightMargin - stringWidth(page_text, "Helvetica", 8), 8.5 * mm, page_text)
    canvas.restoreState()


def section(title, styles):
    return [Spacer(1, 5), Paragraph(title, styles["section"]), Spacer(1, 3)]


def dated_entry(date, title, subtitle, details, styles):
    body = [Paragraph(f"<b>{title}</b>", styles["entry_title"]), Paragraph(subtitle, styles["entry_subtitle"])]
    body.extend(Paragraph(f"• {item}", styles["bullet"]) for item in details)
    table = Table([[Paragraph(date, styles["date"]), body]], colWidths=[28 * mm, 143 * mm], hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    return KeepTogether(table)


def publication_entry(title, authors, venue, note, link, styles):
    parts = [
        Paragraph(f'<b><link href="{link}" color="#102A43">{title}</link></b>', styles["publication_title"]),
        Paragraph(authors, styles["publication_authors"]),
        Paragraph(f"<i>{venue}</i>. {note}", styles["publication_venue"]),
    ]
    return KeepTogether(parts + [Spacer(1, 4)])


def build_cv():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    doc = BaseDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=14 * mm,
        bottomMargin=18 * mm,
        title="Peng Ruoxin - Academic Curriculum Vitae",
        author="Peng Ruoxin",
        subject="Academic curriculum vitae",
        pageCompression=0,
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="cv-frame", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id="cv", frames=[frame], onPage=footer)])

    sample = getSampleStyleSheet()
    styles = {
        "name": ParagraphStyle("name", parent=sample["Title"], fontName="Helvetica-Bold", fontSize=24, leading=27, textColor=NAVY, alignment=TA_CENTER, spaceAfter=3),
        "tagline": ParagraphStyle("tagline", parent=sample["Normal"], fontName="Helvetica", fontSize=10.5, leading=14, textColor=BLUE, alignment=TA_CENTER, spaceAfter=4),
        "contact": ParagraphStyle("contact", parent=sample["Normal"], fontName="Helvetica", fontSize=8.6, leading=11, textColor=MUTED, alignment=TA_CENTER, spaceAfter=7),
        "section": ParagraphStyle("section", parent=sample["Heading2"], fontName="Helvetica-Bold", fontSize=11.2, leading=14, textColor=NAVY, borderColor=LINE, borderWidth=0, borderPadding=0, spaceBefore=2, spaceAfter=1),
        "body": ParagraphStyle("body", parent=sample["BodyText"], fontName="Helvetica", fontSize=9.2, leading=12.6, textColor=INK, alignment=TA_LEFT),
        "date": ParagraphStyle("date", parent=sample["Normal"], fontName="Helvetica-Bold", fontSize=8.6, leading=11, textColor=BLUE),
        "entry_title": ParagraphStyle("entry_title", parent=sample["Normal"], fontName="Helvetica", fontSize=9.7, leading=12.5, textColor=INK),
        "entry_subtitle": ParagraphStyle("entry_subtitle", parent=sample["Normal"], fontName="Helvetica-Oblique", fontSize=8.8, leading=11.5, textColor=MUTED, spaceAfter=2),
        "bullet": ParagraphStyle("bullet", parent=sample["BodyText"], fontName="Helvetica", fontSize=8.7, leading=11.5, textColor=INK, leftIndent=4, firstLineIndent=-4, spaceAfter=1),
        "publication_title": ParagraphStyle("publication_title", parent=sample["Normal"], fontName="Helvetica", fontSize=9.2, leading=11.8, textColor=NAVY),
        "publication_authors": ParagraphStyle("publication_authors", parent=sample["Normal"], fontName="Helvetica", fontSize=8.4, leading=10.8, textColor=INK),
        "publication_venue": ParagraphStyle("publication_venue", parent=sample["Normal"], fontName="Helvetica", fontSize=8.4, leading=10.8, textColor=MUTED),
    }

    story = [
        Paragraph("Peng Ruoxin", styles["name"]),
        Paragraph("M.Sc. Student · Artificial Intelligence and Big Data Computing", styles["tagline"]),
        Paragraph(
            '<link href="mailto:yiwu1777@gmail.com">yiwu1777@gmail.com</link>  ·  '
            '<link href="https://pengruoxin.github.io">pengruoxin.github.io</link>  ·  '
            '<link href="https://github.com/pengruoxin">GitHub</link>  ·  '
            '<link href="https://scholar.google.com/citations?user=SluSJCYAAAAJ&amp;hl=en">Google Scholar</link>',
            styles["contact"],
        ),
    ]

    story += section("RESEARCH PROFILE", styles)
    story.append(
        Paragraph(
            "My research focuses on efficient reuse and composition of pretrained vision models. I am interested in variable-cardinality model reassembly, low-cost architecture evaluation, multi-objective search, and computer-vision systems for scientific and agricultural applications.",
            styles["body"],
        )
    )

    story += section("EDUCATION", styles)
    story.append(
        dated_entry(
            "2025–2027",
            "The Hong Kong Polytechnic University",
            "M.Sc. in Artificial Intelligence and Big Data Computing · Hong Kong SAR, China",
            ["Expected graduation: March 2027"],
            styles,
        )
    )
    story.append(
        dated_entry(
            "2021–2025",
            "China Agricultural University",
            "B.Eng. in Data Science and Big Data Technology · Beijing, China",
            ["GPA: 3.76/4.00 · Rank: 5/29"],
            styles,
        )
    )

    story += section("RESEARCH EXPERIENCE", styles)
    story.append(
        dated_entry(
            "2025–Present",
            "HeteroWeave: Variable-Cardinality Vision Model Reassembly",
            "Research project · Three-person team",
            [
                "Contributed to parallel block-composition rules, low-cost candidate ranking, and Pareto-guided search across accuracy, parameters, and FLOPs.",
                "Developed CLAS, a cardinality-aware activation proxy whose ranking correlations reach 0.775 and 0.570 on two validation pools.",
                "Evaluated the framework across image classification, vision-language retrieval, semantic segmentation, and object detection; the selected ImageNet-1K model reaches 79.457% Top-1 with 26.7% fewer parameters and 11.9% fewer FLOPs than serial single-block reassembly.",
            ],
            styles,
        )
    )
    story.append(
        dated_entry(
            "2022–2024",
            "Machine-Vision Rice Classification and Quality Evaluation",
            "Research project · China Agricultural University",
            [
                "Built and annotated approximately 20,000 images across six rice varieties and developed detection, variety-classification, completeness-grading, and chalkiness-analysis modules.",
                "Produced a co-first-author paper accepted at the AAAI 2026 AgriAI Workshop and Rice Quality Detection Software V1.0.",
            ],
            styles,
        )
    )
    story.append(
        dated_entry(
            "2023–2024",
            "Computer-Vision Analysis of Pig Aggregation Behavior",
            "Research project · China Agricultural University",
            [
                "Created approximately 3,000 annotated video frames and combined individual detection with spatial-neighborhood analysis to estimate aggregation.",
                "Published as first author at ECPLF 2024 and delivered Pig Aggregation Degree Calculation Software V1.0.",
            ],
            styles,
        )
    )

    story += section("PUBLICATIONS", styles)
    story.append(
        publication_entry(
            "An Overall Real-Time Mechanism for Classification and Quality Evaluation of Rice",
            "Wanke Xia*, <b>Ruoxin Peng*</b>, Haoqi Chu, Xinlei Zhu, Zhiyu Yang, Yiting Zhao, Lili Yang",
            "AAAI 2026 Workshop on AI to Accelerate Science and Engineering in Agriculture",
            "Accepted. *Equal contribution.",
            "https://arxiv.org/abs/2502.13764",
            styles,
        )
    )
    story.append(
        publication_entry(
            "An Improved Pure Fully Connected Neural Network for Rice Grain Classification",
            "Wanke Xia, <b>Ruoxin Peng</b>, Haoqi Chu, Xinlei Zhu, Zhiyu Yang, Lili Yang, Bo Lv, Xunwen Xiang",
            "International Conference on Computer Applications and Information Technology",
            "Accepted at CAIT 2025.",
            "https://arxiv.org/abs/2503.03111",
            styles,
        )
    )
    story.append(
        publication_entry(
            "Intelligent Recognition of Live Pig Aggregation Behavior Based on Convolutional Neural Network",
            "<b>Ruoxin Peng</b>, Chao Liang, Peiguang Xin",
            "European Conference on Precision Livestock Farming",
            "First author, ECPLF 2024.",
            "https://www.ecplf2024.it/program/parallel-sessions-12-00-13-15/",
            styles,
        )
    )

    doc.build(story)


if __name__ == "__main__":
    build_cv()
