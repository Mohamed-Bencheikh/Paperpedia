from pydantic import BaseModel
from typing import List, Optional

class PaperBasic(BaseModel):
    """Basic information about a paper."""
    title: str
    authors: List[str]
    date: Optional[str]
    url: str
    categories: List[str]

class PaperDetailed(PaperBasic):
    """Detailed information about a paper."""
    abstract: Optional[str]
    id: Optional[str]
    links: Optional[List[str]]
    doi: Optional[str]
    journal: Optional[str]
    comment: Optional[str]
