from typing import List


def split_text(text: str, chunk_size: int, chunk_overlap: int = 0) -> List[str]:
    """Splits a long text into smaller chunks.

    Args:
        text: The input text.
        chunk_size: The maximum size of each chunk.
        chunk_overlap: The number of overlapping characters between chunks.

    Returns:
        A list of text chunks.
    """
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        start += chunk_size - chunk_overlap
    return chunks