# 08. Hành trình Thẩm định của Nhà Đầu Tư (Lender Side)

Tài liệu này mô tả kỹ thuật và luồng hành vi (Specs) dành cho vai trò Nhân vật Cấp vốn (Nhà đầu tư quỹ, Analyst, RM Ngân hàng) trên nền tảng Matcha Capital.

## I. Điểm truy cập An toàn (Trust Anchor & Authentication)

Do bản chất các thông tin tài chính luôn mang tính sống còn và dễ bị "Front-running" hoặc Đánh cắp, Matcha Capital **tuyệt đối không cho phép đăng ký công khai (No open public sign-up)**.

### Banking API / KYC-KYB
*   Mọi Lender muốn tham gia chợ đều phải được xác lập qua một Tổ chức Tài trợ hoặc kết nối thẳng **Banking API Validation**.
*   **Chứng minh Số dư (Proof of Fund):** Chức năng này kết nối sổ cái, chứng minh quỹ này có quỹ đạo giải ngân tối thiểu để tránh các Entity ném đá dò đường (Spies, Phishing). Chỉ khi Số dư được xác lập (Ví dụ > 200 tỷ VND Khả dụng), Lender mới được Set up vào Sector tương ứng với các Đặc quyền lọc Deal hạng A.

## II. Deal Discovery (Khám phá Thị trường)
Khi đã vào thành công sảnh (Marketplace), Lender không bị "ngộp" thông tin giống như rải giấy tờ BCTC giấy.
Hệ thống bố trí dạng Hub-Listing (dạng lưới). Mỗi thẻ Card tương đương 1 Project Vốn.

*   **Bộ lọc Phức hợp (Heuristics Filter):** Lọc theo Số tiền cần, Mục đích giải ngân (Working Capital vs Project Finance), IRR kỳ vọng, Tần suất trả nợ gốc.
*   **Blind Profile (Chân dung Ẩn danh):** Ở giai đoạn này, doanh nghiệp có thể hiển thị dưới dạng "Một tập đoàn Đầu ngành Vật liệu và Nông nghiệp Cây công nghiệp tại Đăk Lăk, VN" thay vì chỉ đích danh DRG (Điều này nhằm bảo vệ danh tiếng CFO khi rải đơn số lượng lớn).

## III. Deal Room & Execution (Quyết định Thẩm định)

Khi một Lender quan sát kỹ 1 Deal Card và quyết định vào sâu:

1.  **Gửi Yêu Cầu Xem Hồ Sơ (Request View):** Lệnh này trỏ thẳng về hộp thư In-app của Internal Borrower (DRG). 
2.  **Xem VDR (Virtual Data Room):** Borrower nhận diện thành công vị Lender này là "Đối tác uy tín" -> Bấm Đồng ý. Lúc này, giao diện Lender bung ra toàn bộ Folder Tree (Pháp lý, Thuế, Báo cáo dòng tiền, Khấu hao tài sản...).
3.  **Tương tác (In-line QA):** Lenders đánh dấu từng ô trong báo PDF, để lại câu hỏi (VD: "Tại sao tồn kho tháng này vọt lên 90 ngày?"). Internal Borrower có một khay Chat Inbox QA trực tiếp trên file, trả lời ngay và đính kèm bằng chứng (Receipt) ngay lập tức.
4.  **Submit Indicative Term Sheet:** Nếu hài lòng, Lender không cần phải gửi mail nháp word dài ngoằng. Trên nền tảng có Module Form điền: "Tỷ lệ Lãi đề xuất: 9.5%/Năm", "Kỳ ân hạn: 6 tháng", "Điều kiện tiên quyết: Cầm cố 10% cổ phẩn công ty con M"...
5.  **Click & Sign:** Sau khi 2 bên đàm phán tới lui trên Dashboard, chốt Deal. Chuyển sang Blockchain ghi nhận Hash => Off-board giải ngân theo quy trình nội bộ Ngân hàng thực tế.
