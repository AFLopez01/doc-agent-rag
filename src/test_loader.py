from document_loader import load_document

pages = load_document("../data/Uolo V2 Guidelines_Spanish.pdf")

# Print the first Document

print(pages[0].page_content[:300]) # Print the first 300 characters of the first page's content
print("---")
print(pages[0].metadata) # Print the metadata of the first page