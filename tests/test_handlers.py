import json
from pydoc import cli
import re
from urllib import response

import pytest

from app import app

from fastapi.testclient import TestClient

client = TestClient(app.app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200

def test_read_ping():
    response = client.get("/ping")
    assert response.status_code == 200

def test_read_pong():
    response = client.get("/ping/pong")
    assert response.status_code == 200

def test_read_pinging():
    response = client.get("/hello")
    assert response.status_code == 404
