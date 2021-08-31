"""This script returned a parsed quote (body and author) from a PDF file."""
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import random
import subprocess
import os
from typing import List


class PDFIngestor(IngestorInterface):
    """A class to read and parse .pdf files."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """A class method to parse a file."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        temp = f'./tmp{random.randint(0,10000000)}.txt'
        call = subprocess.call(['pdftotext', path, temp], shell=True)

        file_ref = open(temp, encoding='utf-8-sig')
        quotes = []
        for line in file_ref:
            if line.endswith('\n'):
                line = line[:-1]
            parse = line.split(' - ')
            if len(parse) == 2:
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)
        file_ref.close()
        os.remove(temp)

        return quotes

