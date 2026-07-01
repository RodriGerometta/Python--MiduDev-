import re
import os
os.system("cls")

# url = input("URL: ").strip()
# username = url.removeprefix("https://twitter.com/", "")
# print(f"Username: {username}")

url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-zA-Z0-9_]+)$", url, re.IGNORECASE):
    print("Username:", matches.group(1))