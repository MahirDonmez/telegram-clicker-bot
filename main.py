import uvicorn
from fastapi import FastAPI
import os
from dotenv import load_dotenv

# .env dosyasını yükle
load_dotenv()

app = FastAPI()

API_TOKEN = os.getenv('API_TOKEN')

@app.get('/')
def test():
    print(API_TOKEN)
    return True

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, reload=True)
