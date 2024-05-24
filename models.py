from pydantic import BaseModel
from typing import List, Optional

class PaperBasic(BaseModel):
    """Basic information about a paper."""
    title: str
    authors: List[str]
    publication_date: Optional[str]
    id: str
    url: str
    categories: List[str]

class PaperDetailed(PaperBasic):
    """Detailed information about a paper."""
    abstract: Optional[str]
    keywords: Optional[List[str]]
    citation_count: Optional[int]
    doi: Optional[str]
    journal: str
    references: Optional[List[str]]
