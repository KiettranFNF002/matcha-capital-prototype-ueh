# Matcha Capital — Prototype Walkthrough Guide (Verified Master)

> Tài liệu hướng dẫn thuyết trình và walkthrough sản phẩm cho buổi bảo vệ.
> Đối chiếu 100% với code thực tế và kịch bản thuyết trình.

---

## 🎭 Ba Persona (Vai trò người dùng)

| Persona | Vai trò | Mục tiêu trong Demo |
|---|---|---|
| **CFO (DRG Internal)** | **Borrower** — Bên đi vay/huy động vốn | Cấu trúc deal, tải tài liệu, niêm phong Blockchain |
| **Investor (Lender)** | **Bên cấp vốn** — Ngân hàng/Quỹ | Khám phá deal, thẩm định, nộp Term Sheet |
| **Auditor (Admin)** | **Người giám sát** | Phát hiện giả mạo, bảo đảm tính toàn vẹn dữ liệu |

---

## 🧭 Hub — Điểm xuất phát (`index.html`)
- **Là gì**: Bản đồ toàn bộ 18 màn hình, chia thành 3 cột (Internal / Lender / Admin).
- **Tương tác**: Click "START DEMO" -> `login.html` để chọn vai trò.
- **Lưu ý**: Prototype dùng `localStorage` để nhớ vai trò; quay về Login để đổi sang role khác.

---

## 🏢 Phase 1: Internal View — DRG (Borrower)
*Hành trình của CFO: từ spreadsheet rời rạc -> Deal Room được niêm phong Blockchain.*

### 1. Login (`login.html`)
- Chọn vai trò: Internal / Lender / Admin.
- Hệ thống tự động điều hướng và hiển thị sidebar tương ứng.

### 2. Financial Dashboard (`dashboard.html`)
- Dashboard tổng quan: **EBITDA, DSCR, Portfolio, Success Rate**.
- **Pain Point**: DRG đang phải quản lý nhiều dự án trên nhiều file Excel riêng lẻ.
- **Điểm nhấn**: Chỉ vào chỉ số **DSCR** — đây là thước đo khả năng trả nợ mà Lender quan tâm nhất.

### 3. Company Verification (`company-verify.html`)
- AI tự động trích xuất & đối chiếu Mã số thuế, GPKD với dữ liệu Tổng cục Thuế.
- **Tương tác**: Nhấn "Save & Continue" để xác nhận hồ sơ pháp lý.

### 4. Project Initiation Wizard (`create-room.html`)
- Wizard 5 bước: Phân loại -> Mục tiêu -> Tài chính -> Rủi ro -> Xác nhận.
- **Điểm nhấn**: Bước 5 — Click **"REGISTER ON BLOCKCHAIN"**, xuất hiện hiệu ứng Hashing. Đây là "Dấu ấn tin cậy" đầu tiên.

### 5. Document Vault (`upload-docs.html`)
- Thư mục được chia theo chuẩn: `01_LEGAL`, `02_FINANCIAL`, `03_TECHNICAL`, `04_ESG/EUDR`.
- **Điểm nhấn 1**: Badge **S1/S2/S3** = Quyền truy cập phân tầng (Tiered Privacy).
- **Điểm nhấn 2**: Nút **"SEAL DATA ROOM"** -> Hiệu ứng niêm phong Blockchain (3 pha).
- **Điểm nhấn 3**: Q&A Window và Access Log ngay trong VDR.

### 6. Distribution (`distribution.html`)
- Cấu hình chế độ: **Private** (mời đích danh) hoặc **Public** (niêm yết marketplace).
- **Điểm nhấn**: AI Matching — hệ thống gợi ý Lender dựa trên khẩu vị đầu tư (Green Finance).

### 7. Deal Pipeline (`deal-pipeline.html`)
- Kanban board quản lý tiến độ: Outreach -> Due Diligence -> Term Sheet -> Disbursing.
- **Điểm nhấn**: Bảng so sánh lãi suất và điều kiện giữa các Ngân hàng.

