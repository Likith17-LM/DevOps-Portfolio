from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to my DevOps Portfolio 🚀"}


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "devops-portfolio"
    }