import argparse
import requests
import config

email = config.EMAIL
api_key = config.API_KEY


def format_phone_number(phone_number):
    """Removes non-numeric characters from a phone number."""
    
    
       characters_to_remove = {'-', '.', '(', ')'}
    return ''.join(char for char in phone_number if char not in characters_to_remove)

