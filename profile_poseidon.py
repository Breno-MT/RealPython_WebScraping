import re
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/poseidon"

page = urlopen(url)
html = page.read().decode("utf-8")
pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
print("Match results: ", match_results)
title = match_results.group()
title = re.sub("<.*?>", "", title)

print("Title: ", title)
