from src.document_stores.document_loader import DocumentLoader

def test_document_loader_load_document():
    # Create a dummy text file for testing.
    with open("test_document.txt", "w") as f:
        f.write("This is a test document.\nIt has two lines.")

    loader = DocumentLoader()
    documents = loader.load_document("test_document.txt")

    assert len(documents) == 1
    assert documents[0].page_content == "This is a test document.\nIt has two lines."

    # Clean up the dummy file.
    import os
    os.remove("test_document.txt")