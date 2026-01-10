import os
from pypdf import PdfReader, PdfWriter
from pathlib import Path

def split_pdf(input_pdf_path, pages_per_chunk=10):
    """
    Split a PDF into smaller chunks.

    Args:
        input_pdf_path: Path to the input PDF
        pages_per_chunk: Number of pages per output PDF (default: 10)
    """
    pdf_path = Path(input_pdf_path)
    reader = PdfReader(input_pdf_path)
    total_pages = len(reader.pages)

    print(f"\nProcessing: {pdf_path.name}")
    print(f"Total pages: {total_pages}")

    # Create output directory for chunks
    output_dir = pdf_path.parent / f"{pdf_path.stem}_chunks"
    output_dir.mkdir(exist_ok=True)

    # Split into chunks
    chunk_num = 1
    for start_page in range(0, total_pages, pages_per_chunk):
        end_page = min(start_page + pages_per_chunk, total_pages)

        writer = PdfWriter()
        for page_num in range(start_page, end_page):
            writer.add_page(reader.pages[page_num])

        output_filename = f"{pdf_path.stem}_part{chunk_num:02d}_pages{start_page+1}-{end_page}.pdf"
        output_path = output_dir / output_filename

        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

        print(f"[OK] Created: {output_filename} (pages {start_page+1}-{end_page})")
        chunk_num += 1

    print(f"Output directory: {output_dir}")

def main():
    # Get all PDF files in current directory
    pdf_files = [
        "MISSION DOCUMENT L-OREAL BRANDSTORM 2026 (1).pdf",
        "Fragrance key needs 2021 - Luxury drivers.pdf",
        "CMI DUPES IN FRAGRANCE - SOCIAL LISTENING US FR.pdf",
        "Exception Taskforce Executive Summary 2023.pdf"
    ]

    print("=" * 70)
    print("PDF SPLITTER - Breaking down large PDFs into manageable chunks")
    print("=" * 70)

    for pdf_file in pdf_files:
        if os.path.exists(pdf_file):
            try:
                split_pdf(pdf_file, pages_per_chunk=10)
            except Exception as e:
                print(f"[ERROR] Error processing {pdf_file}: {str(e)}")
        else:
            print(f"\n[WARNING] File not found: {pdf_file}")

    print("\n" + "=" * 70)
    print("[DONE] PDF splitting complete!")
    print("=" * 70)

if __name__ == "__main__":
    main()
