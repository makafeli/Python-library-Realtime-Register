from typing import Dict, Any
from decimal import Decimal

class Currency:
    """Currency handling utility"""
    
    @staticmethod
    def format_amount(amount: Decimal, currency: str) -> str:
        """Format amount with currency"""
        return f"{amount:.2f} {currency}"
    
    @staticmethod
    def parse_amount(amount_str: str) -> tuple[Decimal, str]:
        """Parse amount string to decimal and currency"""
        amount, currency = amount_str.split()
        return Decimal(amount), currency
    
    @staticmethod
    def convert_amount(amount: Decimal, from_currency: str, to_currency: str, rates: Dict[str, float]) -> Decimal:
        """Convert amount between currencies"""
        if from_currency == to_currency:
            return amount
            
        if from_currency not in rates or to_currency not in rates:
            raise ValueError(f"Exchange rate not available for {from_currency} to {to_currency}")
            
        # Convert through base currency (usually EUR)
        amount_base = amount * Decimal(str(rates[from_currency]))
        return amount_base / Decimal(str(rates[to_currency]))