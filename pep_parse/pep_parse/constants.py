from pathlib import Path


BASE_DIR = Path(__file__).parent.parent
DOMAIN = ['peps.python.org']
HEADERS_PEP_TABLE = ('Статус', 'Количество')
PATTERN = r'(PEP \d+)'
START_URL = ['https://peps.python.org/']
TIME_FORMAT = '%Y-%m-%dT%H-%M-%S'
