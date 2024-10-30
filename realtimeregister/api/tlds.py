from typing import Dict, Any, List, Optional
from ..models.tld import TLD

class TLDsApi:
    def __init__(self, client):
        self.client = client

    def list(self, page: int = 1, limit: int = 25) -> Dict[str, Any]:
        """List TLDs"""
        return self.client._request('GET', 'tlds', params={'page': page, 'limit': limit})

    def get(self, name: str) -> TLD:
        """Get TLD details"""
        response = self.client._request('GET', f'tlds/{name}')
        return TLD.from_dict(response)

    def query(
        self,
        query: str,
        idn_script: Optional[str] = None,
        status: Optional[str] = None,
        page: int = 1,
        limit: int = 25
    ) -> Dict[str, Any]:
        """Search TLDs"""
        params = {
            'q': query,
            'page': page,
            'limit': limit
        }
        if idn_script:
            params['idnScript'] = idn_script
        if status:
            params['status'] = status
            
        return self.client._request('GET', 'tlds/query', params=params)