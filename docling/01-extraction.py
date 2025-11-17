import os

from docling.document_converter import DocumentConverter

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
pdf_path = os.path.join(script_dir, "Docling_Technical_Report.pdf")
converter = DocumentConverter()

# result = converter.convert(pdf_path)
# result = converter.convert("https://arxiv.org/html/2408.09869v1")
result = converter.convert("https://github.com/docling-project/docling")

document = result.document
markdown_output = document.export_to_markdown()

print(markdown_output)