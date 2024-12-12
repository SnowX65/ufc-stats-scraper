from scripts import ENV, UFCSTATS_FIGHTERS_URL, retrive_web_page, content_exists
import string
import random
import time
import logging
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

def get_fighters():
    """
    Scrapes the fighters table and returns a list of fighters.
    """
    # retrive list of fighters - setting char as 'ž' retrives the entire list

    html_content = retrive_web_page(UFCSTATS_FIGHTERS_URL.format('ž'), 'fighters.htm')

    soup = BeautifulSoup(html_content, 'lxml')

    fighters_table      = content_exists('table', soup.find('table', {'class': 'b-statistics__table'}))
    figthers_table_body = content_exists('tbody', fighters_table.find('tbody'))
    fighters_rows       = content_exists('tr', figthers_table_body.find_all('tr'))


    
    #class="b-statistics__table"

    print(fighters_rows)





