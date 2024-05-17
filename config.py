from os import environ
from dotenv import load_dotenv

load_dotenv()
# Load database credentials from environment variables
user = environ.get("ATLAS_USER")
pwd = environ.get("ATLAS_PWD")
db = environ.get("ATLAS_DB")
url = environ.get("ATLAS_URL")

# load models credentials from environment variables
pc_api_key = environ.get("PINECONE_API_KEY")
g_api_key = environ.get("GOOGLE_API_KEY")

