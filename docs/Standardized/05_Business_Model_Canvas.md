# 05. Business Model Canvas (BMC) & Revenue Model

Mô hình kinh doanh của nền tảng B2B Capital Infrastructure Platform (Matcha Capital) với tư duy phát triển làm hai giai đoạn (Pilot - Tập trung vào Doanh nghiệp, và Scale - Mở rộng Chợ giao dịch).

---

## I. Business Model Canvas (Giới thiệu Tổng quan)

### 1. Customer Segments (Phân khúc)
*   **Borrowers (Tập đoàn cần vốn):** Tập đoàn mẹ đa ngành quy mô lớn (như DRG), hoặc các SME cần vốn để đẩy capex hoặc vốn lưu động.
*   **Lenders (Người cấp vốn):** Ngân hàng thương mại, Công ty tài chính, Quỹ Đầu tư tư nhân (PE/VC), Nhà đầu tư chiến lược, và các tổ chức tín dụng cấp vốn xanh.

### 2. Value Propositions (Đề xuất Giá trị)
*   **Đối với Doanh nghiệp:** Hệ thống bóc tách hồ sơ gọi vốn chuyên sâu (Multi-deal); Quản lý truy cập Zero-Trust, Giữ vững quyền lực đàm phán; Tăng tốc tìm thấy nguồn tiền phù hợp.
*   **Đối với Lender:** Cung cấp sân chơi (Deal Room) chuẩn hóa, giảm mập mờ thông tin (Asymmetry), chi phí Due diligence cực thấp, tích hợp Blockchain Audit Trail đảm bảo hồ sơ không bị thao túng.

### 3. Channels (Kênh phân phối)
*   Tham gia trực tiếp (Direct Onboarding) cấp tài khoản nội bộ (Giai đoạn Pilot với DRG).
*   Chợ niêm yết có kiểm soát (Public Marketplace nhưng yêu cầu KYC khắt khe).

### 4. Customer Relationships (Quan hệ khách hàng)
*   High-touch Account Management cho việc thiết lập cấu trúc Deal phức tạp lúc đầu.
*   Self-service Workflow Workflow engine (Cơ chế tự động phê duyệt quyền, chấm điểm matching).

### 5. Key Activities (Hoạt động chính)
*   Vận hành Hạ tầng Data Room (Project-based Capital Rooms) & Quyền truy cập.
*   Vận hành Blockchain Node để mã băm tài liệu & Lịch sử log (Audit Trail).
*   Thẩm định AML/KYC/KYB đối tác cấp doanh nghiệp.

### 6. Key Resources (Nguồn lực chính)
*   Phần mềm lõi (Cloud Platform + Security Layer).
*   Mạng lưới Smart Contract / Ledger (Công nghệ chuỗi khối).
*   Relationship Manager (Chuyên gia thấu hiểu cấu trúc tài chính mảng Agri/Năng lượng).

### 7. Key Partners (Đối tác chính)
*   Các Định chế tín dụng (Banks, Funds).
*   Nhà cung cấp điện toán đám mây & Dịch vụ eKYC API (Kết nối hệ thống cổng ngân hàng).

---

## II. Cấu trúc Mô hình Doanh thu (Revenue Model)

Nền tảng sử dụng một biểu đồ phí linh hoạt (Multi-layered revenue model). Việc thu lợi nhuận được dựa trên mốc Milestone để tối đa hóa cam kết (Alignment of Incentives).

### Layer 1: Enterprise Setup Fee (Phí thiết lập ban đầu)
*   **Bên trả phí:** Doanh nghiệp (Borrower - VD: DRG).
*   **Khi nào thu:** Trả 1 lần (One-off) khi Onboarding tạo không gian công ty.
*   **Định mức:** Có thể từ 0.5 - 1 triệu (SMEs) tới 3 - 5 triệu (Đại tập đoàn).
*   **Logic:** Bù lại chi phí Cloud, phân nhóm quyền truy cập. *(Trong giai đoạn Pilot, phí này được Miễn phí/Discount mạnh để thu hút Adoption).*

### Layer 2: Project Room / Upload Fee (Phí hạ tầng Deal Room)
*   **Bên trả phí:** Doanh nghiệp (Borrower). 
*   **Khi nào thu:** Thu mỗi khi tạo một Deal Room mới.
*   **Logic:** Khác với các Data Room truyền thống (như Intralinks) tính phí trên dung lượng 10.000 users hoặc $0.60/page một cách hút máu và khó lường. Ở đây, Matcha Capital thu phí khoán theo tầm vóc Deal. Một Deal Working Capital đơn giản sẽ rẻ hơn một Deal Project Finance 1000 tỷ phức tạp (chia 5-7 cấp Stage).
*   **Project Insight Fee (Tùy chọn cho Lender):** Nếu Lender muốn xem các dữ liệu VIP nằm sâu hơn trong Stage Thẩm định Dữ Liệu Lõi, họ có thể chia sẻ một phần nhỏ phí Room này với Doanh nghiệp để thể hiện sự "Nghiêm túc cọc".

### Layer 3: Success Fee (Chiết khấu Thành công)
*   **Bên trả phí:** Doanh nghiệp (Borrower).
*   **Khi nào thu:** Khi có chữ ký Term Sheet chính thức, hoặc khi Lệnh giải ngân (Disbursement) xuống tiền thật.
*   **Định mức:** Tỷ lệ \% rất nhỏ (VD: 0.01% - 0.1% / Deal size).
*   **Logic:** Đây là nguồn thu khổng lồ và chủ chốt giúp Model có thể Scale vĩ đại. Hỗ trợ khách hàng gọi vốn thành công rồi mới thu phí sẽ giúp xóa bỏ toàn bộ Rào cản thâm nhập (Friction).

### Phase Scale Up (Tương lai)
Giai đoạn sau có thể bổ sung **Premium Analytics** (Dành cho nhà đầu tư cần biểu đồ Dashboard Data), **Subscriptions Fee** hàng năm. Biên lợi nhuận vận hành mục tiêu cho Software Service này là 15-25%.
