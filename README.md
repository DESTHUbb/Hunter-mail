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
