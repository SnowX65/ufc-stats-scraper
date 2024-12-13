from scripts import ENV, UFCSTATS_FIGHTERS_URL, UFCSTATS_FIGHTERS_HEADERS, retrive_web_page, content_exists, write_to_file
import string
import random
import time
import json
import logging
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

def get_ufcstats_fighters():
    """
    Scrapes the fighters table and returns a list of fighters.
    """
    fighters = []

    # retrive list of fighters - setting char as 'ž' retrives the entire list
    html_content = retrive_web_page(UFCSTATS_FIGHTERS_URL.format('ž'), 'fighters.htm')

    soup = BeautifulSoup(html_content, 'lxml')

    fighters_table      = content_exists('table', soup.find('table', {'class': 'b-statistics__table'}))
    figthers_table_body = content_exists('tbody', fighters_table.find('tbody'))
    fighters_table_rows = content_exists('tr', figthers_table_body.find_all('tr'))

    # first row is empty so skip it 
    rows = fighters_table_rows[1:]

    for row_index, row in enumerate(rows):
        row_td = row.find_all('td')

        fighter = {}

        for td_index, td in enumerate(row_td):

            # get the fighters page URL
            if (td_index == 0):
                url = content_exists('a', td.find('a'))['href'].split('/')[-1]
                fighter['url'] = url

            value = ''.join(td.find_all(text=True)).strip().replace('-', '').replace('\\', '')

            fighter[UFCSTATS_FIGHTERS_HEADERS[td_index]] = value
        
        fighters.append(fighter)


    write_to_file(json.dumps(fighters), './data/fighters.json')




