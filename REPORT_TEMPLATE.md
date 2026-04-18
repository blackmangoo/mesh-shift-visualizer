# 23F-XXXX_A2_Q4_Report

## 1. Introduction (~0.5 page)
- Define circular q-shift: node i sends data to node (i + q) mod p.
- Explain why mesh decomposition helps parallel communication.
- Explain why visualization improves understanding.

## 2. Algorithm Description (~1 page)
Given p = n^2 and q:
- Stage 1 (row shift): each row shifts by q mod n.
- Stage 2 (column shift): each column shifts by floor(q / n).

### Worked Example (p=16, q=5)
- n = 4
- row shift = 5 mod 4 = 1
- col shift = floor(5/4) = 1
- Show before grid, after Stage 1 grid, and final Stage 2 grid.
- Explain movement of sample nodes (for example D0, D5, D15).

## 3. Application Architecture (~0.5 page)
- Components:
  - ControlPanel.py for validated user inputs
  - MeshGrid.py for visualization and animation
  - ComplexityPanel.py for formulas and comparison chart
  - shiftLogic.py for pure algorithm
- Data flow:
  - Input p, q -> validation -> compute states -> render panels.
- State approach:
  - Streamlit reactive rerun + button-triggered animation.

## 4. Complexity Analysis (~1 page)
Formulas:
- Ring steps = min(q, p-q)
- Mesh steps = (q mod sqrt(p)) + floor(q / sqrt(p))

### Comparison Table
| p | q | Ring steps | Mesh steps | Better |
|---|---|------------|------------|--------|
|16|3|3|3|Equal|
|16|5|5|2|Mesh|
|16|7|7|4|Mesh|
|64|3|3|3|Equal|
|64|5|5|5|Equal|
|64|7|7|7|Equal|

Comment on cases where mesh helps more (larger q not near 0).

## 5. Deployment Guide (~0.5 page)
- GitHub:
  - Create public repository.
  - Push code from local machine.
- Streamlit Cloud:
  - Connect GitHub repo.
  - Deploy app using app.py.
  - Copy live URL into README and report.
- Local run:
  - pip install -r requirements.txt
  - streamlit run app.py

## 6. Screenshots (~0.5 page)
Include at least 3 screenshots:
1. Initial state (before shift)
2. Mid-animation (Stage 1 visible)
3. Final state (Stage 2 complete)

Important:
- Ensure live deployment URL is visibly shown in at least one screenshot.

## Final Export
- Export this report as PDF named:
  - 23F-XXXX_A2_Q4_Report.pdf