### 8. Permission Management (`permission.html`)
- Ma trận phân quyền chi tiết cho từng Lender theo từng giai đoạn thẩm định.

---

## 🏦 Phase 2: Lender View — Investor/Ngân hàng (Bên cấp vốn)
*Hành trình của Lender: Tìm kiếm cơ hội -> Xác thực năng lực -> Thẩm định sâu.*

### 9. Capital Marketplace (`deal-discovery.html`)
- Danh sách deal dạng card với IRR, Tenor, Risk.
- **Điểm nhấn**: **"Blind Profile"** — Chỉ thấy ngành hàng (Agri-Materials) mà chưa thấy tên DRG để bảo mật danh tiếng.

### 10. Investor Profile (`investor-profile.html`)
- Chọn loại hình: **Cá nhân (HNWI)** hoặc **Tổ chức (Bank/Fund)**.

### 11. Verification Center (`verification-center.html`)
- KYC/KYB + **Proof of Funds (POF)**.
- **Tương tác**: Kết nối Bank API để chứng minh số dư (xác thực năng lực tài chính).

### 12. Lender Deal Room (`deal-room.html`)
- Giao diện xem tài liệu dành cho Lender với Watermark bảo mật.
- **Điểm nhấn 1**: Hiệu ứng **"VERIFYING INTEGRITY"** khi mở file — tự động so khớp Hash với Blockchain.
- **Điểm nhấn 2**: Nhãn trạng thái `[ Verified ]` khẳng định tài liệu an toàn.

### 13. My Deals Portal (`lender-view.html`)
- Quản lý danh mục các dự án đang theo dõi hoặc đã được mời.

### 14. Indicative Offer (`indicative-offer.html`)
- Nộp đề xuất đầu tư (Term Sheet sơ bộ) một cách có cấu trúc và được hash lên ledger.

---

## 🛡️ Phase 3: Admin & Integrity View (Giám sát)
*Hành trình của Admin: Đảm bảo "Zero-Trust" cho toàn hệ thống.*

### 15. Global Dashboard (`admin-dashboard.html`)
- Tổng quan sức khỏe hệ thống: Traffic, Security Alerts, Integrity Status.

### 16. Integrity Monitor (`blockchain-monitor.html`)
- So sánh trực tiếp Local Hash vs Blockchain Hash.
- **Điểm nhấn (Quan trọng nhất)**: Phát hiện lỗi **Mismatch** (Dòng màu đỏ). 
- **Tương tác**: Click **"Suspend Room"** (Đình chỉ) hoặc **"Restore"** (Khôi phục bản gốc).

### 17. Audit Trail (`audit-trail.html`)
- Nhật ký truy cập chi tiết, mỗi hành động gắn với một Block Number trên Blockchain.

### 18. Blockchain Ledger (`blockchain-ledger.html`)
- Sổ cái thô hiển thị các chuỗi mã băm — minh chứng cho tính bất biến.

---

## 🔄 Chiến thuật Walkthrough (7 bước chốt)

1. **Start**: `index.html` (Giới thiệu tầm nhìn hệ thống).
2. **Setup**: `create-room.html` (Khởi tạo deal chuyên nghiệp).
3. **Control**: `upload-docs.html` -> Nhấn **SEAL ROOM** (Khoảnh khắc tạo niềm tin).
4. **Discover**: `deal-discovery.html` (Cách Lender tìm thấy deal mà không lộ danh tính).
5. **Verify**: `deal-room.html` (Tính năng tự động kiểm tra tính vẹn toàn khi xem file).
6. **Detect**: `blockchain-monitor.html` (**Điểm đắt giá nhất**: Phát hiện gian lận số liệu).
7. **End**: `index.html` (Tổng kết giá trị: Bảo mật — Tốc độ — Tin cậy).

---
*Secured by Blockchain · Matcha Capital © 2026*
