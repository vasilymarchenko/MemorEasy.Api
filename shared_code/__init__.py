"""
This module provides shared code for the Azure Functions word translation service.
It includes models and services for managing word translations.
"""

from .models import Translation, PagedResult
from .word_service import WordService, word_service

__all__ = [
    'Translation',
    'PagedResult',
    'WordService',
    'word_service'
]
