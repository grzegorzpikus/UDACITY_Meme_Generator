from .IngestorInterface import IngestorInterface
from .CSVIngestor import CSVIngestor
from .DOCXIngestor import DOCXIngestor
from .TXTIngestor import TXTIngestor
from .PDFInterface import PDFIngestor
from .QuoteModel import QuoteModel
from typing import List


class Ingestor(IngestorInterface):
    """An abstract class to read all all type of files (i.e. csv, docx,
    txt and pdf """
    ingestors = [CSVIngestor, DOCXIngestor, TXTIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)

