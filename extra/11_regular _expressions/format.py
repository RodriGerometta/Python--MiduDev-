import re
import os
os.system("cls")

# name = input("What is your name? ").strip()
# if "," in name:
#     last, first = name.split(", ?")
#     name = f"{first} {last}"
# print(f"Hello, {name}")

name = input("What is your name? ").strip()
matches = re.search(r"^(.+), * (.+)$", name)
if matches:
    name = matches.group(2) + " " + matches.group(1)
print(f"Hello, {name}")