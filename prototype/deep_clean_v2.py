import os
import re

files_to_check = [f for f in os.listdir('.') if f.endswith('.html') or f.endswith('.js')]
# Exclude some files if needed
files_to_check = [f for f in files_to_check if f not in ['find_vi.py', 'salvage_translations.py']]

vietnamese_map = {
    "Mục tiêu": "Target",
    "THỜI HẠN": "TENOR",
    "KHÁM PHÁ": "EXPLORE",
    "Yêu cầu Truy cập": "Request Access",
    "Thử nghiệm": "Trial",
    "Cá nhân": "Individual",
    "Dành cho nhà đầu tư cá nhân & nhóm nhỏ": "For individual investors & small teams",
    "Thiết kế cho sự tăng trưởng & quy mô doanh nghiệp": "Designed for growth & business scale",
    "Tỷ": "Billion",
    "Triệu": "Million",
    "đ": "đ", # Keep đ but ensure it's in innerHTML
    "Kho hàng / Khoản thu": "Inventory / Receivables",
    "Kỳ hạn": "Tenor",
    "TS đảm bảo": "Collateral",
    "ĐANG HOẠT ĐỘNG": "ACTIVE",
    "ĐANG CHỜ": "PENDING",
    "Đã hủy": "Cancelled",
    "Hủy bỏ": "Cancel",
    "Đồng ý": "Agree",
    "Tiếp tục": "Continue",
    "Quay lại": "Back",
}

for filename in files_to_check:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # 1. Replace known Vietnamese words
    for vi, en in vietnamese_map.items():
        content = content.replace(vi, en)
    
    # 2. Fix JS dynamic updates from textContent to innerHTML for currency
    content = content.replace(".textContent = val + ',000,000,000 <u>đ</u>'", ".innerHTML = val + ',000,000,000 <u>đ</u>'")
    content = content.replace(".textContent = val + ' <u>đ</u>'", ".innerHTML = val + ' <u>đ</u>'")
    
    # 3. Clean up any loose Tỷ/VND/VNĐ
    content = content.replace(' Billion VND', ' Billion <u>đ</u>')
    content = content.replace(' Billion VNĐ', ' Billion <u>đ</u>')
    
    if content != original_content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Deep cleaned {filename}")

print("Final English code sweep complete.")
