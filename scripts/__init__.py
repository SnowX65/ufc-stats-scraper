import logging
from scripts.config import ENV, UFCSTATS_FIGHTERS_URL
from scripts.helpers import content_exists, retrive_web_page

# Create the logger
logger = logging.getLogger(__name__)
logger = logging.basicConfig(filename='app.log', format='%(asctime)s %(levelname)s %(module)s - %(funcName)s: %(message)s',
                             datefmt='%Y-%m-%d %H:%M:%S', encoding='utf-8', level=logging.INFO)