from document_loader import load_document, split_documents

pages = load_document("../data/Uolo V2 Guidelines_Spanish.pdf")

chunks = split_documents(pages)

print(f"\nTotal pages loaded: {len(pages)}")
print(f"Total chunks created: {len(chunks)}")
print("\n--- Chunk Examples ---")
print(chunks[0].page_content[:300]) 
print("\n--- Metadata of first chunk ---")
print(chunks[0].metadata)