import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# Major strings to replace in HTML (to avoid FOUC or fallback to VI)
hardcoded_replacements = {
    "Dự kiến băm Hash": "Pending Hash",
    "Mục tiêu": "Target",
    "IRR dự kiến": "Expected IRR",
    "Thời hạn": "Tenor",
    "Xem Teaser": "View Teaser",
    "Yêu cầu Truy cập": "Request Access",
    "VỐN LƯU ĐỘNG CAO SU": "RUBBER WORKING CAPITAL",
    "Tài trợ thu mua mủ cao su cho mùa vụ 2026. Đảm bảo bằng kho hàng và phải thu.": "Financing rubber latex procurement for 2026 season. Secured by inventory & receivables.",
    "Loại vốn": "Capital Type",
    "250 Tỷ": "250 Billion",
    "335.9 Tỷ": "335.9 Billion",
    "TS đảm bảo": "Collateral",
    "Kỳ hạn": "Tenor",
    "12-18 tháng": "12-18 months",
    "XUẤT KHẨU TRÁI CÂY": "FRUIT EXPORT",
    "Hình thức: Vốn góp (Equity) | DRG góp 33.33%": "Mode: Equity | DRG stake 33.33%",
    "Khám phá": "Explore",
    "Pro / Thử nghiệm": "Pro / Trial",
    "Dành cho nhà đầu tư cá nhân & nhóm nhỏ": "For individual investors & small teams",
    "/ tháng": "/ month",
    "/ THÁNG": "/ MONTH",
    "Business / Thử nghiệm": "Business / Trial",
    "Thiết kế cho sự tăng trưởng & quy mô doanh nghiệp": "Designed for growth & business scale",
    "DỰ ÁN CAMBODIA": "CAMBODIA PROJECT",
    "Hình thức: Project Finance | Đối tượng: Quỹ PE": "Mode: Project Finance | Target: PE Funds",
    "KIỂM TOÁN & QUẢN TRỊ": "AUDIT & ADMINISTRATION",
    "TỔNG THANH TOÁN": "TOTAL PAYMENT",
}

for filename in html_files:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    for vi, en in hardcoded_replacements.items():
        content = content.replace(vi, en)
    
    # Also standardize <u>đ</u> in HTML
    content = content.replace(' VND', ' <u>đ</u>')
    content = content.replace(' VNĐ', ' <u>đ</u>')
    
    if content != original_content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Hardcoded strings updated in {filename}")

print("Completed Final HTML Polish.")
