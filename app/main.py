from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "CI/CD pipeline using Github Actions and Docker"}
