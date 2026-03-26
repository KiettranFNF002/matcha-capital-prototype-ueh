# Matcha Capital — Prototype Guide

**Matcha Capital** is a Capital Infrastructure Platform that connects companies seeking capital (Borrowers) with institutional investors (Lenders) through a secure, blockchain-verified Virtual Data Room (VDR) and Deal Marketplace. This guide walks you through all 18 screens.

---

## How to Start

1. Open `index.html` — this is the **Visual Hub** showing the full prototype map.
2. Click **START DEMO (LOGIN)** to enter the role selection screen.
3. Choose one of three roles. Each role unlocks a different set of screens via the sidebar.

---

## Three Roles Explained

| Role | Who They Are | What They Do |
|---|---|---|
| **DRG Internal** | CFO / Finance team of the borrowing company | Create deal rooms, upload documents, manage capital raising |
| **Lender / Investor** | Banks, PE funds, green finance institutions | Discover deals, conduct due diligence, submit term sheets |
| **Platform Admin** | Matcha Capital system administrators | Monitor system integrity, detect document fraud via blockchain |

> **Technical Note:** Roles are stored in `localStorage`. Each screen sets its own role to ensure the correct sidebar navigation appears. The sidebar dynamically shows/hides menu items based on the active role using CSS classes (`.internal-only`, `.lender-only`, `.admin-only`).

---

## Screen-by-Screen Breakdown

### HUB & LOGIN (Shared)

#### 1. Hub (`index.html`)
**Purpose:** High-level overview map of the entire prototype, organized by role. Serves as the "table of contents" for stakeholder demonstrations.
- **Logo:** White version for dark background branding.
- **Role Cards:** Three columns (Internal / Lender / Admin) with clickable links to each screen.
- **Footer:** "Secured by Blockchain" — reinforces the platform's core trust proposition.

#### 2. Login (`login.html`)
**Purpose:** Simulates role-based authentication. In a real system, this would integrate with Banking API for KYC/KYB verification.
- **Three Role Buttons:** Each navigates to the default landing page for that role and stores the role in `localStorage`.
- **Logo:** Dark version for light background contrast.

---

### GROUP 1: DRG INTERNAL (Borrower — 7 Screens)

> *These screens represent the CFO's journey: from verifying the company, to creating a deal, uploading documents, distributing to lenders, and tracking progress.*

#### 3. Dashboard (`dashboard.html`)
**Purpose:** The CFO's command center — a real-time overview of the company's financial health and active capital-raising activities.
- **Financial Summary Cards:** Debt/Equity ratio, EBITDA, DSCR — key metrics lenders will evaluate.
- **Active Deals Table:** Shows project names, target amounts, committed capital, and status. Allows CFO to quickly assess which deals need attention.
- **Notifications Panel:** Recent activities (lender requests, document uploads) to keep CFO informed.

#### 4. Company Verify (`company-verify.html`)
**Purpose:** KYC/KYB for the borrowing company itself. Before creating any deal, the company must prove its legitimacy.
- **Business Registration Input:** Tax ID (MST) and business license (GPKD) fields.
- **AI Data Extraction:** Simulates automated document parsing to reduce manual data entry.
- **Verification Status:** Shows blockchain-anchored verification result with hash.

#### 5. Initiate Project (`create-room.html`)
**Purpose:** The 5-step wizard for creating a new capital request. This mirrors the real-world process of structuring a fundraising pitch.
- **Step 1 — Classification:** Project name, capital structure type (Green Finance, Working Capital, Trade Finance, Investment Capital), funding type (Debt/Equity/Hybrid), and purpose of funds.
- **Step 2 — Capital Needs:** Total ask (slider from 10B–1,000B đ), use of funds breakdown, disbursement method (lump-sum or milestone-based).
- **Step 3 — Timeline & Cash Flow:** Disbursement dates, grace period, payback period, and financial metrics (IRR, NPV, DSCR).
- **Step 4 — Target Investors:** Appropriate investor types (Banks, PE, Green Funds, FDI) and key risk factors with severity badges.
- **Step 5 — Confirmation:** Project summary review and blockchain registration with a live SHA-256 hashing animation.
- **Post-Submit Navigation:** Links to Document Vault, Distribution, and Deal Pipeline for next steps.

