# 09. Bảo mật, Quản trị & Cơ chế Blockchain (Admin Side)

Để Value Proposition của toàn bộ nền tảng (Minh bạch tuyệt đối, Giảm sát phạt Due Diligence) thực sự thành hiện thực, Matcha Capital yêu cầu một kiến trúc bảo mật trung gian mạnh mẽ đóng vai trò là "Kẻ giám sát và Niềm tin" (System Authority & Trust Machine). Đó là Role: **Admin / System Guard**.

## I. Global Dashboard (Trung tâm Điều phối)
Với Admin quản trị hệ thống, họ có trách nhiệm quan sát toàn bộ sức khỏe nền tảng chứ không được quyền "can thiệp sửa số".

1.  **Giám sát Volume:** Thống kê luồng gọi vốn toàn thị trường diễn ra trên App (Bao nhiêu Deal Active, Bao nhiêu Lenders đang Onboarded, Tổng Demand vốn...).
2.  **Quản trị Tài khoản (User Governance):** Admin phê duyệt dứt điểm hoặc thu hồi khẩn cấp quyền truy cập của một Lender có biểu hiện bất thường trên Banking API hoặc nghi ngờ Spam Request tới các Borrowers. Chặn đứng đường dây Rò rỉ danh tính công ty.

## II. Cơ chế Blockchain (Toán học trở thành Luật)

Khác biệt cốt lõi nhất của Matcha Capital so với Dropbox hay Google Drive là việc Tích hợp Blockchain làm Lớp xác thực Dữ liệu (Layer 1 Integrity). Lenders không còn lo ngại CFO "Photoshop" chênh lệch số giữa các quý. 

### Cách thức hoạt động của "Audit Trail & Integrity Monitor"
Khi DRG tải lên hệ thống một file PDF (Ví dụ: `BCTC_Q3_2025.pdf`), hệ thống không nhét thẳng cục File (dung lượng lớn) lên On-chain (vô cùng tốn phí gas do Blockchain nghẽn). Thay vào đó, nó chạy cơ chế sau:

1.  **Thuật toán Băm (Hashing):** Ngay khi File chạm Cloud, hệ thống tính toán (Hash SHA-256) nội dung PDF ra một chuỗi cực độ như `0x9c3f4a...`.
2.  **Lưu Hash (Immutability):** Chuỗi `0x...` này cộng thêm Thời gian chính xác (Timestamp) + Chữ ký số của Kế toán trưởng được nạp thẳng lên Smart Contract. Nó tồn tại vĩnh viễn và không thể sửa chữa.
3.  **Check Mismatch liên tục:** 
    *   Giả sử 3 tháng sau, do làm ăn thua lỗ khoản dự án B, một kế toán vào Server ngầm **ghi đè (override)** 1 trang của file PDF cũ, sửa con số Tồn Kho.
    *   Hệ thống Blockchain Integrity Monitor định kỳ (Cron jobs) chạy lệnh quết lại Hash tài liệu và đối soát chữ ký ban đầu `0x9c3f4a...`.
    *   Nhận thấy Mismatch dữ liệu do File mới bị đổi nội dung -> **Cảnh báo Đỏ (Red Alert)** báo thẳng về Admin Dashboard `Mismatch Detected in DRG_Q3.pdf`. Từ đó, Admin hoặc hệ thống cảnh báo auto tới các Lenders đang xem File đó, đánh sập uy tín (Credit Reputation) của Doanh nghiệp.

Nhờ có *Luật răn đe Toán học* này, các CFO (Borrowers) tuyệt đối không lừa đảo được trên File. Lenders thì cực kỳ yên tâm, tiết kiệm cả đống tiền thuê người Audit lại từ đầu. Sự tin tưởng là Nền tảng luân chuyển dòng Vốn (Capital Moving Layer).
