# Telegram bot parameters
CHANNEL_ID = 'your-channel-id'
with open('.env', 'rt') as token:
    TOKEN = token.readline().strip()

# Filtering spam messages
MAX_MESSAGE_COUNT = 15
DELAY = 15

# Cropping parameters. Correction for your display is IMPORTANT!
DEFAULT_CROP_TOP = 110
CROP_TOP = 110
CROP_LEFT = 350
CROP_RIGHT = 400

# Table with answers: data/philosophy.csv or data/effective_communication.csv
ANSWERS_TABLE = 'data/business.csv'

# Directory with screenshots.
# Remember that all pictures here will be deleted after scanning!
BACKUP_DIR: str = '~/Pictures/Screenshots_back/'
DIR_NAME: str = '~/Pictures/Screenshots/business/'

# Technical directory for parsing texts
OUTPUT_DIR: str = 'data/texts/'
