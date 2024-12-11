from config import ENV, UFCSTATS_FIGHTERS_URL
from helpers import get_html_content

import string
import fake_useragent
import os

ua = fake_useragent.UserAgent(platforms='desktop')
print(ua.random)

base_url = UFCSTATS_FIGHTERS_URL


# char has values from a to z
for char in string.ascii_lowercase:
    url = base_url.format(char)
    response = get_html_content(url=url)

    # retrive the url and save the response into a file
    with open ("./data/{}.htm".format(char), "wb") as text_file:
        text_file.write(response)

    print(response)
    break
