import argparse
import requests
import config

email = config.EMAIL
api_key = config.API_KEY

def format_phone_number(phone_number):
    """Elimina los caracteres no numéricos de un número de teléfono."""
    
    
       characters_to_remove = {'-', '.', '(', ')'}
    return ''.join(char for char in phone_number if char not in characters_to_remove)

