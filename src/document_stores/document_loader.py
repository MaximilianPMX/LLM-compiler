class DocumentLoader:
    def load_document(self, source: str) -> str:
        """Loads a document from a specified source (file or URL)."""
        try:
            # Check if the source is a file path
            with open(source, 'r') as f:
                return f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {source}")
        except Exception as e:
            raise Exception(f"Error loading document from {source}: {e}")


if __name__ == '__main__':
    # Example Usage, create a dummy file
    with open('test.txt', 'w') as f:
        f.write('This is a test document.\nIt has multiple lines.')

    loader = DocumentLoader()
    try:
        content = loader.load_document('test.txt')
        print(content)

        # Example of handling file not found
        # content = loader.load_document('non_existent_file.txt')
        # print(content)
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")