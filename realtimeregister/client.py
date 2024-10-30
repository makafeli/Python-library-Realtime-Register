import requests
from datetime import datetime
from typing import Dict, Any, Optional
from .exceptions import (
    RealtimeRegisterException,
    ValidationException,
    AuthenticationException,
    NotFoundException
)
from .api import (
    DomainsApi,
    ContactsApi,
    BrandsApi,
    CustomersApi,
    ProvidersApi,
    DNSApi,
    CertificatesApi,
    BillingApi,
    TemplatesApi,
    NotificationsApi,
    AbuseApi,
    ProcessesApi,
    StatisticsApi,
    TLDsApi,
    ResellerApi,
    TransfersApi
)

class Client:
    def __init__(
        self,
        customer: str,
        api_key: str,
        test_mode: bool = False,
        timeout: int = 30
    ):
        self.customer = customer
        self.api_key = api_key
        self.test_mode = test_mode
        self.timeout = timeout
        self.base_url = "https://api.realtimeregister.com/v2"
        if test_mode:
            self.base_url = "https://api.test.realtimeregister.com/v2"

        # Initialize API endpoints
        self.domains = DomainsApi(self)
        self.contacts = ContactsApi(self)
        self.brands = BrandsApi(self)
        self.customers = CustomersApi(self)
        self.providers = ProvidersApi(self)
        self.dns = DNSApi(self)
        self.certificates = CertificatesApi(self)
        self.billing = BillingApi(self)
        self.templates = TemplatesApi(self)
        self.notifications = NotificationsApi(self)
        self.abuse = AbuseApi(self)
        self.processes = ProcessesApi(self)
        self.statistics = StatisticsApi(self)
        self.tlds = TLDsApi(self)
        self.reseller = ResellerApi(self)
        self.transfers = TransfersApi(self)
        
    def _request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict] = None,
        data: Optional[Dict] = None
    ) -> Dict[str, Any]:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "X-Customer": self.customer
        }
        
        url = f"{self.base_url}/{endpoint}"
        
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                json=data,
                timeout=self.timeout
            )
            
            if response.status_code == 404:
                raise NotFoundException(f"Resource not found: {endpoint}")
            elif response.status_code == 401:
                raise AuthenticationException("Invalid authentication credentials")
            elif response.status_code == 400:
                raise ValidationException(response.json().get("message", "Validation error"))
            elif response.status_code >= 500:
                raise RealtimeRegisterException("Server error occurred")
                
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            raise RealtimeRegisterException(f"Request failed: {str(e)}")