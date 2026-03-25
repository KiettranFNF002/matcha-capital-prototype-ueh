import os
import re

def final_sweep():
    root_dir = r'd:\Downloads\UX_UI_Design_EN_only\prototype'
    
    # 1. Clean up hardcoded highlights in labels/cards that should be dynamic
    # Look for bg-teal-50, border-teal-500, etc. that might be left over in templates
    highlight_patterns = [
        r'bg-teal-50/30',
        r'bg-teal-50',
        r'border-teal-500',
        r'border-teal-400'
    ]
    
    # 2. Ensure Billion <u>đ</u> standardization
    # Replace any lone "B" or "VND" in text that might have been missed
    currency_pairs = [
        (r'\b(\d+(?:\.\d+)?)\s*B\b', r'\1 Billion <u>đ</u>'),
        (r'\b(\d+(?:\.\d+)?)\s*VND\b', r'\1 <u>đ</u>')
    ]

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.html') or file.endswith('.js'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = content
                
                # Cleanup highlights (only if they look like they are in labels/buttons that should be dynamic)
                # But to be safe, I'll only target specific common leftovers
                if file != 'styles.css': # Don't touch the CSS definitions
                    for p in highlight_patterns:
                        # Only remove from class lists
                        new_content = re.sub(f'class="([^"]*?){p}([^"]*?)"', r'class="\1\2"', new_content)
                
                # Update currency
                for pattern, repl in currency_pairs:
                    new_content = re.sub(pattern, repl, new_content)

                # Fix any double spaces in class names
                new_content = re.sub(r'class="\s+', 'class="', new_content)
                new_content = re.sub(r'\s+"', '"', new_content)
                new_content = re.sub(r'\s{2,}', ' ', new_content)

                if new_content != content:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Cleaned: {file}")

if __name__ == "__main__":
    final_sweep()
