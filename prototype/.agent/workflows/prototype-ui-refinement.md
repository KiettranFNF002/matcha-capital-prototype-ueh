---
description: Prototype UI Refinement & Quality Assurance
---

This workflow ensures consistency and professional polish for multi-screen fintech prototypes. Follow these steps to prevent recurring issues seen in high-velocity prototype development.

### 1. Currency & Unit Integrity
// turbo
Run a project-wide search for doubled currency symbols (e.g., `đ đ`, `$ $`, `<u>đ</u> <u>đ</u>`) after any automated localization or formatting changes.
- **Command**: `grep -r "<u>đ</u> <u>đ</u>" prototype/`
- **Fix**: Replace with a single standardized symbol (e.g., `<u>đ</u>`).

### 2. Table Structural Alignment
When modifying tables or deleting columns:
- **Verified Count**: Ensure the number of `<th>` tags in the `<thead>` exactly matches the number of `<td>` tags in every `<tr>` of the `<tbody>`.
- **IP / Placeholder Check**: If a column's data is missing, ALWAYS insert an empty `<td></td>` or a placeholder like `<td>-</td>` to prevent shifted alignment in subsequent columns.

### 3. Role Persistence & Sidebar Sync
For prototypes with multiple user views (Admin, Internal, Lender), prevent "Role Bleeding" by:
- **Explicit Role Script**: Ensuring every HTML file contains a script at the bottom of the `<body>` to force the correct CSS class:
  ```javascript
  const role = localStorage.getItem('drg-role') || 'internal';
  document.getElementById('prototype-body').className = 'role-' + role;
  ```
- **Hub State Reset**: The `index.html` (Hub) should always clear state to ensure a clean walkthrough:
  ```javascript
  localStorage.clear();
  ```

### 4. Direct CSS Asset Validation
// turbo
Check for malformed or placeholder CSS classes in charts, bars, and interactive components.
- **Search Patterns**: `class="0"`, `class="null"`, `class="undefined"`.
- **Fix**: Replace with design system tokens (e.g., `bg-teal-500`, `shadow-sm`).

### 5. Shadow & Elevation Consistency
Ensure all cards and containers use the same shadow intensity (e.g., `shadow-sm`) unless explicitly highlighting a single "active" element. Avoid `shadow-xl` or `shadow-2xl` on static cards in a list/grid view.
