from typing import Any, Dict, List, Optional, Type, Union
from datetime import datetime
from ..exceptions import ValidationException

class Validator:
    """Data validation utility"""
    
    @staticmethod
    def validate_string(value: Any, field: str, min_length: Optional[int] = None, max_length: Optional[int] = None) -> None:
        """Validate string field"""
        if not isinstance(value, str):
            raise ValidationException(f"{field} must be a string")
            
        if min_length and len(value) < min_length:
            raise ValidationException(f"{field} must be at least {min_length} characters long")
            
        if max_length and len(value) > max_length:
            raise ValidationException(f"{field} must be at most {max_length} characters long")

    @staticmethod
    def validate_integer(value: Any, field: str, min_value: Optional[int] = None, max_value: Optional[int] = None) -> None:
        """Validate integer field"""
        if not isinstance(value, int):
            raise ValidationException(f"{field} must be an integer")
            
        if min_value is not None and value < min_value:
            raise ValidationException(f"{field} must be greater than or equal to {min_value}")
            
        if max_value is not None and value > max_value:
            raise ValidationException(f"{field} must be less than or equal to {max_value}")

    @staticmethod
    def validate_float(value: Any, field: str, min_value: Optional[float] = None, max_value: Optional[float] = None) -> None:
        """Validate float field"""
        if not isinstance(value, (int, float)):
            raise ValidationException(f"{field} must be a number")
            
        if min_value is not None and value < min_value:
            raise ValidationException(f"{field} must be greater than or equal to {min_value}")
            
        if max_value is not None and value > max_value:
            raise ValidationException(f"{field} must be less than or equal to {max_value}")

    @staticmethod
    def validate_boolean(value: Any, field: str) -> None:
        """Validate boolean field"""
        if not isinstance(value, bool):
            raise ValidationException(f"{field} must be a boolean")

    @staticmethod
    def validate_datetime(value: Any, field: str) -> None:
        """Validate datetime field"""
        if not isinstance(value, datetime):
            raise ValidationException(f"{field} must be a datetime object")

    @staticmethod
    def validate_list(value: Any, field: str, item_type: Optional[Type] = None) -> None:
        """Validate list field"""
        if not isinstance(value, list):
            raise ValidationException(f"{field} must be a list")
            
        if item_type:
            for item in value:
                if not isinstance(item, item_type):
                    raise ValidationException(f"All items in {field} must be of type {item_type.__name__}")

    @staticmethod
    def validate_dict(value: Any, field: str, required_keys: Optional[List[str]] = None) -> None:
        """Validate dictionary field"""
        if not isinstance(value, dict):
            raise ValidationException(f"{field} must be a dictionary")
            
        if required_keys:
            missing_keys = [key for key in required_keys if key not in value]
            if missing_keys:
                raise ValidationException(f"Missing required keys in {field}: {', '.join(missing_keys)}")

    @staticmethod
    def validate_email(value: str, field: str) -> None:
        """Validate email address"""
        if '@' not in value or '.' not in value:
            raise ValidationException(f"Invalid email address: {value}")

    @staticmethod
    def validate_phone(value: str, field: str) -> None:
        """Validate phone number"""
        if not value.replace('+', '').replace('-', '').replace(' ', '').isdigit():
            raise ValidationException(f"Invalid phone number: {value}")

    @staticmethod
    def validate_domain(value: str, field: str) -> None:
        """Validate domain name"""
        if not all(part and all(c.isalnum() or c in '-.' for c in part) 
                  for part in value.split('.')):
            raise ValidationException(f"Invalid domain name: {value}")

    @staticmethod
    def validate_url(value: str, field: str) -> None:
        """Validate URL"""
        if not value.startswith(('http://', 'https://')):
            raise ValidationException(f"Invalid URL: {value}. Must start with http:// or https://")