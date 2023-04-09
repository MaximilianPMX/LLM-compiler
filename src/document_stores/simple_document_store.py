class SimpleDocumentStore:
    """
    A simple in-memory document store.
    """
    def __init__(self):
        """
        Initializes the SimpleDocumentStore.
        """
        self.documents = {}

    def add_document(self, document_id: str, document: str) -> None:
        """
        Adds a document to the store.

        Args:
            document_id (str): The ID of the document.
            document (str): The content of the document.
        """
        self.documents[document_id] = document

    def get_document(self, document_id: str) -> str:
        """
        Retrieves a document from the store.

        Args:
            document_id (str): The ID of the document to retrieve.

        Returns:
            str: The content of the document, or None if the document is not found.
        """
        return self.documents.get(document_id)