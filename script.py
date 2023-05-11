import os
import fitz

pdf_documents = pdf_documents = ["example.pdf", "example2.pdf", "example3.pdf"] #YOUR PDF HERE!!!!

for pdf_document in pdf_documents:
    document = fitz.open(pdf_document)
    output_file = os.path.splitext(pdf_document)[0] + ".txt"
    with open(output_file, "wb") as out:
        for page in document:
            text = page.get_text().encode("utf8")
            out.write(text)
            out.write(b"\n----\n")
    document.close()

print("Files converted successfully!!!!")
