import os
import re

filename = 'shared/translations.js'

with open(filename, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Extract the 'en' object properly
# Find the start of the 'en' object
en_match = re.search(r'en:\s*{', text)
if en_match:
    en_start = en_match.start()
    # Find the closing brace of the 'en' object
    # This is a bit tricky with nested objects/strings, but we know the structure
    # The 'en' object ends with '  }\n};' or similar at the end of the file.
    en_end = text.rfind('  }')
    if en_end != -1:
        en_content = text[en_start+4:en_end+3] # including "en: {" and closing "  }"
        
        # Now rebuild the file
        new_content = "const translations = {\n  vi: " + en_content + ",\n  " + en_content + "\n};\n\nwindow.translations = translations;"
        
        # 2. Global Currency Standardization to <u>đ</u>
        new_content = new_content.replace(' VND', ' <u>đ</u>')
        new_content = new_content.replace(' VNĐ', ' <u>đ</u>')
        new_content = new_content.replace(' Tỷ', ' Billion')
        new_content = new_content.replace(' Triệu', ' Million')
        new_content = new_content.replace(' billion', ' Billion')
        new_content = new_content.replace('<u>đ</u> <u>đ</u>', '<u>đ</u>')
        new_content = new_content.replace('<u>đ</u><u>đ</u>', '<u>đ</u>')
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Restructured and standardized translations.js")
else:
    print("Could not find 'en' block")
