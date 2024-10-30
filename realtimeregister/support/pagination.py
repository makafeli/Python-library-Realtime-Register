from typing import Dict, Any, Optional, TypeVar, Generic, List
from dataclasses import dataclass

T = TypeVar('T')

@dataclass
class PaginatedResponse(Generic[T]):
    """Generic paginated response container"""
    items: List[T]
    total: int
    page: int
    limit: int
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any], item_key: str, item_class: Any) -> 'PaginatedResponse[T]':
        """Create PaginatedResponse from API response"""
        return cls(
            items=[item_class.from_dict(item) for item in data[item_key]],
            total=data['total'],
            page=data['page'],
            limit=data['limit']
        )

    def has_next_page(self) -> bool:
        """Check if there is a next page"""
        return self.page * self.limit < self.total

    def has_previous_page(self) -> bool:
        """Check if there is a previous page"""
        return self.page > 1

    def next_page_number(self) -> Optional[int]:
        """Get next page number if available"""
        return self.page + 1 if self.has_next_page() else None

    def previous_page_number(self) -> Optional[int]:
        """Get previous page number if available"""
        return self.page - 1 if self.has_previous_page() else None