# Matcha Capital — Prototype Guide (v2.0)

Hướng dẫn vận hành bản mẫu Premium (17 màn hình) dành cho dự án Matcha Capital.

## 1. Cơ cấu Vai trò (Demo Roles)
Hệ thống sử dụng `localStorage` để mô phỏng 3 vai trò chính. Truy cập qua `login.html`:

- **DRG Internal:** Quản lý dự án, Huy động vốn.
- **Lender / Investor:** Tìm kiếm dự án, Thẩm định, Đầu tư.
- **Admin / Audit:** Giám sát hệ thống, Bảo mật Blockchain.

---

## 2. Bản đồ 17 Màn hình (Prototype Map)

### Nhóm 1: DRG Internal (Chủ đầu tư)
1. **Dashboard (`dashboard.html`):** Tổng quan tài chính (Debt/Equity, EBITDA, DSCR) và trạng thái các deal.
2. **Company Verify (`company-verify.html`):** Xác thực MST, GPKD, AI trích xuất dữ liệu.
3. **Initiate Project (`create-room.html`):** Wizard 5 bước (Phân loại → Mục tiêu → Tài chính → Lộ trình → Rủi ro).
4. **Document Vault (`upload-docs.html`):** Secure Data Room với Folder Tree, Q&A, KPI Bar, Audit Logs.
5. **Distribution (`distribution.html`):** Phát hành Private/Public & Hệ thống Lender Matching.
6. **Deal Pipeline (`deal-pipeline.html`):** Kanban theo dõi tiến độ từ Tiếp cận đến Giải ngân.
7. **Permissions (`permission.html`):** Quản lý quyền truy cập theo Group và Stage (Sơ loại, Thẩm định).

### Nhóm 2: Lender / Investor (Nhà đầu tư)
8. **Marketplace (`deal-discovery.html`):** Khám phá deal với bộ lọc ngành hàng và chỉ số tài chính (IRR, NPV).
9. **Investor Profile (`investor-profile.html`):** Chọn tư cách đầu tư Individual vs Institutional.
10. **Verification Center (`verification-center.html`):** KYC/KYB và kết nối Bank API để xác thực Proof of Funds.
11. **Deal Room (`deal-room.html`):** Giao diện xem tài liệu dành cho Lender (có Watermark & Chống tải xuống).
12. **My Deals (`lender-view.html`):** Quản lý danh mục đầu tư và các yêu cầu đang xử lý.
13. **Indicative Offer (`indicative-offer.html`):** Form gửi đề xuất điều khoản vay (Term Sheet).

### Nhóm 3: Admin / Audit (Quản trị & Giám sát)
14. **Global Dashboard (`admin-dashboard.html`):** Giám sát lưu lượng, sức khỏe hệ thống và cảnh báo bảo mật.
15. **Integrity Monitor (`blockchain-monitor.html`):** Đối chiếu mã băm Blockchain, xử lý Mismatch & Đình chỉ Room.
16. **Audit Trail (`audit-trail.html`):** Nhật ký truy xuất chi tiết với tham chiếu Block (Blockchain Block Refs).
17. **Blockchain Ledger (`blockchain-ledger.html`):** Xem danh sách các giao dịch băm mã hóa thô trên sổ cái.

---

## 3. Công nghệ Core (Key Features)
- **Blockchain Hashing:** Mỗi file tải lên được băm (Hash) và lưu trên sổ cái để chống gian lận.
- **Stage-based Access:** Tài liệu được mở khóa dần theo tiến độ thẩm định (Stage 1-3).
- **Secure Data Room:** Chống copy (Watermark), ghi nhật ký từng giây truy cập.
- **Multilingual Support:** Hỗ trợ song ngữ Anh/Việt trên toàn bộ 17 màn hình với nút chuyển đổi linh hoạt.
- **Teal Design System:** Sử dụng bảng màu Matcha Capital (Teal & Dark Green).

---
*Lưu ý: Bạn có thể quay lại trang chủ bất cứ lúc nào qua nút "Back to Hub" ở Sidebar.*
