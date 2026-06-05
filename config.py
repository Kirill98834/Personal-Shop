from os import getenv

import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = getenv('TOKEN')


MANAGER_ID = int(os.getenv('MANAGER_ID', 0))