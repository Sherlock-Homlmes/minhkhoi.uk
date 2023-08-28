import os
from dotenv import load_dotenv

load_dotenv()

ENVIRONMENT = os.getenv("ENVIRONMENT")
SECRET_KEY = os.getenv("SECRET_KEY")

# mongodb
DATABASE_URL = os.environ.get("DATABASE_URL")

# imgbb
IMGBB_API_KEY = os.environ.get("IMGBB_API_KEY")

# google oauth
GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URL = os.environ.get("GOOGLE_REDIRECT_URL")

# casso
CASSO_API_KEY = os.environ.get("CASSO_API_KEY")
CASSO_SECRET_KEY = os.environ.get("CASSO_SECRET_KEY")