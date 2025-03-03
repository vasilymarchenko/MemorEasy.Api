import uuid
from datetime import datetime
from typing import Optional, List, Dict  # Added Dict import
from .models import Translation, PagedResult

class WordService:
    def __init__(self):
        self._translations: Dict[str, Translation] = {}

    def get_translation(self, id: str) -> Optional[Translation]:
        return self._translations.get(id)

    def create_translation(self, word: str, translation: str) -> Translation:
        new_translation = Translation(
            id=str(uuid.uuid4()),
            word=word,
            translation=translation,
            created_at=datetime.utcnow()
        )
        self._translations[new_translation.id] = new_translation
        return new_translation

    def delete_translation(self, id: str) -> bool:
        if id in self._translations:
            del self._translations[id]
            return True
        return False

    def get_translations(self, page: int = 1, page_size: int = 20, search: Optional[str] = None) -> PagedResult:
        filtered_translations = list(self._translations.values())

        if search:
            search = search.lower()
            filtered_translations = [
                t for t in filtered_translations 
                if search in t.word.lower() or search in t.translation.lower()
            ]

        total_count = len(filtered_translations)

        # Sort by created_at
        filtered_translations.sort(key=lambda x: x.created_at, reverse=True)

        # Apply pagination
        start_idx = (page - 1) * page_size
        end_idx = start_idx + page_size

        paginated_items = filtered_translations[start_idx:end_idx]

        return PagedResult(
            items=paginated_items,
            total_count=total_count,
            page=page,
            page_size=page_size
        )

# Global instance for all functions to use
word_service = WordService()