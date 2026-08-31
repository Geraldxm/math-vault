# /// script
# requires-python = ">=3.10"
# dependencies = ["reportlab==4.4.10"]
# ///
"""Build the math-vault technical report with `uv run --script docs/build_report.py`."""
import os
from pathlib import Path

os.environ["SOURCE_DATE_EPOCH"] = "1788134400"

from reportlab import rl_config
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import BaseDocTemplate, Frame, KeepTogether, PageBreak, Paragraph, Spacer, Table, TableStyle


OUT = Path(__file__).with_name("math-vault-v0.1.0.pdf")
TITLE = "math-vault: Curated, Traceable Snapshots of Public Mathematical Reasoning Datasets"
REPORT_DATE = "31 August 2026"
DATASET_DOI = "10.5281/zenodo.21411214"

rl_config.invariant = True


def page_number(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#cad4dd"))
    canvas.line(doc.leftMargin, 0.56 * inch, A4[0] - doc.rightMargin, 0.56 * inch)
    canvas.setFillColor(colors.HexColor("#586576"))
    canvas.setFont("Helvetica", 8)
    canvas.drawString(doc.leftMargin, 0.37 * inch, "math-vault dataset documentation report")
    canvas.drawRightString(A4[0] - doc.rightMargin, 0.37 * inch, str(doc.page))
    canvas.restoreState()


def p(text, style):
    return Paragraph(text, style)


def build():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="TitleMV", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=26, leading=31, textColor=colors.HexColor("#18212f"), alignment=TA_CENTER, spaceAfter=13))
    styles.add(ParagraphStyle(name="AuthorMV", parent=styles["Normal"], fontName="Helvetica", fontSize=18, leading=22, alignment=TA_CENTER, textColor=colors.HexColor("#364458"), spaceAfter=5))
    styles.add(ParagraphStyle(name="InstitutionMV", parent=styles["Normal"], fontName="Helvetica", fontSize=10.5, leading=15, alignment=TA_CENTER, textColor=colors.HexColor("#445163"), spaceAfter=4))
    styles.add(ParagraphStyle(name="AbstractMV", parent=styles["Normal"], fontName="Helvetica", fontSize=9.8, leading=14.2, alignment=TA_JUSTIFY, leftIndent=22, rightIndent=22, spaceAfter=10))
    styles.add(ParagraphStyle(name="BodyMV", parent=styles["Normal"], fontName="Helvetica", fontSize=9.8, leading=14.2, alignment=TA_JUSTIFY, spaceAfter=6))
    styles.add(ParagraphStyle(name="H1MV", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=13.5, leading=17, textColor=colors.HexColor("#145a86"), spaceBefore=5, spaceAfter=3))
    styles.add(ParagraphStyle(name="H2MV", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=10.5, leading=13.5, textColor=colors.HexColor("#18212f"), spaceBefore=7, spaceAfter=3))
    styles.add(ParagraphStyle(name="SmallMV", parent=styles["Normal"], fontName="Helvetica", fontSize=8.2, leading=11.2, textColor=colors.HexColor("#445163"), spaceAfter=5))

    doc = BaseDocTemplate(str(OUT), pagesize=A4, leftMargin=0.78 * inch, rightMargin=0.78 * inch, topMargin=0.72 * inch, bottomMargin=0.78 * inch, title=TITLE, author="Xinmu Ge", subject="Dataset documentation report")
    doc.addPageTemplates([__import__("reportlab.platypus", fromlist=["PageTemplate"]).PageTemplate(id="report", frames=[Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="body")], onPage=page_number)])
    body, h1, h2, small = styles["BodyMV"], styles["H1MV"], styles["H2MV"], styles["SmallMV"]
    story = [Spacer(1, 0.18 * inch), p(TITLE, styles["TitleMV"]), p("Xinmu Ge", styles["AuthorMV"]), p("Shanghai Innovation Institute · Shanghai Jiao Tong University · g3ra1d@sjtu.edu.cn", styles["InstitutionMV"]), p("Independent dataset documentation report · " + REPORT_DATE + " · Related dataset DOI: <link href=\"https://doi.org/10.5281/zenodo.21411214\">" + DATASET_DOI + "</link>", styles["InstitutionMV"]), Spacer(1, 11)]
    story += [p("<b>Abstract.</b> math-vault is a versioned snapshot of public mathematical-reasoning datasets assembled for traceable evaluation. The v0.1.0 dataset release contains 15 evaluation subsets and 32,226 parser-valid rows in a canonical JSONL interface with required <font name=\"Courier\">id</font>, <font name=\"Courier\">problem</font>, and <font name=\"Courier\">answer</font> fields. It maintains source, derived, and canonical layers rather than treating all copies as equivalent. Per-file parent pointers and recorded SHA256 hashes make materialization auditable. Nineteen Omni-MATH rows that the current parser cannot reliably process remain preserved as isolated audit issues and are excluded from the evaluation count. The canonical and DAPO dedup data-materialization scripts use only the Python standard library. Code and documentation are MIT-licensed; each dataset retains its upstream licensing terms.", styles["AbstractMV"])]
    story += [p("1. Purpose and scope", h1), p("Mathematical-reasoning evaluation often combines public datasets whose fields, provenance, and answer conventions differ. math-vault provides a frozen release that makes those distinctions explicit. It does not claim ownership of the upstream data or collapse their licenses into a single data license. Instead, it records snapshots and transformations, then supplies a common evaluation-facing representation for tools that need stable identifiers and gold answers.", body), p("The release is designed to feed math-eval [1] directly. This is an interface relationship: math-vault supplies evaluation rows and provenance, while math-eval provides generation and evaluation machinery. The OPD study [2] documents one downstream use case, and should not be read as an endorsement by any upstream dataset author.", body)]
    facts = [[p("<b>15</b><br/><font size=\"8\">evaluation subsets</font>", small), p("<b>32,226</b><br/><font size=\"8\">parser-valid rows</font>", small), p("<b>19</b><br/><font size=\"8\">isolated audit issues</font>", small)]]
    table = Table(facts, colWidths=[2.0 * inch] * 3, hAlign="CENTER")
    table.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#b6c5d1")), ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#d8e1e8")), ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f4f7fa")), ("ALIGN", (0, 0), (-1, -1), "CENTER"), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("TOPPADDING", (0, 0), (-1, -1), 9), ("BOTTOMPADDING", (0, 0), (-1, -1), 9)]))
    story += [Spacer(1, 5), table, Spacer(1, 8)]
    story += [p("2. Release structure", h1), p("The frozen v0.1.0 dataset release distinguishes three layers. <b>source/</b> contains upstream artifact snapshots and permits only serialization changes that preserve rows, fields, ordering, and content. <b>derived/</b> holds transformations such as filtering, deduplication, prompt removal, or sampling, together with their parents and reconstruction rules. <b>canonical/</b> mechanically materializes data usable by math-eval.", body), p("Every canonical evaluation row has a non-empty unique string identifier, a problem, and an answer. Optional solution, source, and metadata fields are retained when needed for audit. canonical/manifest.json records the source name, parent path, recorded parent SHA256, recorded output SHA256, and row count for each materialized file.", body)]
    subsets = [["Subset family", "Evaluation rows"], ["AIME, AMC, AIMO, BrUMO, CMIMC, HMMT", "403"], ["GSM8K", "8,792"], ["DAPO-Math-17K dedup", "17,176"], ["MATH-500, Minerva-Math", "772"], ["Omni-MATH, OlympiadBench", "5,083"]]
    subset_table = Table([[p("<b>%s</b>" % row[0], small), p("<b>%s</b>" % row[1], small)] for row in subsets], colWidths=[4.25 * inch, 1.65 * inch])
    subset_table.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#c9d4dc")), ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e9f0f5")), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 7), ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
    story += [KeepTogether([subset_table, p("Table 1. Compact grouping of the 15 canonical subsets. The manifest is the authoritative per-file accounting.", small)])]
    story += [p("3. Parser audit boundary", h1), p("The Omni-MATH source snapshot has 4,428 rows. Of these, 4,409 are materialized as evaluation rows. Nineteen records are retained without alteration in canonical/omni_math/issues.jsonl because the current parser cannot reliably process their answers. The recorded categories are nine empty answers, six malformed LaTeX answers, one truncated answer, one unsupported piecewise-text answer, one verification error, and one row with multiple boxed answers. Keeping these rows separate makes the exclusion reviewable rather than silently repairing or discarding source data.", body), p("The release notes an audit baseline in which all 32,226 included canonical answers passed the current math-eval parser’s boxed strict/soft check consistently. That check describes compatibility with a named parser configuration; it is not a claim that every upstream answer is universally unambiguous.", body)]
    story += [p("4. Deterministic materialization", h1), p("The canonical and DAPO dedup data-materialization scripts rely only on the Python standard library. The DAPO dedup script checks expected source and output row counts and identifier uniqueness. The canonical build checks row counts and canonical identifier uniqueness, then records parent and output SHA256 hashes in its manifest. This deliberately narrow implementation keeps the release inspectable: users can compare the manifest against the materialized files and their parents without relying on a hidden service or a third-party build framework.", body), p("For use, consumers can cite the versioned dataset artifact, inspect the relevant source or derived README, and load the canonical JSONL files into math-eval or another evaluator that understands the same fields. Consumers remain responsible for honoring the upstream terms attached to each dataset.", body)]
    story += [p("5. Licensing and provenance", h1), p("Code and documentation in math-vault are released under the MIT License. The datasets are not relicensed: data remains subject to the license or terms documented for each upstream artifact, and an upstream absence of an explicit license is recorded as such rather than interpreted as public-domain permission. This boundary is central to the repository design: a uniform technical interface does not erase provenance or rights information.", body), p("How to cite", h1), p("<b>Dataset documentation report.</b> Xinmu Ge. <i>math-vault: Curated, Traceable Snapshots of Public Mathematical Reasoning Datasets</i>. Independent dataset documentation report, " + REPORT_DATE + ".", body), p("<b>Dataset artifact.</b> Xinmu Ge. <i>math-vault: Curated, Traceable Snapshots of Public Mathematical Reasoning Datasets</i>. Dataset v0.1.0, 2026. Related dataset DOI: <link href=\"https://doi.org/10.5281/zenodo.21411214\">" + DATASET_DOI + "</link>.", body), p("References", h1), p("[1] Xinmu Ge. <i>math-eval: Reproducible Mathematical Reasoning Generation and Evaluation</i>. Software, v0.1.0, 2026. DOI: <link href=\"https://doi.org/10.5281/zenodo.21411208\">10.5281/zenodo.21411208</link>.", body), p("[2] Xinmu Ge et al. <i>Towards Understanding On-Policy Distillation through the Lens of Test-Time Scaling</i>. arXiv:2608.11829, 2026. <link href=\"https://arxiv.org/abs/2608.11829\">https://arxiv.org/abs/2608.11829</link>.", body)]
    doc.build(story)


if __name__ == "__main__":
    build()
