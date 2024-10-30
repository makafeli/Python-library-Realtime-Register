from typing import Dict, Any, List, Optional
from ..models.domain import Domain

class DomainsApi:
    def __init__(self, client):
        self.client = client

    def list(self, page: int = 1, limit: int = 25) -> Dict[str, Any]:
        """List domains"""
        return self.client._request('GET', 'domains', params={'page': page, 'limit': limit})

    def get(self, domain: str) -> Domain:
        """Get domain details"""
        response = self.client._request('GET', f'domains/{domain}')
        return Domain.from_dict(response)

    def check(self, domain: str) -> Dict[str, Any]:
        """Check domain availability"""
        return self.client._request('GET', f'domains/{domain}/check')

    def register(
        self,
        domain: str,
        registrant: Dict[str, Any],
        period: int = 1,
        nameservers: Optional[List[Dict[str, Any]]] = None,
        tech_contact: Optional[Dict[str, Any]] = None,
        admin_contact: Optional[Dict[str, Any]] = None,
        billing_contact: Optional[Dict[str, Any]] = None,
        auth_code: Optional[str] = None,
        properties: Optional[Dict[str, Any]] = None
    ) -> Domain:
        """Register a domain"""
        data = {
            'registrant': registrant,
            'period': period
        }

        if nameservers:
            data['nameservers'] = nameservers
        if tech_contact:
            data['techContact'] = tech_contact
        if admin_contact:
            data['adminContact'] = admin_contact
        if billing_contact:
            data['billingContact'] = billing_contact
        if auth_code:
            data['authCode'] = auth_code
        if properties:
            data['properties'] = properties

        response = self.client._request('POST', f'domains/{domain}', data=data)
        return Domain.from_dict(response)

    def update(
        self,
        domain: str,
        nameservers: Optional[List[Dict[str, Any]]] = None,
        tech_contact: Optional[Dict[str, Any]] = None,
        admin_contact: Optional[Dict[str, Any]] = None,
        billing_contact: Optional[Dict[str, Any]] = None,
        auth_code: Optional[str] = None,
        properties: Optional[Dict[str, Any]] = None
    ) -> Domain:
        """Update domain details"""
        data = {}
        if nameservers:
            data['nameservers'] = nameservers
        if tech_contact:
            data['techContact'] = tech_contact
        if admin_contact:
            data['adminContact'] = admin_contact
        if billing_contact:
            data['billingContact'] = billing_contact
        if auth_code:
            data['authCode'] = auth_code
        if properties:
            data['properties'] = properties

        response = self.client._request('PUT', f'domains/{domain}', data=data)
        return Domain.from_dict(response)

    def delete(self, domain: str) -> None:
        """Delete a domain"""
        self.client._request('DELETE', f'domains/{domain}')

    def renew(
        self,
        domain: str,
        period: int = 1,
        properties: Optional[Dict[str, Any]] = None
    ) -> Domain:
        """Renew a domain"""
        data = {'period': period}
        if properties:
            data['properties'] = properties

        response = self.client._request('POST', f'domains/{domain}/renew', data=data)
        return Domain.from_dict(response)

    def restore(
        self,
        domain: str,
        properties: Optional[Dict[str, Any]] = None
    ) -> Domain:
        """Restore a domain"""
        data = {}
        if properties:
            data['properties'] = properties

        response = self.client._request('POST', f'domains/{domain}/restore', data=data)
        return Domain.from_dict(response)

    def query(
        self,
        query: str,
        status: Optional[str] = None,
        registrar: Optional[str] = None,
        page: int = 1,
        limit: int = 25
    ) -> Dict[str, Any]:
        """Search domains"""
        params = {
            'q': query,
            'page': page,
            'limit': limit
        }
        if status:
            params['status'] = status
        if registrar:
            params['registrar'] = registrar
            
        return self.client._request('GET', 'domains/query', params=params)

    def update_registrant(
        self,
        domain: str,
        registrant: Dict[str, Any],
        properties: Optional[Dict[str, Any]] = None
    ) -> Domain:
        """Update domain registrant"""
        data = {'registrant': registrant}
        if properties:
            data['properties'] = properties

        response = self.client._request('PUT', f'domains/{domain}/registrant', data=data)
        return Domain.from_dict(response)