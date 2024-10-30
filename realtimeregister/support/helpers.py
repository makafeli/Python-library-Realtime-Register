from typing import Any, Dict, Optional
from datetime import datetime

def format_date(date: Optional[datetime]) -> Optional[str]:
    """Format datetime object to ISO 8601 string"""
    return date.isoformat() if date else None

def parse_date(date_str: Optional[str]) -> Optional[datetime]:
    """Parse ISO 8601 string to datetime object"""
    return datetime.fromisoformat(date_str) if date_str else None

def clean_dict(data: Dict[str, Any]) -> Dict[str, Any]:
    """Remove None values from dictionary"""
    return {k: v for k, v in data.items() if v is not None}

def validate_required(data: Dict[str, Any], required: list) -> None:
    """Validate required fields in dictionary"""
    missing = [field for field in required if field not in data]
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")

def validate_enum(value: str, enum_class: Any) -> None:
    """Validate enum value"""
    if not any(value == item.value for item in enum_class):
        valid_values = [item.value for item in enum_class]
        raise ValueError(f"Invalid value: {value}. Must be one of: {', '.join(valid_values)}")

def validate_type(value: Any, expected_type: type, field_name: str) -> None:
    """Validate value type"""
    if not isinstance(value, expected_type):
        raise TypeError(f"Invalid type for {field_name}. Expected {expected_type.__name__}, got {type(value).__name__}")