import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # 1. Redirect "Request Access" logic to pricing.html
    # Look for buttons with data-i18n="market_btn_request" or data-i18n="btn_request_access"
    # and ensure they have the correct onclick.
    
    # Simple regex for the marketplace buttons
    content = content.replace("onclick=\"window.location.href='investor-profile.html'\"", "onclick=\"window.location.href='pricing.html'\"")
    
    # Handle buttons that don't have onclick yet but have the request-access i18n
    # <button class="..." data-i18n="btn_request_access">...</button>
    content = re.sub(r'(<button[^>]*data-i18n=["\']btn_request_access["\'][^>]*>)', r'\1', content) # Placeholder for more complex replacement if needed
    
    # In lender-view.html specifically
    if filename == 'lender-view.html':
        content = content.replace('data-i18n="btn_request_access">', 'onclick="window.location.href=\'pricing.html\'" data-i18n="btn_request_access">')
        content = content.replace('VND 85.2B', '85.2B <u>đ</u>')

    # In verification-center.html specifically
    if filename == 'verification-center.html':
        content = content.replace('VND 500B', '500B <u>đ</u>')

    # 2. General Currency Standardization in HTML (hardcoded strings)
    content = content.replace(' VNĐ', ' <u>đ</u>')
    content = content.replace(' VND', ' <u>đ</u>')
    
    if content != original_content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")

print("Completed HTML updates for redirects and currency.")
