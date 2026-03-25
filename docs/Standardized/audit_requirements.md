# Practical Audit Requirements
*Extracted from Fintech Lecturer Feedback Transcripts*

Based on the thorough critique of the previous failed prototype phase, the following foundational rules have been extracted. These must act as our "North Star" during the final audit of the **Matcha Capital** platform.

## 1. Accurate Problem Identification (The "Core Problem")
- **Critique:** The team previously misidentified "information asymmetry" as the bank's problem to solve. The reality is that banks lack the desire to process raw operational data. The actual problem was the borrower's lack of stable, long-term revenue streams to justify long-term credit.
- **Audit Requirement:** Ensure Matcha Capital focuses on solving the *borrower’s* problem—helping them aggregate and summarize their data to prove creditworthiness, rather than forcing the bank into the role of a raw data analyst. 

## 2. Realistic Technology Scope (No "Buzzword Bingo")
- **Critique:** Pitching "Real-time API Integration into Bank Core Systems" is highly unrealistic. Banks maintain closed systems and do not want live sensor data from farms.
- **Audit Requirement:** The platform must act as an independent, secure data room and verification hub (e.g., Blockchain document anchoring). Do not claim direct database integration with banks unless it's a standard Open Banking read-only API (like Plaid for proof-of-funds).

## 3. Focus on a Single "Basic Proposition"
- **Critique:** "Làm nhiều nhưng làm tùm lum tà la" (Doing too much, but haphazardly). The lecturer pointed out that combining too many tech buzzwords (AI, API, Blockchain, Real-time DB) dilutes the solution.
- **Audit Requirement:** Matcha Capital must champion *one* clear workflow: **Streamlining Capital Raising (Deal Preparation -> Data Room -> Lender Matching -> Term Sheet).** Remove any lingering complex, unnecessary features that don’t serve this core pipeline.

## 4. Practical Financial Engineering
- **Critique:** Instead of relying purely on tech to "unlock liquidity," use real financial mechanisms. The lecturer suggested that if the problem is unstable commodity prices, use derivatives or smart-contract-based off-take agreements to lock in prices. 
- **Audit Requirement:** Matcha Capital correctly categorizes projects into "Green Finance," "Capex," and "Trade Finance." Ensure the platform reflects matching lenders based on these specific, viable financial structures.

## 5. Clear, Honest Terminology
- **Critique:** Avoid over-promising phrases like "phá vỡ cấu trúc dữ liệu minh bạch" (breaking transparent data structures) or "cởi trói thanh khoản" (unchaining liquidity) without explaining *how*.
- **Audit Requirement:** Review the platform UI to ensure all copywriting is professional, objective, and realistic. Use terms like "Blockchain Verified Document" rather than "Immutable Real-Time Operations."

---
**Conclusion for Matcha Capital:**
The current 17-screen prototype largely avoids the pitfalls of the previous failure by positioning itself as a secure **VDR (Virtual Data Room)** and **Marketplace** rather than a core banking integration. The final audit must simply verify that the narrative remains tightly focused on Deal Structuring and Document Integrity.
