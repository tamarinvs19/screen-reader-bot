# Telegram bot parameters
TOKEN = 'your-token'
CHANNEL_ID = 'your-channel-id'

# Filtering spam messages
MAX_MESSAGE_COUNT = 15
DELAY = 15

# Cropping parameters. Correction for your display is IMPORTANT!
CROP_TOP = 110
CROP_LEFT = 350
CROP_RIGHT = 400

# Table with answers: data/philosophy.csv or data/effective_communication.csv
ANSWERS_TABLE = 'data/philosophy.csv'

# Directory with screenshots.
# Remember that all pictures here will be deleted after scanning!
DIR_NAME: str = '~/Pictures/Screenshots/'
BACKUP_DIR: str = '~/Pictures/Screenshots_back/'

# Technical directory for parsing texts
OUTPUT_DIR: str = 'data/texts/'
