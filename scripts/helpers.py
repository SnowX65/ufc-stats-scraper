import requests
import os
from config import ENV

def get_html_content_file(path):
    """
    Returns the HTML content from a file.
    """    

    if path:
        if os.path.exists(path):
            with open(path, 'r') as f:
                return f.read()
        else:
            raise FileNotFoundError('No such file ')

def get_html_content_url(url, tries=0):
    """
    Returns the HTML content from either the live website or the test file.
    """
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        raise SystemExit(requests.exceptions.RequestException)

    return response.content

