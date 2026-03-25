import os
import re

filename = 'shared/translations.js'

with open(filename, 'r', encoding='utf-8') as f:
    text = f.read()

# Greedily search for all "key: value" pairs in the entire file
# We assume keys are alphanumeric and values are in " " or ' '
pairs = re.findall(r'([a-zA-Z0-9_]+):\s*("(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\')', text)

# Filter out noise and preserve unique keys (keeping the last one found, which is likely from the 'en' block if it was at the bottom)
translations_dict = {}
for k, v in pairs:
    if k not in ['vi', 'en', 'translations', 'window']:
        translations_dict[k] = v

# Rebuild the file
dict_content = "    " + ",\n    ".join([f'{k}: {v}' for k, v in translations_dict.items()])

new_translations = f"""const translations = {{
  vi: {{
{dict_content}
  }},
  en: {{
{dict_content}
  }}
}};

window.translations = translations;
"""

# Final currency fix
new_translations = new_translations.replace(' VND', ' <u>đ</u>')
new_translations = new_translations.replace(' VNĐ', ' <u>đ</u>')
# Ensure Billion is English
new_translations = new_translations.replace(' Tỷ', ' Billion')
new_translations = new_translations.replace(' Billion <u>đ</u>', ' Billion <u>đ</u>')

with open(filename, 'w', encoding='utf-8') as f:
    f.write(new_translations)

print(f"Salvaged {len(translations_dict)} translation keys.")
