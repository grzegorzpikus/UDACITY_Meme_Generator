from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """An abstract class to read files"""
    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """a class method to check if a file can be parsed"""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    #@abstractmethod
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """a class method to parse a file"""
        pass
