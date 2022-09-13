import requests
print(requests.get("https://raw.githubusercontent.com/MdderUofA/cmput404labs/main/lab1/lab1.py").content.decode("utf-8"))