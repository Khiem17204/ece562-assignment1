import argparse
import os
import subprocess

try:
    from PyPDF2 import PdfMerger
    MERGE = True
except ImportError:
    print("Could not find PyPDF2. Leaving pdf files unmerged.")
    MERGE = False


def main(files):
    pdfs = []

    for f in files:
        print(f"Converting {f} to PDF...")
        cmd = [
            "jupyter",
            "nbconvert",
            "--log-level", "CRITICAL",
            "--to", "pdf",
            f,
        ]
        result = subprocess.run(cmd)
        if result.returncode == 0:
            pdf_name = os.path.splitext(f)[0] + ".pdf"
            pdfs.append(pdf_name)
            print(f"Created {pdf_name}")
        else:
            print(f"⚠️ Failed to create PDF for {f}")

    if MERGE and pdfs:
        print("Merging PDFs into assignment.pdf...")
        merger = PdfMerger()
        for pdf in pdfs:
            if os.path.exists(pdf):
                merger.append(pdf)
        merger.write("assignment.pdf")
        merger.close()
        print("✅ Created assignment.pdf")

        # Remove individual PDFs (optional)
        for pdf in pdfs:
            os.remove(pdf)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--notebooks", type=str, nargs="+", required=True)
    args = parser.parse_args()
    main(args.notebooks)
import argparse
import os
import subprocess

try:
    from PyPDF2 import PdfMerger
    MERGE = True
except ImportError:
    print("Could not find PyPDF2. Leaving pdf files unmerged.")
    MERGE = False


def main(files):
    pdfs = []

    for f in files:
        print(f"Converting {f} to PDF...")
        cmd = [
            "jupyter",
            "nbconvert",
            "--log-level", "CRITICAL",
            "--to", "pdf",
            f,
        ]
        result = subprocess.run(cmd)
        if result.returncode == 0:
            pdf_name = os.path.splitext(f)[0] + ".pdf"
            pdfs.append(pdf_name)
            print(f"Created {pdf_name}")
        else:
            print(f"⚠️ Failed to create PDF for {f}")

    if MERGE and pdfs:
        print("Merging PDFs into assignment.pdf...")
        merger = PdfMerger()
        for pdf in pdfs:
            if os.path.exists(pdf):
                merger.append(pdf)
        merger.write("assignment.pdf")
        merger.close()
        print("✅ Created assignment.pdf")

        # Remove individual PDFs (optional)
        for pdf in pdfs:
            os.remove(pdf)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--notebooks", type=str, nargs="+", required=True)
    args = parser.parse_args()
    main(args.notebooks)
