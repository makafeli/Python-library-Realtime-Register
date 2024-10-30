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
        # Try to list domains (a simple operation to test connectivity)
        response = client.domains.list()
        print("✓ Successfully connected to Realtime Register OTE API")
        print(f"Total domains: {response.get('total', 0)}")
        
        # Let's also try to get some TLD information
        tlds = client.tlds.list()
        print(f"Available TLDs: {tlds.get('total', 0)}")
        
        return True
        
    except RealtimeRegisterException as e:
        print(f"✗ API Error: {str(e)}")
        return False
    except Exception as e:
        print(f"✗ Unexpected error: {str(e)}")
        return False

if __name__ == "__main__":
    test_api_connection()