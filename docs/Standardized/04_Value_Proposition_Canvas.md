# 04. Value Proposition Canvas (VPC)

*Bản đồ Giá trị (Value Map) kết nối trực tiếp những Nỗi đau (Pains) và Khát vọng (Gains) của hai nhóm khách hàng cốt lõi được định nghĩa trong JTBD.*

## 1. VPC cho Doanh nghiệp (Capital Seeker: DRG)

### The Problem (Customer Profile)
CFO đang cố gắng giải quyết một **Jobs-to-be-Done**: Cần đóng gói hồ sơ tài chính riêng biệt cho từng loại dự án để huy động vốn, mà không để lộ các dữ liệu nhạy cảm hoặc báo cáo tài chính tổng hợp (đang có dấu hiệu âm dòng tiền) của cả tập đoàn.

*   **Pains:** Dữ liệu phân mảnh; Tốn thời gian làm hồ sơ thủ công nhưng vẫn bị định giá sai lệch (Mispricing); Căng thẳng rủi ro lộ lọt thông tin nhạy cảm.
*   **Gains:** Muốn chia sẻ thông tin có kiểm duyệt, muốn tăng tốc độ ra quyết định của hội đồng tín dụng, muốn tách biệt rủi ro để đàm phán lãi suất vay (Debt) hoặc mức độ pha loãng cổ phần (Equity) tốt nhất.

### The Solution (Pain Relievers & Gain Creators)
Giải pháp là **Project-based Capital Rooms (Phòng gọi vốn theo dự án)** trên nền tảng Matcha Capital.

#### A. Pain Relievers (Thuốc giảm đau)
1.  **Duy nhất 1 nguồn sự thật (Single Source of Truth):** Quản lý tập trung tài liệu bằng Folder Tree, không còn cảnh gửi đi gọi lại version email sai sót.
2.  **Khóa chia sẻ bảo mật (Permissioned Access):** Cấp quyền truy cập theo từng Stage (Sơ loại, Thẩm định, Ký kết). Lenders xem gì, tải được hay không đều bị kiểm soát cứng (Watermark / View-only).
3.  **Audit Trail (Nhật ký truy cập):** Có cơ chế lưu vết lịch sử mọi cú click, mọi lần view tài liệu để dễ dàng truy xuất dấu vết rò rỉ hoặc đánh giá mức độ quan tâm của Lender (Ai đang xem file định giá nhiều nhất?).

#### B. Gain Creators (Yếu tố tạo ra giá trị gia tăng)
1.  **Kanban Deal Pipeline:** Bảng theo dõi tiến độ từng deal (Tiếp cận -> Thẩm định -> Offer -> Giải ngân), tiết kiệm thời gian tổng hợp báo cáo gửi HĐQT.
2.  **Indicative Offer Workflow:** Tích hợp tính năng nhận và phản hồi Term Sheet trực tiếp. Loại bỏ hàng tháng trời thương thảo hợp đồng không rõ ràng.
3.  **Isolation:** Tách bạch câu chuyện rủi ro. Mảng Nhà máy sản xuất có thể được "đóng gói" sạch đẹp đi chào các Quỹ xanh (Green Finance) độc lập hoàn toàn với khoản lỗ từ chuỗi Khách sạn Dakruco do công ty mẹ quản lý.

---

## 2. VPC cho Nhà Đầu tư (The Lender / Investor)

### The Problem (Customer Profile)
Các Ngân hàng Đầu tư và Quỹ tư nhân liên tục tìm kiếm các mỏ vàng cấu trúc (Deal Sourcing). Châm ngôn của họ là "Time is money". 

*   **Pains:** Chi phí Due Diligence quá đắt; Hồ sơ doanh nghiệp sơ sài, nộp thiếu, dữ liệu mập mờ, mất công người đi rà soát và đối chiếu chứng từ (Information Asymmetry). Lệch pha khẩu vị rủi ro với Project.
*   **Gains:** Đòi hỏi dữ liệu chuẩn, tin cậy, ra quyết định cực nhanh. Cần một Deal Room có đầy đủ mọi thứ bày sẵn trên mâm.

### The Solution (Pain Relievers & Gain Creators)
Giải pháp là **Capital Marketplace & Standardized Deal Room (Chợ Vốn & Phòng Thẩm định Chuẩn hóa)**.

#### A. Pain Relievers (Thuốc giảm đau)
1.  **Chuẩn hóa Data (Standardized Data Room):** Cấu trúc Data Room 04 thư mục (General - Financial - Legal - ESG) được validate trước từ nền tảng. Khi vào xem là đủ ngay hồ sơ, tiết kiệm 50% chi phí Audit và Analyst.
2.  **Bộ lọc theo khẩu vị (Matching Engine):** Lender có thể lọc nhanh các Deals theo Sector, Expected IRR (Lợi suất dự kiến), NPV, hoặc Loan Size để tránh lãng phí thời gian vào dự án không khớp khẩu vị dải rủi ro.

#### B. Gain Creators (Yếu tố tạo ra giá trị gia tăng)
1.  **Kiểm chứng Blockchain (Blockchain Integrity):** Tự động băm mã Hash SHA-256 các tài liệu lõi và lưu trên Ledger. Bất cứ hành vi "đánh tráo" hồ sơ tài chính nào đều bị hệ thống phát hiện Mismatch. Lender hoàn toàn tin tưởng 100% vào tệp tin trước mặt họ.
2.  **Q&A Nội tuyến:** Công cụ trao đổi câu hỏi Q&A trực tiếp ngay trên từng file báo cáo, không còn cảnh phải list hàng chục câu hỏi ra file Excel đi gửi qua lại. Rút ngắn Due Diligence.
