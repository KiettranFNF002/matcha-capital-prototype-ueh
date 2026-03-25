import os
import re

filename = 'shared/translations.js'

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Parse the translations object
# We have translations = { 'vi': { ... }, 'en': { ... } }
# The goal is to make 'vi' identical to 'en' (English-only) or just replace strings.

# A more direct way: 
# Find all occurrences of "vi: {" to "}," and replace its contents with the contents of "en: {" to "},"

vi_start = content.find("vi: {")
vi_end = content.find("},", vi_start)
en_start = content.find("en: {")
en_end = content.find("},", en_start)

if vi_start != -1 and en_start != -1:
    en_body = content[en_start+5:en_end]
    content = content[:vi_start+5] + en_body + content[vi_end:]

# 2. Global Currency Standardization to <u>đ</u>
# The user wants ONLY one. I'll use <u>đ</u>.
content = content.replace(' VND', ' <u>đ</u>')
content = content.replace(' VNĐ', ' <u>đ</u>')
content = content.replace(' Billion VND', ' Billion <u>đ</u>')
content = content.replace(' Million VND', ' Million <u>đ</u>')
# Ensure no double đ
content = content.replace('<u>đ</u> <u>đ</u>', '<u>đ</u>')
content = content.replace('<u>đ</u><u>đ</u>', '<u>đ</u>')

# 3. Specific price in pricing.html (translations)
content = content.replace('500,000<u>đ</u>', '500,000<u>đ</u>') # Already okay

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)

print("Standardized translations to English and Unified Currency.")
