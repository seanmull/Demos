import requests
api_url = "http://localhost:16649/v0/notifications"
notification = {
    "role": "user",
    "target": "Phone 1",
    "subject": "wake up",
    "body": "something is on fire",
    "mode": "sms"
}
response = requests.post(api_url, json=notification)
response.json()
response.status_code
