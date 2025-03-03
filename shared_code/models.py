from dataclasses import dataclass
from typing import Optional, List, Dict
from datetime import datetime

@dataclass
class Translation:
    id: str
    word: str
    translation: str
    created_at: datetime

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "word": self.word,
            "translation": self.translation,
            "created_at": self.created_at.isoformat()
        }

@dataclass
class PagedResult:
    items: List[Translation]
    total_count: int
    page: int
    page_size: int

    def to_dict(self) -> Dict:
        return {
            "items": [item.to_dict() for item in self.items],
            "total_count": self.total_count,
            "page": self.page,
            "page_size": self.page_size
        }
