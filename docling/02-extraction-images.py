import os

from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling_core.types.doc import PictureItem

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
pdf_path = os.path.join(script_dir, "Docling_Technical_Report.pdf")
images_dir = os.path.join(script_dir, "images")

pipeline_options = PdfPipelineOptions()
pipeline_options.images_scale = 2.0
pipeline_options.generate_picture_images = True

converter = DocumentConverter(
    format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)}
)

result = converter.convert(pdf_path)

os.makedirs(images_dir, exist_ok=True)

picture_counter = 0
for element, _level in result.document.iterate_items():
    if isinstance(element, PictureItem):
        picture_counter += 1
        image_path = os.path.join(images_dir, f"picture_{picture_counter}.png")
        with open(image_path, "wb") as fp:
            element.get_image(result.document).save(fp, "PNG")

document = result.document
markdown_output = document.export_to_markdown()
print(markdown_output)
