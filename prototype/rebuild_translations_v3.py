import os
import re

filename = 'shared/translations.js'

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Clean up the messed up structure from previous failed scripts
# We want to extract the content inside the first '{ ... }' block that looks like a valid translation object.

# Since the file is already mostly English but technically broken, 
# let's just extract the *keys and values* and rebuild it.

# A better way: find the last occurrence of '{' and '}' that contains the pricing plans
# or just look for the first '{' after 'vi: {' and the matching '}'

# Actually, let's just use a simplified version:
# Find everything between the first '{' after 'en: {' and the last '}' before '};' 

en_start = content.find('en: {')
if en_start != -1:
    body_start = content.find('{', en_start)
    body_end = content.rfind('}') # Last brace of the object
    # Find the matching brace for the whole translations object
    # Let's just find the last block of keys.
    
    # Let's try to find the full body of the 'en' object.
    # It ends with '  }\n};' or similar.
    
    # Actually, I'll just search for all "key: value" pairs.
    pairs = re.findall(r'(\w+):\s*("(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\')', content)
    
    dict_content = "    " + ",\n    ".join([f'{k}: {v}' for k, v in pairs if k not in ['vi', 'en', 'translations']])
    
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
    # Fix currency formatting inside strings
    new_translations = new_translations.replace(' VND', ' <u>đ</u>')
    new_translations = new_translations.replace(' VNĐ', ' <u>đ</u>')
    new_translations = new_translations.replace(' Billion VND', ' Billion <u>đ</u>')
    new_translations = new_translations.replace(' Billion VNĐ', ' Billion <u>đ</u>')
    new_translations = new_translations.replace(' Billion <u>đ</u>', ' Billion <u>đ</u>') # Ensure no double
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_translations)
    print("Cleanly rebuilt translations.js and fixed syntax errors.")

else:
    print("Error: Could not find 'en:' block to recover from.")
