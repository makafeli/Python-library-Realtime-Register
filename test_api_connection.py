from realtimeregister import Client
from realtimeregister.exceptions import RealtimeRegisterException

def test_api_connection():
    # Initialize the client with test credentials
    client = Client(
        customer="allachtoon-ote",
        api_key="YWxsYWNodG9vbi1vdGUva2V2aW46EiuoKfaPcnU4VibgMq0HRC8KjdanEFCkwzYA7jnJLfQ=",
        test_mode=True  # This ensures we're using the OTE environment
    )

    try:
        # Test various API endpoints
        print("\nTesting API Connection...")
        
        # 1. List domains
        domains = client.domains.list()
        print(f"✓ Domains API: Found {domains.get('total', 0)} domains")
        
        # 2. List TLDs
        tlds = client.tlds.list()
        print(f"✓ TLDs API: Found {tlds.get('total', 0)} TLDs")
        
        # 3. Get balance (if available)
        try:
            balance = client.reseller.get_balance()
            print(f"✓ Reseller API: Balance {balance.get('balance', 0)} {balance.get('currency', 'EUR')}")
        except RealtimeRegisterException:
            print("ℹ Reseller API: Balance check skipped (not available)")
        
        # 4. List certificates
        certificates = client.certificates.list()
        print(f"✓ Certificates API: Found {certificates.get('total', 0)} certificates")
        
        # 5. List contacts
        contacts = client.contacts.list()
        print(f"✓ Contacts API: Found {contacts.get('total', 0)} contacts")
        
        print("\n✓ Successfully connected to Realtime Register OTE API")
        return True
        
    except RealtimeRegisterException as e:
        print(f"\n✗ API Error: {str(e)}")
        return False
    except Exception as e:
        print(f"\n✗ Unexpected error: {str(e)}")
        return False

if __name__ == "__main__":
    test_api_connection()