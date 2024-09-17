import os
import requests
from dotenv import load_dotenv
import pytest


@pytest.mark.order(1)
def test_create_repository():
    load_dotenv()
    url = f"https://api.github.com/user/repos"
    headers = {
        "Authorization": f"token {os.getenv("GITHUB_TOKEN")}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "name": os.getenv("REPO_NAME"),
        "auto_init": True,
        "private": False
    }
    response = requests.post(url, json=data, headers=headers)
    assert response.status_code == 201


@pytest.mark.order(2)
def test_check_repository_exists():
    load_dotenv()
    url = f"https://api.github.com/users/{os.getenv("GITHUB_USERNAME")}/repos"
    headers = {
        "Authorization": f"token {os.getenv("GITHUB_TOKEN")}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers)
    repos = response.json()
    for repo in repos:
        if repo['name'] == os.getenv("REPO_NAME"):
            assert repo['name'] == os.getenv("REPO_NAME")


@pytest.mark.order(3)
def test_delete_repository():
    load_dotenv()
    url = f"https://api.github.com/repos/{os.getenv("GITHUB_USERNAME")}/{os.getenv("REPO_NAME")}"
    headers = {
        "Authorization": f"token {os.getenv("GITHUB_TOKEN")}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204
