# src/document_stores/simple_document_store.py

class SimpleDocumentStore:
    def __init__(self):
        self.documents = {}

    def add_document(self, doc_id, document):
        self.documents[doc_id] = document

    def get_document(self, doc_id):
        return self.documents.get(doc_id)