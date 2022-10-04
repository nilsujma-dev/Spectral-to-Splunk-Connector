import os
import json
import sys

import requests
import dotenv

dotenv.load_dotenv()

SPECTRAL_URL = os.environ["SPECTRAL_URL"]
SPECTRAL_SPU = os.environ["SPECTRAL_SPU"]
SPLUNK_URL = os.environ["SPLUNK_URL"]
SPLUNK_AUTH = os.environ["SPLUNK_AUTH"]


def get_spectral_issues() -> list:
    headers = {"Authorization": f"Bearer {SPECTRAL_SPU}", "Accept": "application/json"}
    r = requests.get(f"{SPECTRAL_URL}/api/v1/issues", headers=headers)
    return r.json()


def create_splunk_event(event):
    ...


def main():
    issues = get_spectral_issues()["issues"]

    headers = {"Authorization": f"Splunk {SPLUNK_AUTH}"}
    for issue in issues:
        data = {"event": issue}
        r = requests.post(
            f"{SPLUNK_URL}/services/collector/event",
            headers=headers,
            json=data,
            verify=False,
        )


if __name__ == "__main__":
    main()
