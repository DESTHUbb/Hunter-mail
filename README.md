# Hunter-mail

![H-M 3 (1)](https://user-images.githubusercontent.com/90658763/234571180-3f0fdcb6-0f01-44d4-b67b-d2dce62e714e.gif)



# Application operation:

## It is a command line application that uses the Hunter.io API to search for emails related to a specific email address.
## This code is used to automate the search for emails related to a specific email address and may be useful for marketing or research purposes.

# Tools:

## For its operation, the following tools are used:

### -Argparse:
#### Is a Python library used to parse command line arguments. In this case, it is used to define the arguments that can be passed to the application, such as the email address to look up, the API key, the email domain to filter, and others.
### -Requests: 
#### Is a Python library used to send HTTP requests to web servers. In this case, it is used to send requests to the Hunter.io API and get the search results.
### -Config:
#### This is an external file that contains constants like email address and API key. It is used to separate confidential information from the application source code.

# Functions:
## -fetch_emails:
### The fetch_emails function is what does the fetching of emails. It takes the lookup email address, API base URL, authentication headers, proxies, and command line arguments. It then sends requests to the Hunter.io API and processes the results to find related emails. The function uses a set to deduplicate and a request counter to avoid exceeding the API request limit.

## -Main:
### The main function is the main entry point of the program and uses argparse to parse command line arguments. Then, call the fetch_emails function to fetch the emails.

# Use:
## Config File: The code uses the Hunter.io email address and API key from a configuration file called config.py. Therefore, you will need to create a configuration file with the following values:

### This is what should be added in config.py
```python
EMAIL = 'your_email_address'
API_KEY = 'your_hunterio_api_key'
```

### You can save this file in the same directory as the Python file. Make sure you don't share your API key with anyone else.

### After you have everything set up, you can run the provided code on the command line. For example:
```python
python <file_name>.py <email_address_to_lookup> <hunterio_api_key>
```
### You can also use the optional arguments as described in the code.

# LIBRARIES:

## Argparse:
[![Argparse](https://user-images.githubusercontent.com/90658763/235024808-d9e3fe1d-fa76-40fc-9404-c28edbf32611.png)](https://docs.python.org/es/3/library/argparse.html)

## Requests:
[![Requests](https://user-images.githubusercontent.com/90658763/235026743-488143d7-310c-420f-8745-432ec8288d5b.png)](https://pypi.org/project/requests/)

## Config:
[![Requests](https://user-images.githubusercontent.com/90658763/235028993-2337cb2f-d2c9-4ceb-a375-0d968735a32a.png)](https://wiki.python.org/moin/ConfigParserShootout)

## Hunter.io:

[![Requests](https://user-images.githubusercontent.com/90658763/235026743-488143d7-310c-420f-8745-432ec8288d5b.png)](https://pypi.org/project/requests/)
https://hunter.io/users/sign_in

