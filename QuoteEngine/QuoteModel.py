
class QuoteModel:
    """A class keep the body and the author of a quote."""

    def __init__(self, body: str, author: str):
        """Storage in memory body and author of a quote"""
        self.body = body
        self.author = author
