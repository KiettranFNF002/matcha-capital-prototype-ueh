import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# We want to find characters that are not ASCII (0-127) and not common symbols
# Vietnamese characters are usually in the range U+00C0 to U+1EF9

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Simple regex for non-ascii
    non_ascii = re.findall(r'[^\x00-\x7F]', content)
    # Remove duplicates
    unique_non_ascii = set(non_ascii)
    # Only keep those that look like Vietnamese (ignore some common symbols like currency or emojis if any left)
    interesting = [c for c in unique_non_ascii if c not in ['＋', '→', '←', '🔗', '✔', '⚡', '🔒', '👁', '…', '·', '©', '–', '—']]
    
    if interesting:
        print(f"File: {filename} contains: {interesting}")
