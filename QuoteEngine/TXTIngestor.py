from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List


class TXTIngestor(IngestorInterface):
    """An abstract class to read .txt files"""
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
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
