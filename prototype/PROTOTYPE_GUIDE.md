# Matcha Capital — Official Prototype Guide

**Matcha Capital** is a next-generation **Capital Infrastructure Platform**. It bridges the gap between high-growth companies (Borrowers) and institutional investors (Lenders) by replacing fragmented email-based fundraising with a secure, **Blockchain-Verified Virtual Data Room (VDR)**.

This guide is designed to help you navigate and demonstrate the 18+ screens of this prototype with maximum impact.

---

## 🚀 Getting Started

1. **Launch the Hub:** Open `index.html` in your browser. This is your "Map" of the entire ecosystem.
2. **Access the Demo:** Click **START DEMO** to reach the role-selection screen (`login.html`).
3. **Role Persistence:** The prototype uses `localStorage` to remember your role. To reset or switch, simply return to the Login screen.

---

## 🎭 The Three User Personas

| Persona | Role in Ecosystem | Key Objective |
|---|---|---|
| **CFO (DRG Internal)** | The Capital Seeker | Structure the deal, upload "Green" proof, and manage lender access. |
| **Investor (Lender)** | The Capital Provider | Discover verified deals, perform due diligence, and submit Term Sheets. |
| **Auditor (Admin)** | The Trust Guardian | Monitor data integrity and detect document tampering using Blockchain. |

---

## 📖 Guided Narrative Walkthrough

### Flow A: The CFO's "5-Minute Fundraising" Journey
*Goal: Move from local spreadsheets to a blockchain-sealed deal room.*

1. **Dashboard (`dashboard.html`):** Start here to see the high-level financial health of the group. Note the **EBITDA** and **DSCR** metrics — these are what lenders crave.
2. **Project Initiation (`create-room.html`):** Walk through the 5-step wizard.
   - *Demo Hack:* Point out Step 5 where the system generates a **Blockchain Hash** for the project concept. This is the first "Proof of Intent".
3. **Document Vault (`upload-docs.html`):** This is the core engine. Documents are organized into 4 critical folders (Legal, Financial, Tech, ESG). 
   - *Key Feature:* Notice the **S1, S2, S3 badges**. This represents **Tiered Privacy** — lenders only see what they have permission for.
4. **Deal Pipeline (`deal-pipeline.html`):** Track progress in a Kanban view. This is where the CFO manages the "Funnel" of interested banks.

### Flow B: The Investor's "Trusted Investment" Journey
*Goal: Find a high-yield green project and verify its claims.*

1. **Marketplace (`deal-discovery.html`):** Browse the listings. 
   - *Key Feature:* **Blind Profiles**. Notice you see "Agri-Materials Group" instead of "Dak Lak Rubber". This protects the borrower's reputation during early outreach.
2. **Verification Center (`verification-center.html`):** Connect to a simulated Bank API to prove **Proof of Funds (POF)**. This filters out "tire-kickers" and ensures only serious capital enters the room.
3. **The Secure Deal Room (`deal-room.html`):** Experience the ultimate privacy. 
   - *Key Feature:* **Watermark & Anti-Download**. Every document has a "CONFIDENTIAL" diagonal overlay. This is a premium security feature for high-stakes finance.
4. **Indicative Offer (`indicative-offer.html`):** Instead of a messy email, the lender submits a **Structured Term Sheet** which is instantly hashed to the ledger.

### Flow C: The Admin's "Zero-Trust" Security Audit
*Goal: Ensure no data tampering has occurred during the deal lifecycle.*

1. **Blockchain Monitor (`blockchain-monitor.html`):** This is the "WOW" screen for technical stakeholders.
   - *The Mismatch:* Notice the **Red Row**. The system has detected that a "Debt Repayment Plan" was modified after being sealed on the blockchain. 
   - *Action:* The Admin can instantly **Suspend the Room** to prevent fraud.
2. **Audit Trail (`audit-trail.html`):** A forensic log of every single click. Every action is tied to a **Blockchain Block Number**, making it legally defensible.

---

## 🛠️ Trust Mechanics (The "Special Sauce")

| Feature | Technical Implementation | Why It Wins Deals |
|---|---|---|
| **SHA-256 Hashing** | Every file generates a unique digital fingerprint. | Eliminates the possibility of "shadow folders" or document swapping. |
| **Tiered Access (T1-T3)** | Logic-gated folders based on NDA status. | Allows the CFO to share a Teaser publicly while keeping the P&L private. |
| **Immutable Ledger** | A simulated transparent log of all transaction hashes. | Provides an "Audit Trail of Truth" for regulators and auditors. |
| **SVG Standard** | Professional, high-contrast iconography. | Replaces amateurish emojis with a high-end corporate fintech aesthetic. |

---

## 🎤 Tips for a Winning Presentation

1. **Start with the Pain Point:** Mention that traditional fundraising takes months of "email ping-pong" and has high fraud risk.
2. **Show, Don't Just Tell:** When you click "Submit" in the Wizard, point out the **Hashing Animation**. It makes the technology feel "alive".
3. **Focus on the "Security Mismatch":** Spend 30 seconds on the **Integrity Monitor**. Explain that if a hacker (or a dishonest employee) changes 1% of a document, the system will turn **Red**. This usually gets the best reaction from stakeholders.
4. **Mention the Branding:** Note the consistent use of **Emerald/Teal accents and Dark-Mode Sidebars** — this was designed to feel like a premium Bloomberg or BlackRock Bloomberg terminal.

--- **Screen Count:** 18 functional screens + 1 Hub + 1 Login = 20 total pages.

---

*Secured by Blockchain · Matcha Capital © 2026*
