from dotenv import load_dotenv

import os 

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_HOST = os.getenv("DB_HOST")
DB_PASSWORD =os.getenv("DB_PASSWORD")
DB_DATABASE =os.getenv("DB_DATABASE")
DB_PORT = os.getenv("DB_PORT")

