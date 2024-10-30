import time
from typing import Optional
from datetime import datetime, timedelta

class RateLimiter:
    """Rate limiting utility for API requests"""
    
    def __init__(self, requests_per_second: int = 10):
        self.requests_per_second = requests_per_second
        self.requests = []
        
    def wait(self) -> None:
        """Wait if necessary to respect rate limits"""
        now = datetime.utcnow()
        
        # Remove requests older than 1 second
        self.requests = [
            req_time for req_time in self.requests
            if now - req_time < timedelta(seconds=1)
        ]
        
        # If at limit, wait until oldest request is more than 1 second old
        if len(self.requests) >= self.requests_per_second:
            sleep_time = 1 - (now - self.requests[0]).total_seconds()
            if sleep_time > 0:
                time.sleep(sleep_time)
        
        # Add current request
        self.requests.append(now)
    
    def get_remaining_requests(self) -> int:
        """Get number of remaining requests in current window"""
        self.wait()  # Clean up old requests
        return self.requests_per_second - len(self.requests)
    
    def reset_in(self) -> Optional[float]:
        """Get seconds until rate limit resets"""
        if not self.requests:
            return None
        
        now = datetime.utcnow()
        oldest_request = self.requests[0]
        return max(0, 1 - (now - oldest_request).total_seconds())