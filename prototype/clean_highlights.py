import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# Classes to remove from labels that are now handled by CSS :has()
remove_classes = [
    'border-teal-500', 
    'bg-teal-50', 
    'bg-teal-50/20', 
    'bg-teal-50/30', 
    'bg-teal-50/50',
    'bg-teal-50/80',
    'border-l-teal-500',
    'bg-emerald-50/20',
    'border-l-emerald-500',
    'bg-rose-50/20',
    'border-l-rose-500'
]

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We only want to remove these if they are on a <label> or a <div> that acts like a card
    # But since they are now globally handled by CSS for selection, let's target the static ones.
    for cls in remove_classes:
        content = content.replace(f' {cls}', '')
        content = content.replace(f'"{cls} ', '"')
        content = content.replace(f'"{cls}"', '""') # Handle cases where it's the only class

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Cleaned highlights in {filename}")
