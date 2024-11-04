from realtimeregister import Client
from realtimeregister.exceptions import (
    RealtimeRegisterException,
    AuthenticationException,
    ValidationException,
    NotFoundException
)


def test_api_connection():
    """Test connection to Realtime Register API with proper error handling"""
    try:
        # Initialize the client with test credentials
        client = Client(
            api_key="YWxsYWNodG9vbi1vdGUva2V2aW46EiuoKfaPcnU4VibgMq0HRC8KjdanEFCkwzYA7jnJLfQ=",
            customer="allachtoon-ote",
            test_mode=True
        )

        print("\nConnection Configuration:")
        print(f"Base URL: {client.base_url}")
        print(f"Test Mode: {client.test_mode}")
        print(f"Customer ID: {client.customer}")
        print("\nAttempting API connection...\n")

        # Test domain availability check
        domain = "example.com"
        print(f"Checking domain availability: {domain}")
        print(f"Requesting: {client.base_url}/domains/{domain}/check")
        availability = client.domains.check(domain)
        print(f"Domain check response: {availability}")

        # Test domain listing with correct parameters
        print("\nTesting domain listing:")
        print(f"Requesting: {client.base_url}/domains")
        domains = client.domains.list()

        print("✓ Successfully connected to API")
        if domains.get('entities'):
            print(f"Total domains: {len(domains['entities'])}")
            print("\nListing domains:")
            for domain in domains['entities']:
                status = ', '.join(domain.get('status', [])) if isinstance(domain.get('status'), list) else domain.get(
                    'status', 'N/A')
                print(f"- {domain.get('domainName', 'N/A')} ({status})")
                print(f"  Registrant: {domain.get('registrant', 'N/A')}")
                print(f"  Created: {domain.get('createdDate', 'N/A')}")
                print(f"  Expires: {domain.get('expiryDate', 'N/A')}")
        else:
            print("No domains found")

        # Test TLD info
        print("\nTesting TLD info:")
        try:
            # Get info for .com TLD
            print(f"\nRequesting: {client.base_url}/tlds/com/info")
            print("Getting info for .com TLD:")
            com_tld = client.tlds.get_info("com")
            metadata = com_tld.metadata

            print("TLD Metadata:")
            print(f"- Grace Periods:")
            print(f"  Add: {metadata.add_grace_period} days")
            print(f"  Auto Renew: {metadata.auto_renew_grace_period} days")
            print(f"  Renew: {metadata.renew_grace_period} days")
            print(f"  Transfer: {metadata.transfer_grace_period} days")

            print("\n- Contact Requirements:")
            print(
                f"  Admin: {metadata.admin_contacts.min}-{metadata.admin_contacts.max} contacts (Required: {metadata.admin_contacts.required})")
            print(
                f"  Tech: {metadata.tech_contacts.min}-{metadata.tech_contacts.max} contacts (Required: {metadata.tech_contacts.required})")
            print(
                f"  Billing: {metadata.billing_contacts.min}-{metadata.billing_contacts.max} contacts (Required: {metadata.billing_contacts.required})")

            print("\n- Nameserver Requirements:")
            print(f"  Min: {metadata.nameservers.min}")
            print(f"  Max: {metadata.nameservers.max}")
            print(f"  Required: {metadata.nameservers.required}")

            print("\n- DNSSEC:")
            print(f"  Allowed Records: {metadata.allowed_dnssec_records}")
            print(f"  Allowed Algorithms: {metadata.allowed_dnssec_algorithms}")

        except Exception as e:
            print(f"✗ TLD info error: {str(e)}")
            print(f"Current base URL: {client.base_url}")

        # Test pricelist retrieval
        print("\nTesting pricelist retrieval:")
        try:
            print(f"\nRequesting: {client.base_url}/customers/{client.customer}/pricelist")
            print("Getting pricelist:")
            pricelist = client.customers.get_pricelist(client.customer)

            print("\nPricelist:")
            for price in pricelist.prices:
                print(f"- {price.product} ({price.action}):")
                print(f"  Price: {price.price / 100:.2f} {price.currency}")

        except Exception as e:
            print(f"✗ Pricelist error: {str(e)}")
            print(f"Current base URL: {client.base_url}")

        return True

    except AuthenticationException:
        print("✗ Authentication failed: Please check your API key")
        print("\nTroubleshooting tips:")
        print("1. Verify your API key is correct")
        print("2. Ensure your API key is not expired")
        print("3. Check if you have the necessary permissions")
        return False
    except ValidationException as e:
        print(f"✗ Validation error: {str(e)}")
        print("\nPlease check your request parameters")
        return False
    except NotFoundException:
        print("✗ API endpoint not found")
        print("\nPlease check if you're using the correct API version")
        print(f"Current base URL: {client.base_url}")
        return False
    except RealtimeRegisterException as e:
        print(f"✗ API Error: {str(e)}")
        print("\nPlease check your API configuration")
        print(f"Current base URL: {client.base_url}")
        return False
    except Exception as e:
        print(f"✗ Unexpected error: {str(e)}")
        print("\nPlease contact support if the issue persists")
        print(f"Current base URL: {client.base_url}")
        return False


if __name__ == "__main__":
    test_api_connection()
