from langchain.tools import DuckDuckGoSearchRun


class SearchTool:
    def __init__(self):
        self.search = DuckDuckGoSearchRun()

    def use(self, query: str) -> str:
        """Uses the DuckDuckGo search engine to find relevant information."""
        return self.search.run(query)