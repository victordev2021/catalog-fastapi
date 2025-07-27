from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello World vat fast api..."}


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
