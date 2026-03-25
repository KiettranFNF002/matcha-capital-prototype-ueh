import os

def find_vi_lines(filepath):
    bad_chars = "íáạủậổàưảổừăâệé"
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        for i, line in enumerate(f, 1):
            found = [c for c in bad_chars if c in line]
            if found:
                print(f"File: {filepath}, Line {i}: {line.strip()} (Chars: {found})")

find_vi_lines('dashboard.html')
find_vi_lines('deal-discovery.html')
