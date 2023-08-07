import re
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")

# Get Name - My Solution
pattern_name = "<h2.*?>.*?</h2.*?>"
match_results = re.search(pattern_name, html, re.IGNORECASE)
name = match_results.group()
name = re.sub("<.*?>", "", name)
print(name)

# Get Color - My Solution with RealPython Solution helps lol
color_index = html.find("Favorite Color:")
color_start_index = color_index + len("Favorite Color:")
color_end_offset = html[color_start_index:].find("<")
color_end_index = color_start_index + color_end_offset
color_raw_text = html[color_start_index:color_end_index]
color_text = color_raw_text.strip(" \r\n\t")
print("Favorite Color:", color_text)

# Get Color and Name - RealPython Solution
# for string in ["Name: ", "Favorite Color:"]:
#     string_start_idx = html.find(string)
#     text_start_idx = string_start_idx + len(string)

#     next_html_tag_offset = html[text_start_idx:].find("<")
#     text_end_idx = text_start_idx + next_html_tag_offset

#     raw_text = html[text_start_idx : text_end_idx]
#     clean_text = raw_text.strip(" \r\n\t")
#     print(clean_text)
