"""This script returned a parsed quote (body and author) from a CSV file."""
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
import pandas as pd


class CSVIngestor(IngestorInterface):
    """A class to read and parse .csv files."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """a class method to parse a file."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        file = pd.read_csv(path, header=0)
        for index, row in file.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes
