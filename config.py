from os import getenv

from aiofiles import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = getenv('TOKEN')


MANAGER_ID = int(os.getenv('MANAGER_ID', 0))