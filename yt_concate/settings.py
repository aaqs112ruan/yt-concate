import os
from dotenv import load_dotenv
# 彷彿讓.env檔案當中所寫的API_KEY加入電腦的環境變數 讓os.getenv可以obtain到
load_dotenv()

API_KEY = os.getenv('API_KEY')
