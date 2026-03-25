import os

filename = 'shared/translations.js'

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix unescaped double quotes in class attributes within translation strings
content = content.replace('class="', "class='")
content = content.replace('font-bold"', "font-bold'") # For status_mismatch line

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed unescaped quotes in translations.js")
