import argparse
import requests
import config

email = config.EMAIL
api_key = config.API_KEY


def format_phone_number(phone_number):
    """Removes non-numeric characters from a phone number."""
    
    
       characters_to_remove = {'-', '.', '(', ')'}
    return ''.join(char for char in phone_number if char not in characters_to_remove)


def fetch_emails(base_url, search_email, headers, proxies, args):
    """Search for emails related to the specified email address."""
    all_emails = {search_email}
  
request_count = 0
    for email in all_emails:
        if request_count >= args.max_requests:
            print(f'Max limit of {args.max_requests} requests reached.')
    

break

        target_url = f'{base_url}emails={email}'
