import os

base_dir = r"d:\Downloads\UX_UI_Design_EN_only\prototype"

index_html = r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Matcha Capital — Prototype Hub</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="shared/styles.css">
    <script src="shared/translations.js"></script>
    <script src="shared/i18n.js"></script>
    <style>
        .map-card { transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); cursor: pointer; border-left: 4px solid transparent; }
        .map-card:hover { transform: translateX(8px); background: #f0fdfa; border-left-color: #0d7377; }
    </style>
</head>
<body class="bg-slate-50 font-['Inter']">
    <div class="max-w-6xl mx-auto px-6 py-12">
        <header class="mb-16 text-center">
            <img src="shared/logo.png" alt="Matcha Capital" class="h-16 mx-auto mb-6">
            <h1 class="text-4xl font-black text-[#0a2e2f] tracking-tight mb-2">MATCHA CAPITAL</h1>
            <p class="text-slate-500 font-medium" data-i18n="hub_subtitle">Bản đồ Prototype Chi tiết — Hệ thống 17 Màn hình</p>
            <div class="mt-8 flex justify-center gap-4">
                <a href="login.html" class="px-8 py-3 bg-[#0d7377] text-white rounded-xl font-bold shadow-xl shadow-teal-900/20 hover:scale-105 transition-all" data-i18n="btn_login">BẮT ĐẦU DEMO (LOGIN)</a>
            </div>
        </header>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-12">
            <!-- Phase A: Internal -->
            <div>
                <h2 class="text-xs font-black text-slate-400 uppercase tracking-[0.3em] mb-6 border-b pb-2" data-i18n="hub_phase_1">01. DRG INTERNAL (INTERNAL)</h2>
                <div class="space-y-3">
                    <div onclick="window.location.href='dashboard.html'" class="card map-card p-4">
                        <div class="flex justify-between items-start mb-1">
                            <h3 class="font-bold text-sm" data-i18n="nav_dashboard">Dashboard</h3>
                        </div>
                        <p class="text-[10px] text-slate-400" data-i18n="hub_desc_dash">Tổng quan tài chính & KPI (EBITDA, DSCR)</p>
                    </div>
                    <div onclick="window.location.href='company-verify.html'" class="card map-card p-4">
                        <div class="flex justify-between items-start mb-1">
                            <h3 class="font-bold text-sm" data-i18n="nav_verify">Company Verify</h3>
                        </div>
                        <p class="text-[10px] text-slate-400" data-i18n="hub_desc_cv">Xác thực MST, GPKD, Định danh DN</p>
                    </div>
                    <div onclick="window.location.href='create-room.html'" class="card map-card p-4 border-l-teal-500 bg-teal-50/20">
                        <div class="flex justify-between items-start mb-1">
                            <h3 class="font-bold text-sm" data-i18n="nav_initiate">5-Step Wizard</h3>
                        </div>
                        <p class="text-[10px] text-slate-400" data-i18n="hub_desc_wizard">Initiate Project (Mục tiêu, Lộ trình, Rủi ro)</p>
                    </div>
                    <div onclick="window.location.href='upload-docs.html'" class="card map-card p-4">
                        <div class="flex justify-between items-start mb-1">
                            <h3 class="font-bold text-sm" data-i18n="nav_vault">Secure Data Room</h3>
                        </div>
                        <p class="text-[10px] text-slate-400" data-i18n="hub_desc_vdr">Folder Tree, Q&A, Audit, KPI Bar</p>
                    </div>
                    <div onclick="window.location.href='distribution.html'" class="card map-card p-4">
                        <div class="flex justify-between items-start mb-1">
                            <h3 class="font-bold text-sm" data-i18n="nav_distribution">Distribution</h3>
                        </div>
                        <p class="text-[10px] text-slate-400" data-i18n="hub_desc_dist">Lender Matching & Private/Public Mode</p>
                    </div>
                    <div onclick="window.location.href='deal-pipeline.html'" class="card map-card p-4">
                        <div class="flex justify-between items-start mb-1">
                            <h3 class="font-bold text-sm" data-i18n="nav_pipeline">Deal Pipeline</h3>
                        </div>
                        <p class="text-[10px] text-slate-400" data-i18n="hub_desc_pipeline">Kanban Board: Approaching → Disbursing</p>
                    </div>
                    <div onclick="window.location.href='permission.html'" class="card map-card p-4 opacity-50">
                        <h3 class="font-bold text-sm" data-i18n="nav_permission">Stage Permissions</h3>
                        <p class="text-[10px] text-slate-400" data-i18n="hub_desc_perm">Quản lý quyền truy cập theo Stage</p>
                    </div>
                </div>
            </div>

            <!-- Phase B: Lender -->
            <div>
                <h2 class="text-xs font-black text-slate-400 uppercase tracking-[0.3em] mb-6 border-b pb-2" data-i18n="hub_phase_2">02. LENDER / INVESTOR SIDE</h2>
                <div class="space-y-3">
                    <div onclick="window.location.href='deal-discovery.html'" class="card map-card p-4 bg-emerald-50/20 border-l-emerald-500">
                        <div class="flex justify-between items-start mb-1">
                            <h3 class="font-bold text-sm" data-i18n="nav_marketplace">Marketplace</h3>
                        </div>
                        <p class="text-[10px] text-slate-400" data-i18n="hub_desc_market">Deal Discovery, IRR/NPV Cards, Filters</p>
                    </div>
                    <div onclick="window.location.href='investor-profile.html'" class="card map-card p-4">
                        <div class="flex justify-between items-start mb-1">
                            <h3 class="font-bold text-sm" data-i18n="nav_profile">Investor Profile</h3>
                        </div>
                        <p class="text-[10px] text-slate-400" data-i18n="hub_desc_profile">Individual vs Institutional Selector</p>
                    </div>
                    <div onclick="window.location.href='verification-center.html'" class="card map-card p-4">
                        <div class="flex justify-between items-start mb-1">
                            <h3 class="font-bold text-sm" data-i18n="nav_verification">Verification</h3>
                        </div>
                        <p class="text-[10px] text-slate-400" data-i18n="hub_desc_verify">KYC/KYB & Bank API Proof-of-Funds</p>
                    </div>
                    <div onclick="window.location.href='deal-room.html'" class="card map-card p-4">
                        <h3 class="font-bold text-sm" data-i18n="nav_vault">Lender Deal Room</h3>
                        <p class="text-[10px] text-slate-400" data-i18n="hub_desc_room">Viewer mode for Data Room docs</p>
                    </div>
                    <div onclick="window.location.href='lender-view.html'" class="card map-card p-4">
                        <h3 class="font-bold text-sm" data-i18n="nav_indicative">Term Sheet Portal</h3>
                        <p class="text-[10px] text-slate-400" data-i18n="hub_desc_ts">Gửi đề xuất vay & Phản hồi</p>
                    </div>
                </div>
            </div>

            <!-- Phase C: Admin -->
            <div>
                <h2 class="text-xs font-black text-slate-400 uppercase tracking-[0.3em] mb-6 border-b pb-2" data-i18n="hub_phase_3">03. AUDIT & ADMIN SIDE</h2>
                <div class="space-y-3">
                    <div onclick="window.location.href='admin-dashboard.html'" class="card map-card p-4 bg-rose-50/20 border-l-rose-500">
                        <div class="flex justify-between items-start mb-1">
                            <h3 class="font-bold text-sm" data-i18n="nav_admin_global">Global Dashboard</h3>
                        </div>
                        <p class="text-[10px] text-slate-400" data-i18n="hub_desc_admin">Traffic, System Health, Global Alerts</p>
                    </div>
                    <div onclick="window.location.href='blockchain-monitor.html'" class="card map-card p-4">
                        <div class="flex justify-between items-start mb-1">
                            <h3 class="font-bold text-sm" data-i18n="nav_integrity">Integrity Monitor</h3>
                        </div>
                        <p class="text-[10px] text-slate-400" data-i18n="hub_desc_integrity">Mismatch Handling & Room Suspensions</p>
                    </div>
                    <div onclick="window.location.href='audit-trail.html'" class="card map-card p-4">
                        <h3 class="font-bold text-sm" data-i18n="nav_audit">Audit Trail</h3>
                        <p class="text-[10px] text-slate-400" data-i18n="hub_desc_audit">Blockchain Block Refs & Access Logs</p>
                    </div>
                    <div onclick="window.location.href='blockchain-ledger.html'" class="card map-card p-4">
                        <div class="flex justify-between items-start mb-1">
                          <h3 class="font-bold text-sm" data-i18n="nav_ledger">B.Chain Explorer</h3>
                        </div>
                        <p class="text-[10px] text-slate-400" data-i18n="hub_desc_ledger">Raw ledger view of transaction hashes</p>
                    </div>
                </div>
            </div>
        </div>

        <footer class="mt-20 pt-8 border-t border-slate-200 flex justify-between items-center text-[10px] font-bold text-slate-400 uppercase tracking-widest">
            <span data-i18n="footer_version">Matcha Capital Prototype v2.0</span>
            <div class="flex gap-4">
                <span class="text-teal-600" data-i18n="footer_secure">Bảo mật bởi Blockchain</span>
            </div>
        </footer>
    </div>
</body>
</html>
"""

login_html = r"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - Matcha Capital</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="shared/styles.css">
    <script src="shared/translations.js"></script>
    <script src="shared/i18n.js"></script>
    <style>
        body {
            background: linear-gradient(135deg, #0a2e2f 0%, #0d7377 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .login-card {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            width: 100%;
            max-width: 450px;
            border-radius: 2rem;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            padding: 3rem;
        }
        .role-btn {
            transition: all 0.3s;
            border: 2px solid #f1f5f9;
        }
        .role-btn:hover {
            border-color: #0d7377;
            background: #f0fdfa;
            transform: translateY(-2px);
        }
    </style>
</head>
<body>
    <div class="login-card text-center">
        <img src="shared/logo.png" alt="Matcha Capital" class="h-16 mx-auto mb-6">
        <h1 class="text-2xl font-black text-[#0a2e2f] mb-2 uppercase tracking-tight" data-i18n="login_welcome">Chào mừng trở lại</h1>
        <p class="text-slate-500 text-sm mb-10" data-i18n="login_select_role">Vui lòng chọn vai trò để trải nghiệm Demo</p>

        <div class="space-y-4 mb-10">
            <button onclick="setRole('internal', 'dashboard.html')" class="w-full role-btn p-4 rounded-2xl flex items-center justify-between group">
                <div class="flex items-center gap-4">
                    <div class="w-10 h-10 bg-slate-100 rounded-xl flex items-center justify-center text-slate-600 group-hover:bg-[#0d7377] group-hover:text-white transition-all">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"></path></svg>
                    </div>
                    <div class="text-left">
                        <p class="text-sm font-black text-[#0a2e2f]" data-i18n="role_internal">DRG INTERNAL</p>
                        <p class="text-[10px] text-slate-400" data-i18n="role_internal_desc">Huy động vốn & Quản lý dự án</p>
                    </div>
                </div>
                <svg class="w-4 h-4 text-slate-300 group-hover:text-[#0d7377]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
            </button>

            <button onclick="setRole('lender', 'deal-discovery.html')" class="w-full role-btn p-4 rounded-2xl flex items-center justify-between group">
                <div class="flex items-center gap-4">
                    <div class="w-10 h-10 bg-slate-100 rounded-xl flex items-center justify-center text-slate-600 group-hover:bg-emerald-600 group-hover:text-white transition-all">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                    </div>
                    <div class="text-left">
                        <p class="text-sm font-black text-[#0a2e2f]" data-i18n="role_lender">LENDER / INVESTOR</p>
                        <p class="text-[10px] text-slate-400" data-i18n="role_lender_desc">Tìm kiếm deal & Đầu tư</p>
                    </div>
                </div>
                <svg class="w-4 h-4 text-slate-300 group-hover:text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
            </button>

            <button onclick="setRole('admin', 'admin-dashboard.html')" class="w-full role-btn p-4 rounded-2xl flex items-center justify-between group">
                <div class="flex items-center gap-4">
                    <div class="w-10 h-10 bg-slate-100 rounded-xl flex items-center justify-center text-slate-600 group-hover:bg-rose-600 group-hover:text-white transition-all">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
                    </div>
                    <div class="text-left">
                        <p class="text-sm font-black text-[#0a2e2f]" data-i18n="role_admin">PLATFORM ADMIN</p>
                        <p class="text-[10px] text-slate-400" data-i18n="role_admin_desc">Giám sát hệ thống & Integrity</p>
                    </div>
                </div>
                <svg class="w-4 h-4 text-slate-300 group-hover:text-rose-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
            </button>
        </div>

        <p class="text-[10px] font-bold text-slate-400 uppercase tracking-widest border-t pt-6" data-i18n="footer_version">Matcha Capital Prototype v2.0</p>
    </div>

    <script>
        function setRole(role, target) {
            localStorage.setItem('drg-role', role);
            window.location.href = target;
        }
    </script>
</body>
</html>
"""

styles_css = r"""/* Lo-fi Design System for DRG Prototype */

:root {
  --primary: #0d7377;
  /* Matcha Teal */
  --primary-hover: #095c5f;
  --bg-main: #f0f4f4;
  /* Slightly teal-tinted background */
  --bg-card: #ffffff;
  --text-main: #0a2d2f;
  /*Deep dark green for text*/
  --text-muted: #5a7a7a;
  --border: #d1dbdb;

  /* Status Colors */
  --status-active-bg: #dcfce7;
  --status-active-text: #166534;
  --status-draft-bg: #f1f5f9;
  --status-draft-text: #475569;
  --status-pending-bg: #fef9c3;
  --status-pending-text: #854d0e;
  --status-closed-bg: #fee2e2;
  --status-closed-text: #991b1b;
}

.sidebar-logo {
  width: 120px;
  height: auto;
  margin-bottom: 1rem;
}

body {
  font-family: 'Inter', sans-serif;
  background-color: var(--bg-main);
  color: var(--text-main);
  line-height: 1.5;
}

/* Base Components */
.card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 0.5rem;
  padding: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.btn {
  display: inline-flex;
  align-items: center;
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  font-weight: 500;
  transition: all 0.2s;
  cursor: pointer;
}

.btn-primary {
  background-color: var(--primary);
  color: white;
}

.btn-primary:hover {
  background-color: var(--primary-hover);
}

.btn-secondary {
  background-color: white;
  border: 1px solid var(--border);
  color: var(--text-main);
}

.btn-secondary:hover {
  background-color: #f1f5f9;
}

/* Sidebar & Header */
.sidebar {
  width: 260px;
  background: #1e293b;
  color: white;
  min-height: 100vh;
  position: fixed;
  left: 0;
  top: 0;
}

.sidebar a {
  display: block;
  padding: 0.75rem 1.5rem;
  color: #cbd5e1;
  text-decoration: none;
  transition: background 0.2s;
}

.sidebar a:hover,
.sidebar a.active {
  background: #334155;
  color: white;
}

.main-content {
  margin-left: 260px;
  padding: 2rem;
}

/* Tables */
.table-container {
  overflow-x: auto;
  background: white;
  border: 1px solid var(--border);
  border-radius: 0.5rem;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th {
  text-align: left;
  padding: 0.75rem 1rem;
  background: #f1f5f9;
  border-bottom: 2px solid var(--border);
  font-size: 0.875rem;
  text-transform: uppercase;
  color: var(--text-muted);
}

td {
  padding: 1rem;
  border-bottom: 1px solid var(--border);
  font-size: 0.875rem;
}

/* Badges */
.badge {
  padding: 0.25rem 0.625rem;
  border-radius: 9999px;
  font-size: 0.75rem;
  font-weight: 600;
}

.status-active {
  background: var(--status-active-bg);
  color: var(--status-active-text);
}

.status-draft {
  background: var(--status-draft-bg);
  color: var(--status-draft-text);
}

.status-pending {
  background: var(--status-pending-bg);
  color: var(--status-pending-text);
}

.status-closed {
  background: var(--status-closed-bg);
  color: var(--status-closed-text);
}

/* Role Theming */
body.role-internal .sidebar {
  background: #0a2e2f;
}

/* Dark Teal for Internal */
body.role-lender .sidebar {
  background: #0d5e3b;
}

/* Dark Green for Lender */
body.role-admin .sidebar {
  background: #1a1a2e;
}

/* Dark Navy for Admin */

/* i18n switcher additional styles */
.lang-btn:hover {
  background: #f0fdfa;
  transform: translateY(-1px);
}

.lang-btn.active {
  background: #0d7377;
  color: white;
}
"""

with open(os.path.join(base_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)

with open(os.path.join(base_dir, "login.html"), "w", encoding="utf-8") as f:
    f.write(login_html)

with open(os.path.join(base_dir, "shared", "styles.css"), "w", encoding="utf-8") as f:
    f.write(styles_css)

print("Restoring sidebar headers in other HTML files...")
files_without_text_white = ["permission.html", "dashboard.html"]

for fname in os.listdir(base_dir):
    if fname.endswith(".html") and fname not in ["index.html", "login.html"]:
        path = os.path.join(base_dir, fname)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Check if the logo tag exists and the h2 tag is missing
        logo_tag = r'<img src="shared/logo.png" alt="Matcha Capital" class="sidebar-logo mx-auto">'
        if logo_tag in content and "Matcha Capital" not in content[content.find(logo_tag):content.find(logo_tag)+150]:
            h2_tag = '\n      <h2 class="text-xl font-bold tracking-tight">Matcha Capital</h2>' if fname in files_without_text_white else '\n      <h2 class="text-xl font-bold tracking-tight text-white">Matcha Capital</h2>'
            content = content.replace(logo_tag, logo_tag + h2_tag)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

print("Restoration script completed.")
