import uvicorn
from catalog import main

if __name__ == "__main__":
    uvicorn.run(app=main.api, host="0.0.0.0", port=8000, reload=True)