import os
import re

filename = 'shared/translations.js'

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix unescaped double quotes inside SVG class attributes
# Find class="some-classes" and change to class='some-classes'
content = re.sub(r'class="([^"]*)"', r"class='\1'", content)

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)

print("Properly fixed unescaped quotes in translations.js using regex")
