import requests
session = requests.Session()
session.auth = ("ditto", "ditto")

response = session.get("http://localhost:8080/api/2/things/org.eclipse.ditto:39bf8d66-ed48-4fad-ae35-6dc576a1cc7d/attributes/Position/1")
print(response.content)