#### 6. Document Vault / Secure Data Room (`upload-docs.html`)
**Purpose:** The core VDR where borrowers manage all confidential project documents. This is the "single source of truth" that replaces scattered email attachments.
- **Project Header Bar:** Shows target amount, committed capital, interested lenders, and remaining days.
- **4-Folder Structure:** Legal, Financial, Technical, ESG/EUDR — standardized for due diligence efficiency.
- **Document Table:** File names, stage badges (S-1, S-2, S-3 representing tiered access levels), compliance status, blockchain hash verification, and action buttons (View/Delete).
- **Lender Management Panel:** Shows which lenders have signed NDAs and which are pending.
- **Q&A Window:** Inline discussion per document — replaces back-and-forth email chains.
- **Access Log (Audit):** Timestamped log of every view, upload, and stage change — CFO can see exactly who viewed what and when.
- **Action Bar:** "Seal Data Room" (lock), "Export Report", and "Issue Deal" (send to distribution).

#### 7. Distribution (`distribution.html`)
**Purpose:** Controls how and to whom the deal is published — private targeted invitations or open marketplace listing.
- **Distribution Modes:** Private (targeted lender list) or Public (marketplace visible).
- **Lender Matching Engine:** Suggests suitable lenders based on deal characteristics.
- **Outreach Tracking:** Status of each invitation (sent, opened, responded).

#### 8. Deal Pipeline (`deal-pipeline.html`)
**Purpose:** Kanban-style board tracking all deals from first contact to disbursement — the CFO's portfolio management view.
- **Pipeline Columns:** Draft → Data Gathering → Active Pitching → Term Sheet Issued → Closed.
- **Deal Cards:** Each card shows project name, amount, and current stage.
- **Drag-and-Drop (Simulated):** Visual representation of deal progression.

#### 9. Permissions (`permission.html`)
**Purpose:** Granular access control for the secure data room — determines what each lender can see at each stage of the due diligence process.
- **Group Permissions:** Defines access levels per lender group.
- **Stage-Based Access:** Tier 1 (Public Synopsis), Tier 2 (Basic Financials), Tier 3 (Full VDR with NDA).
- **Download Controls:** Block direct downloads, enforce view-only with watermark.

---

### GROUP 2: LENDER / INVESTOR (6 Screens)

> *These screens represent the investor's journey: from verifying their identity, to discovering deals, entering data rooms, and submitting term sheets.*

#### 10. Marketplace (`deal-discovery.html`)
**Purpose:** The "deal supermarket" — a curated listing of all available capital requests.
- **Filter Bar:** Sector (Rubber/Solar/Agri), Type (Loan/Equity), Risk Rating, Green Deals toggle.
- **Deal Cards:** Each shows badge (Green Finance, Low Risk, High Growth, Cross-Border), project name with blind profile (identity hidden at Tier 1), financial metrics (Target, IRR, EBITDA, Tenor, Collateral), and action buttons (View Teaser, Request Access).
- **Blind Profile Design:** Companies appear as "Agri-Materials Group — Highlands, VN" rather than by real name — a critical privacy feature for the CFO.

#### 11. Investor Profile (`investor-profile.html`)
**Purpose:** Lender self-classification — determines their investment appetite and capability.
- **Profile Type:** Individual vs. Institutional investor.
- **Investment Preferences:** Preferred sectors, deal sizes, risk tolerance.

#### 12. Verification Center (`verification-center.html`)
**Purpose:** KYC/KYB for lenders — ensures only accredited investors access confidential deal rooms.
- **Banking API Connection:** Simulates Proof-of-Funds verification.
- **Accreditation Status:** Shows verified credentials and approved sectors.

#### 13. Deal Room (`deal-room.html`)
**Purpose:** The lender's view of a specific project's secure data room — with view-only protections.
- **Watermark Overlay:** "CONFIDENTIAL · VIEW ONLY" diagonal watermark across the document area — prevents unauthorized sharing.
- **Document List:** Files with blockchain verification badges.
- **Version History:** Track document changes (V1.0 Draft → V2.1 Review → V3.0 Final).
- **"Need More Access?" Panel:** Request Full Access (leads to Pricing) or Ask a Question (Q&A).
- **Immutable Hash Display:** Shows the blockchain hash for the current document set.

#### 14. My Deals (`lender-view.html`)
**Purpose:** Portfolio management for the lender — tracks all deals they're participating in.
- **Active Deals:** Deals the lender has requested or been granted access to.
- **Request Status:** Pending, Approved, or Rejected.
- **Term Sheet History:** Previously submitted offers.

