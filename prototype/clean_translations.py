import os
import re

filename = 'shared/translations.js'

with open(filename, 'r', encoding='utf-8') as f:
    text = f.read()

# Define a mapping for remaining Vietnamese strings to English
replacements = {
    "KIỂM TOÁN & QUẢN TRỊ": "AUDIT & ADMINISTRATION",
    "Dự kiến băm Hash": "Blockchain Timestamp (Est.)",
    "Tỷ": "Billion",
    "Triệu": "Million",
    "Yêu cầu Truy cập": "Request Access",
    "Xem Teaser": "View Teaser",
    "Mục tiêu": "Target",
    "Thời hạn": "Tenor",
    "Kỳ hạn": "Tenor",
    "Vốn góp": "Equity",
    "TS đảm bảo": "Collateral",
    "Hình thức": "Mode",
    "Khám phá": "Explore",
    "Cá nhân / Thử nghiệm": "Individual / Trial",
    "TỔNG THANH TOÁN / THÁNG": "TOTAL MONTHLY PAYMENT",
    "Dành cho nhà đầu tư cá nhân & nhóm nhỏ": "For individual investors & small teams",
    "Thiết kế cho sự tăng trưởng & quy mô doanh nghiệp": "Designed for growth & business scale",
    "/ THÁNG": "/ MONTH",
    "BẮT ĐẦU DEMO": "START DEMO",
    "TIẾP TỤC": "CONTINUE",
    "Quay lại": "Back",
    "Lưu hồ sơ & Tiếp tục": "Save & Continue",
    "Đặt câu hỏi / Q&A": "Ask a Question / Q&A",
    "ĐANG HOẠT ĐỘNG": "ACTIVE",
    "ĐANG CHỜ": "PENDING",
    "Đã hủy": "Cancelled",
    "Hủy bỏ": "Cancel",
    "Kho hàng / Khoản thu": "Inventory / Receivables",
    "12-18 tháng": "12-18 months",
    "5-7 năm": "5-7 years",
}

for vi, en in replacements.items():
    text = text.replace(vi, en)

# Standardize currency one last time
text = text.replace(' Billion VND', ' Billion <u>đ</u>')
text = text.replace(' Million VND', ' Million <u>đ</u>')
text = text.replace(' Billion VNĐ', ' Billion <u>đ</u>')
text = text.replace(' Billion Billion', ' Billion') # Fix logic error if any

with open(filename, 'w', encoding='utf-8') as f:
    f.write(text)

print("Deep cleaned translations.js")
