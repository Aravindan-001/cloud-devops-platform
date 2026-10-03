from fastapi import FastAPI

app = FastAPI(
    title="Cloud DevOps Platform",
    version="1.0.0",
)


@app.get("/")
def root():
    return {"message": "Cloud DevOps Platform API"}


@app.get("/health")
def health():
    return {"status": "healthy", "service": "cloud-devops-platform"}
