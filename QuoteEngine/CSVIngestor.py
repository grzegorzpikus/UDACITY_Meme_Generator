from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
import pandas


class CSVIngestor(IngestorInterface):
    """An abstract class to read .csv files"""
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        file = pandas.read_csv(path, header=0)
        for index, row in file.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes
