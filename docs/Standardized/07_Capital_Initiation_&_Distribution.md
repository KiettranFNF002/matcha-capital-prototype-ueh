# 07. Sáng kiến Hệ thống Vốn & Data Room (Internal Side)

Đây là tài liệu phân tích luồng Thao tác của Vai trò Borrower (Đại diện: Ban Kế toán / CFO của DRG) trên Matcha Capital. Vai trò này tập trung vào 2 tính năng độc quyền lõi: Wizard Khởi tạo Dự án và Secure Data Room.

## I. Project Initiation Wizard (Luồng khởi tạo dự án)
Quá trình khởi chạy (Pitching) một Dự án Mới đòi hỏi chuẩn hóa cực độ để khớp với kỳ vọng của Ngân hàng / Lenders. Giao diện được tách nhỏ thành Wizard 5 bước:

1.  **Fund Ask & Type (Khởi tạo Cấu trúc vốn):** Khai báo quy mô và thể loại (Ví dụ: Working Capital 50 tỷ, Capex Nhà máy 150 tỷ, Green Finance...). 
2.  **Use of Funds (Mục đích Sử dụng):** Phải làm rõ (Có thể đính kèm Hóa đơn/Bảng báo giá từ NCC) số tiền sẽ chạy vào Máy móc bao nhiêu, Lương chuyên gia bao nhiêu... thay vì báo cáo chung chung.
3.  **Timeline & Cashflow (Lộ trình & Dòng tiền):** Các mốc giải ngân (Disbursement) dự kiến và thời gian sinh dòng tiền thu lại (Ramp-up Time để trả lãi). Đảm bảo Cashflow Forecast nằm theo định dạng chung.
4.  **Target Investors (Mục tiêu Nhà Đầu Tư):** Borrowers định hình rõ họ muốn mời Sector nào (Ngân hàng, Quỹ Hưu trí, FDI) dựa trên rủi ro của mình.
5.  **Review & Submit (Xác thực Cuối):** Kiểm tra, nạp lên khối Blockchain. Gán Smart Contract Hash.

## II. Secure Data Room & Deal Distribution (Phòng Dữ Liệu Ảo)
*Yếu tố quyết định sự tự tin của DRG khi gọi vốn (Pains Relief: Risk Isolation).*

### 1. Phân mảnh Thư mục (Categorized Vaults)
*   Mọi dự án đều chia theo 4 Folder lõi chuẩn tắc của thị trường Due Diligence (Financial - Legal - General - Operational/ESG). 
*   Borrower sử dụng hệ thống Tải hàng loạt (Drag & Drop).

### 2. Phân quyền đa Tầng (Multi-tiered Access Permission)
Nền tảng sử dụng một quy chuẩn Cấp phép "Theo yêu cầu duyệt":
*   **Tier 1 (Public Synopsis):** Bất cứ Lenders nào vượt rào KYC (qua Bank API) đều nhìn thấy One-pager, Số tiền cần huy động, Lĩnh vực. Chưa nhìn được tên Công ty mẹ (Blind-name).
*   **Tier 2 (Basic Info):** Khi bấm "Request basic info", nếu được CFO cấp, họ thấy BCTC tổng (Audit) nhưng chưa thấy Chi tiết Thẻ phân bổ ngân sách.
*   **Tier 3 (Deep Audit VDR):** Cấp quyền cực đoan, thường được CFO cung cấp kèm theo NDA kỹ thuật số. Lender thấy hết dòng tiền trần, invoice nội bộ, lịch sử nộp thuế. Cấm Tải Xuống Trực tiếp, bật cơ chế View-Only ngầm hóa Watermark qua IP tĩnh của Lender đó.

### 3. Distribution & Pipeline Kanban
Borrower dễ dàng quản trị 15 Deals đang rải rác đàm phán thông qua 1 màn hình kéo thả Kanban (Pipeline Tracker). Tracking chính xác các trạng thái (Draft, Data Gathering, Active Pitching, Term Sheet Issued, Closed).

Hệ thống cung cấp cho CFO cái nhìn tổng quát: "Tuần này Ngân hàng A, B, C đã xem thư mục Pháp lý tới % nào, ở lại bao lâu?", từ đó gọi điện thúc giục đàm phán với vị thế chủ động.
