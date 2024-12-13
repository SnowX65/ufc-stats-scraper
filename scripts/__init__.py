import logging
from scripts.config import ENV, UFCSTATS_FIGHTERS_URL, UFCSTATS_FIGHTERS_HEADERS
from scripts.helpers import content_exists, retrive_web_page, write_to_file

# Create the logger
logger = logging.getLogger(__name__)
logger = logging.basicConfig(filename='app.log', format='%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s',
                             datefmt='%Y-%m-%d %H:%M:%S', encoding='utf-8', level=logging.INFO)