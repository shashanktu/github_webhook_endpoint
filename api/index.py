from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

@app.post("/github-webhook")
async def github_webhook(request: Request):
    payload = await request.json()

    repo_full_name = payload.get("repository", {}).get("full_name", "unknown")
    ref = payload.get("ref", "")
    branch = ref.split("/")[-1] if ref else None
    print("======================\n",request)

    print(f"Repo: {repo_full_name}")
    print(f"Branch: {branch}")

    return {"status": "processed"}
