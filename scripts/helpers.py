import requests
import os
import logging
import json
import fake_useragent
from scripts import ENV, UFCSTATS_FIGHTERS_URL


logger = logging.getLogger(__name__)

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

def get_html_content_url(url, userAgent):
    """
    Returns the HTML content from either the live website or the test file.
    """
    logger.info('Retriving URL: %s', url)

    try:
        response = requests.get(url, headers={'User-Agent': userAgent})
    except requests.exceptions.RequestException as e:
        logger.warning('Error retriving URL: %s \n %s', url, e)
        raise SystemExit(requests.exceptions.RequestException)

    return response.content


def retrive_web_page(url, fileName):

    fileName = './data/' + fileName

    if fileName:
        if os.path.exists(fileName):
            logger.info('Retriving data from local file - %s', fileName)
            with open(fileName, 'r') as f:
                return f.read()

    ua = fake_useragent.UserAgent(platforms='desktop').random
    logger.info('Fake user agent set to - %s', ua)

    response = get_html_content_url(url, userAgent=ua)

    if not response:
        raise ValueError('No content from response')

    if fileName:
        # retrive the response and save it into a file
        write_to_file(response, fileName)

    return response

def write_to_file(data, fileName): 

    mode = 'w'

    if isinstance(data, bytes):
        mode = 'wb'

    with open (fileName, mode) as file:
        file.write(data)  
    # retrive the response and save it into a file
    


def content_exists(element, content, raiseValueError=True):

    if content is None:
        logger.warning('Element [%s] not found in web page', element)

        if raiseValueError:
            raise ValueError('Element [%s] not found in web page' % element)
    
    return content