#### 15. Indicative Offer (`indicative-offer.html`)
**Purpose:** Structured form for submitting a term sheet — replaces informal email negotiations.
- **Term Sheet Fields:** Proposed interest rate, grace period, conditions precedent (e.g., collateral requirements).
- **Blockchain Anchoring:** Submitted term sheet is hashed and recorded on-chain.

---

### GROUP 3: ADMIN / AUDIT (4 Screens)

> *These screens represent the platform administrator's oversight role: ensuring system integrity and detecting any data tampering.*

#### 16. Admin Dashboard (`admin-dashboard.html`)
**Purpose:** Platform-wide health overview — the control tower for Matcha Capital operations.
- **Global Stats:** Total live deals, total capital raised, active lenders, security alerts.
- **Deals Monitoring Table:** Lists projects requiring attention, with blockchain status (Green/Warning) and latest activity.
- **System Traffic Chart:** Visual representation of platform usage over time.
- **Engine Logs:** Real-time system event feed (logins, verifications, warnings).

#### 17. Integrity Monitor (`blockchain-monitor.html`)
**Purpose:** The heart of Matcha Capital's trust proposition — automated detection of document tampering.
- **Mismatch Detection:** Shows documents where the current file hash doesn't match the on-chain record.
- **Room Suspension:** Ability to suspend a deal room when fraud is detected.
- **Lender Notification:** Alert system to notify lenders when integrity is compromised.

#### 18. Audit Trail (`audit-trail.html`)
**Purpose:** Comprehensive activity log with blockchain block references — ultimate accountability.
- **Event Log:** Every user action (view, upload, download attempt, access grant) timestamped and linked to a blockchain block.
- **Filter & Search:** By user, action type, date range, or deal room.
- **Block References:** Each event shows its corresponding blockchain block number for independent verification.

#### 19. Blockchain Ledger (`blockchain-ledger.html`)
**Purpose:** Raw on-chain transaction viewer — technical proof that the blockchain layer is real and functional.
- **Chain Stats:** Total blocks, documents anchored, mismatches detected, last block time.
- **Transaction Log:** SHA-256 hashes for every on-chain event, color-coded by type (DOC=Document, ACC=Access, OFR=Term Sheet, ERR=Mismatch).
- **Mismatch Highlighting:** Red-highlighted rows showing expected vs. actual hash values — demonstrates the fraud detection mechanism.
- **Pagination:** Standard table pagination for browsing historical records.

---

### BONUS SCREEN

#### 20. Pricing (`pricing.html`)
**Purpose:** Demonstrates the platform's revenue model — a critical component of the Business Model Canvas presented to the class.
- **Pro Plan (500,000đ/month):** 1 deal room, 100 investor cap, basic analytics, screenshot protection.
- **Business Plan (3,000,000đ/month):** 3 deal rooms, unlimited investors, custom deal structuring, investor matching, priority support.
- **No Annual Commitment:** Flexible SaaS model.

---

## Core Technology Features

| Feature | What It Does | Why It Matters |
|---|---|---|
| **Blockchain Hashing (SHA-256)** | Every uploaded file is hashed and the hash is stored on an immutable ledger | Prevents document tampering; any file change creates a detectable mismatch |
| **Stage-Based Access (Tier 1-3)** | Documents unlock gradually as the lender progresses through due diligence | Protects sensitive data; reveals information only when trust is established |
| **Watermark & View-Only** | Documents display a diagonal watermark and block direct downloads | Prevents unauthorized distribution of confidential financial data |
| **Blind Profile** | Company identity hidden at Tier 1 marketplace level | Protects CFO's reputation during mass outreach to multiple lenders |
| **Q&A Inline Discussions** | Questions posted directly on document context | Eliminates email chain confusion; keeps all communication auditable |
| **Audit Trail** | Every click, view, and action is logged with timestamps | CFO knows exactly who viewed what, and for how long |
| **Role-Based Navigation** | Sidebar dynamically shows only relevant screens per role | Clean UX; users see only what they need for their workflow |

---

## Navigation Tips

- **Back to Hub:** Available on every screen's sidebar — returns to the visual overview.
- **Role Switching:** Return to `login.html` to switch between Internal, Lender, and Admin views.
- **Screen Count:** 18 functional screens + 1 Hub + 1 Login = 20 total pages.

---

*Secured by Blockchain · Matcha Capital © 2026*
