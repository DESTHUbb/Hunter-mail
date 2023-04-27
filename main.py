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
    
     response = requests.get(target_url, headers=headers, proxies=proxies)
        response.raise_for_status()
      
     data = response.json()
        for record in data['records']:
            if 'emails' in record:
               
          new_email = record['emails'][0]
                if new_email not in all_emails and (not args.email_domain or new_email.split('@')[-1] == args.email_domain):
               
            all_emails.add(new_email)
        request_count += 1
                
    print('Resultados:')
    for email in sorted(all_emails):
        if args.format_phone:      
                
        email = email.replace(search_email, format_phone_number(search_email))
        print(email)
