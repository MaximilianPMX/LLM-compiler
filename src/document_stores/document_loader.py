class DocumentLoader:
    """
    A class for loading documents from various sources.
    """
    def __init__(self):
        """
        Initializes the DocumentLoader.
        """
        pass

    def load_document(self, file_path: str) -> str:
        """
        Loads a document from a file.

        Args:
            file_path (str): The path to the document file.

        Returns:
            str: The content of the document, or an empty string if loading fails.
        """
        try:
            with open(file_path, 'r') as f:
                document = f.read()
            return document
        except FileNotFoundError:
            print(f"Error: Document file not found at {file_path}")
            return ""
