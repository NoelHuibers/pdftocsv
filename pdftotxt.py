import pathlib, fitz
with fitz.open("chronik.pdf") as doc:  # open document
    text = chr(12).join([page.get_text() for page in doc])
# write as a binary file to support non-ASCII characters
pathlib.Path("people" + ".txt").write_bytes(text.encode())