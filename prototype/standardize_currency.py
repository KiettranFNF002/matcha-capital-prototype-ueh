import os
import re

filename = 'shared/translations.js'

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# Replacement patterns
# 1. Direct VND/VNĐ with space
content = content.replace(' VND', ' <u>đ</u>')
content = content.replace(' VNĐ', ' <u>đ</u>')
content = content.replace('VND ', '<u>đ</u> ')

# 2. Specific Project Values (VI)
content = re.sub(r'(\d+) Tỷ', r'\1 Tỷ <u>đ</u>', content)
content = content.replace('21 Tỷ', '21 Tỷ <u>đ</u>') # Ensure 21 works

# 3. Specific Project Values (EN)
content = re.sub(r'(\d+)B', r'\1B <u>đ</u>', content) # val_125b -> 125B đ
content = content.replace('125B <u>đ</u> <u>đ</u>', '125B <u>đ</u>') # Fix over-replacement if any
content = content.replace('B VND', 'B <u>đ</u>')

# 4. Correcting "Tỷ <u>đ</u> <u>đ</u>" if occurred
content = content.replace('<u>đ</u> <u>đ</u>', '<u>đ</u>')

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)

print("Standardized currency to <u>đ</u> globally in translations.js")
