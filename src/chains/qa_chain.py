from src.chains.base_chain import Chain
from src.llm_api.llm_api import LLMApi

class QuestionAnsweringChain(Chain):
    def __init__(self, llm: LLMApi):
        super().__init__(llm)
        self.prompt = (
            """Use the following pieces of context to answer the question at the end. "
            "If you don't know the answer, just say that you don't know, don't try to make up an answer.\n\n"
            "{context}\n\nQuestion: {question}\nHelpful Answer:"""
        )

    def run(self, question: str, context: str) -> str:
        prompt_template = self.prompt.format(context=context, question=question)
        return self.llm.generate_text(prompt_template)