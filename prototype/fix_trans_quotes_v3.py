import os
import re

filename = 'shared/translations.js'

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix cases where class opening was changed but closing wasn't
content = re.sub(r"class='([^\"']*)(\")", r"class='\1'", content)
# Ensure all class attributes use single quotes inside strings
content = re.sub(r'class="([^"]*)"', r"class='\1'", content)

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)

print("Robustly fixed unescaped quotes in translations.js")
