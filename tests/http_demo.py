import requests


def main() -> None:
    url = "https://httpbin.org/post"
    payload = {
        "patient_age": 35,
        "symptoms": ["头痛", "发热"],
    }

    response = requests.post(url, json=payload, timeout=10)
    print("status_code:", response.status_code)
    print("content_type:", response.headers.get("content-type"))

    data = response.json()
    print("echoed_json:", data["json"])
    print("url:", data["url"])


if __name__ == "__main__":
    main()
