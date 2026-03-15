#!/usr/bin/env python3
"""
Generate Markdown documentation for MIECO ontology terms using ROBOT.

Uses `robot export` to produce a TSV of all MIECO-specific terms and
converts it into a Markdown page that MkDocs can include in the website.

Usage (with a downloaded robot.jar):
    python3 src/scripts/generate_ontology_docs.py --robot-jar /path/to/robot.jar

Usage (with `robot` already on PATH, e.g. inside the ODK Docker container):
    python3 src/scripts/generate_ontology_docs.py
"""

import argparse
import csv
import io
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
OWL_FILE = REPO_ROOT / "src" / "ontology" / "mieco-edit.owl"
CATALOG = REPO_ROOT / "src" / "ontology" / "catalog-v001.xml"
DEFAULT_OUT = REPO_ROOT / "docs_src" / "ontology-terms.md"

MIECO_PREFIX = "MIECO: http://metabolomicssociety.org/ontologies/MIECO#MIECO_"
EXPORT_HEADERS = "ID|LABEL|IAO:0000115|rdfs:comment"


def build_robot_cmd(robot_jar: str | None) -> list[str]:
    """Return the base robot command (either `java -jar ...` or `robot`)."""
    if robot_jar:
        return ["java", "-jar", robot_jar]
    return ["robot"]


def run_robot_export(robot_jar: str | None) -> str:
    """Run ROBOT export and return TSV content."""
    cmd = build_robot_cmd(robot_jar)
    with tempfile.NamedTemporaryFile(suffix=".tsv", delete=False) as tmp:
        tmp_path = tmp.name

    try:
        result = subprocess.run(
            cmd + [
                "export",
                "--catalog", str(CATALOG),
                "--input", str(OWL_FILE),
                "--prefix", MIECO_PREFIX,
                "--header", EXPORT_HEADERS,
                "--format", "tsv",
                "--export", tmp_path,
            ],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            print(
                f"ROBOT export failed on {OWL_FILE}:\n{result.stderr}",
                file=sys.stderr,
            )
            sys.exit(1)

        return Path(tmp_path).read_text(encoding="utf-8")
    finally:
        Path(tmp_path).unlink(missing_ok=True)


def tsv_to_markdown(tsv_content: str) -> str:
    """Convert ROBOT TSV export to Markdown, filtering to MIECO terms only."""
    reader = csv.reader(io.StringIO(tsv_content), delimiter="\t")
    rows = list(reader)

    # Filter: keep only MIECO-namespace rows
    mieco_rows = [r for r in rows[1:] if r and r[0].startswith("MIECO:")]

    col_headers = ["ID", "Label", "Definition (IAO:0000115)", "Comment"]

    lines = [
        "# MIECO Ontology Terms",
        "",
        "This page lists all terms defined in the **Metabolite Identification Evidence"
        " Code Ontology (MIECO)**.",
        "Documentation is generated automatically from"
        " `src/ontology/mieco-edit.owl` using"
        " [ROBOT](http://robot.obolibrary.org/).",
        "",
        "## Term List",
        "",
        "| " + " | ".join(col_headers) + " |",
        "|" + "|".join(["---"] * len(col_headers)) + "|",
    ]

    for row in mieco_rows:
        # Pad short rows
        while len(row) < len(col_headers):
            row.append("")
        # Sanitise Markdown table cell content
        cells = [
            cell.strip()
                .replace("|", "\\|")
                .replace("\n", " ")
            for cell in row[: len(col_headers)]
        ]
        lines.append("| " + " | ".join(cells) + " |")

    lines += [
        "",
        f"*{len(mieco_rows)} terms listed.*",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate Markdown docs for MIECO ontology terms via ROBOT."
    )
    parser.add_argument(
        "--robot-jar",
        default=None,
        help="Path to robot.jar (uses `robot` on PATH when omitted).",
    )
    parser.add_argument(
        "--output",
        default=str(DEFAULT_OUT),
        help=f"Output Markdown file (default: {DEFAULT_OUT}).",
    )
    args = parser.parse_args()

    print(f"Running ROBOT export on {OWL_FILE} …", file=sys.stderr)
    tsv = run_robot_export(args.robot_jar)

    markdown = tsv_to_markdown(tsv)

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(markdown, encoding="utf-8")
    print(f"Wrote {out}", file=sys.stderr)


if __name__ == "__main__":
    main()
