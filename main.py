from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
import requests
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

    repo_full_name = payload["repository"]["full_name"]
    branch = payload["ref"].split("/")[-1]
    print("======================\n",payload)

    print(f"Repo: {repo_full_name}")
    print(f"Branch: {branch}")

    # Fetch repo contents
    # files = get_repo_contents(repo_full_name)

    # print("Files in repo:")
    # for file in files:
    #     print(file["name"])

    return {"status": "processed"}


# def get_repo_contents(repo_full_name):
#     url = f"https://api.github.com/repos/{repo_full_name}/contents"

#     headers = {
#         "Authorization": f"Bearer {GITHUB_TOKEN}",
#         "Accept": "application/vnd.github+json"
#     }

#     response = requests.get(url, headers=headers)
#     return response.json()

handler = Mangum(app)