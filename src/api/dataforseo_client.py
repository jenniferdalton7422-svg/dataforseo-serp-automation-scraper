thonpython
import base64
import json
import logging
import time
import requests
from .auth_handler import AuthHandler

class DataForSEOClient:
 BASE_URL = "https://api.dataforseo.com/v3/serp/google/organic/task_post"

 def __init__(self, username: str, password: str):
 self.auth_header = AuthHandler.generate_auth_header(username, password)

 def fetch_serp(self, keyword: str):
 payload = {
 "data": [{
 "keyword": keyword,
 "language_name": "English",
 "location_name": "United States"
 }]
 }
 headers = {"Authorization": self.auth_header}

 for attempt in range(3):
 try:
 resp = requests.post(self.BASE_URL, json=payload, headers=headers, timeout=15)
 if resp.status_code == 200:
 data = resp.json()
 task_id = data["tasks"][0]["id"]
 return self._fetch_task_result(task_id)
 else:
 logging.warning(f"API error {resp.status_code}: {resp.text}")
 except Exception as e:
 logging.warning(f"Retry {attempt+1}/3 failed: {e}")
 time.sleep(2)

 raise RuntimeError(f"Failed to fetch SERP for keyword: {keyword}")

 def _fetch_task_result(self, task_id: str):
 result_url = f"https://api.dataforseo.com/v3/serp/google/organic/task_get/advanced/{task_id}"
 headers = {"Authorization": self.auth_header}

 for _ in range(10):
 resp = requests.get(result_url, headers=headers, timeout=10)
 data = resp.json()
 if data.get("tasks"):
 results = data["tasks"][0].get("result")
 if results:
 return results[0]
 time.sleep(1)

 raise RuntimeError("Timed out waiting for SERP results.")