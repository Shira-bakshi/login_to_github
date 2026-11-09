import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_URL = "https://github.com"
EMAIL_GITHUB = os.getenv("TEST_USERNAME")
PASSWORD_GITHUB = os.getenv("TEST_PASSWORD")