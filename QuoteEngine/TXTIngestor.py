"""This script returned a parsed quote (body and author) from a TXT file."""
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List


class TXTIngestor(IngestorInterface):
    """A class to read and parse .txt files."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """a class method to parse a file."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        file = open(path, encoding='utf-8-sig')
        for line in file:
            if line.endswith('\n'):
                line = line[:-1]
            parse = line.split(' - ')
            new_quote = QuoteModel(parse[0], parse[1])
            quotes.append(new_quote)

        return quotes
