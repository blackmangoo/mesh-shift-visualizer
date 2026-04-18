# Mesh Circular Shift Visualizer (Python + Streamlit)

Interactive web application to simulate circular q-shift on a 2D mesh topology.

## Live Deployment URL
- Add your deployed public URL here after deployment:
- `https://<your-app>.streamlit.app`

## Features
- Input validation for `p` (4 to 64, perfect square only) and `q` (1 to `p-1`)
- Mesh grid rendering (`sqrt(p)` x `sqrt(p)`) with node index + data value
- Stage 1 animation: row shift by `(q mod sqrt(p))`
- Stage 2 animation: column shift by `floor(q / sqrt(p))`
- Before/After state panels: initial, after Stage 1, after Stage 2
- Complexity panel with formulas and mesh vs ring bar chart

## Algorithm
Given `p = n^2` and shift `q`:
- Stage 1 (row): shift each row right by `rowShift = q mod n`
- Stage 2 (column): shift each column down by `colShift = floor(q / n)`

Complexity comparison:
- Ring steps: `min(q, p-q)`
- Mesh steps: `(q mod sqrt(p)) + floor(q / sqrt(p))`

## Project Structure
```text
mesh-shift-visualizer/
├── public/
├── src/
│   ├── components/
│   │   ├── MeshGrid.py
│   │   ├── ControlPanel.py
│   │   └── ComplexityPanel.py
│   ├── utils/
│   │   └── shiftLogic.py
│   ├── App.py
│   └── index.py
├── tests/
│   └── test_shift_logic.py
├── app.py
├── README.md
├── requirements.txt
└── package.json
```

## Local Run
1. Create and activate virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start app:
   ```bash
   streamlit run app.py
   ```
4. Run tests:
   ```bash
   pytest
   ```

## Deployment (Streamlit Community Cloud)
1. Push repository to GitHub (public).
2. Go to Streamlit Community Cloud.
3. Create new app from GitHub repo.
4. Main file path: `app.py`
5. Deploy and copy the public URL into this README.

## Suggested Incremental Commits (for better grading)
1. `chore: initialize project structure and dependencies`
2. `feat: add pure two-stage mesh shift logic with validation`
3. `feat: implement control panel and mesh grid renderer`
4. `feat: add stage-by-stage animation for row and column shift`
5. `feat: add real-time complexity comparison panel with chart`
6. `test: add unit tests for shift logic and formulas`
7. `docs: add deployment guide and assignment-aligned README`
8. `docs: attach screenshots and final live URL`

## Report File Name
- `23F-XXXX_A2_Q4_Report.pdf`

## Screenshots to Add
- Initial state
- Mid-animation state
- Final state with live URL visible in browser
