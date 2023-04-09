class TextSplitter:
    """
    A tool for splitting text into smaller chunks.
    """
    def __init__(self):
        """
        Initializes the TextSplitter.
        """
        pass

    def split_text(self, text: str, chunk_size: int) -> list[str]:
        """
        Splits the given text into chunks of the specified size.

        Args:
            text (str): The text to split.
            chunk_size (int): The desired size of each chunk.

        Returns:
            list[str]: A list of text chunks.
        """
        chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
        return chunks