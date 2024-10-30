import logging
from typing import Any, Optional
from datetime import datetime

class Logger:
    """Logging utility for SDK operations"""
    
    def __init__(self, name: str = "realtimeregister", level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
    
    def debug(self, message: str, **kwargs: Any) -> None:
        """Log debug message"""
        self.logger.debug(message, extra=kwargs)
    
    def info(self, message: str, **kwargs: Any) -> None:
        """Log info message"""
        self.logger.info(message, extra=kwargs)
    
    def warning(self, message: str, **kwargs: Any) -> None:
        """Log warning message"""
        self.logger.warning(message, extra=kwargs)
    
    def error(self, message: str, **kwargs: Any) -> None:
        """Log error message"""
        self.logger.error(message, extra=kwargs)
    
    def critical(self, message: str, **kwargs: Any) -> None:
        """Log critical message"""
        self.logger.critical(message, extra=kwargs)
    
    def log_request(
        self,
        method: str,
        url: str,
        data: Optional[dict] = None,
        params: Optional[dict] = None
    ) -> None:
        """Log API request"""
        self.debug(
            f"API Request: {method} {url}",
            data=data,
            params=params,
            timestamp=datetime.utcnow().isoformat()
        )
    
    def log_response(
        self,
        status_code: int,
        response_data: Any,
        elapsed: float
    ) -> None:
        """Log API response"""
        self.debug(
            f"API Response: {status_code}",
            data=response_data,
            elapsed=elapsed,
            timestamp=datetime.utcnow().isoformat()
        )