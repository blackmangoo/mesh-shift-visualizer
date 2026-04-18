from __future__ import annotations

import time
from math import isqrt
from typing import List

import streamlit as st

Grid = List[List[str]]


def _build_cell_html(index: int, value: str) -> str:
    return (
        "<div style='border:1px solid #2d4059;border-radius:10px;padding:10px;background:#f9f7f7;"
        "text-align:center;min-height:64px;display:flex;flex-direction:column;justify-content:center;'>"
        f"<div style='font-size:12px;color:#112d4e;'>Node {index}</div>"
        f"<div style='font-size:18px;font-weight:700;color:#3f72af;'>{value}</div>"
        "</div>"
    )


def render_grid(title: str, grid: Grid) -> None:
    st.subheader(title)
    n = len(grid)
    for r in range(n):
        cols = st.columns(n)
        for c in range(n):
            index = r * n + c
            cols[c].markdown(_build_cell_html(index, grid[r][c]), unsafe_allow_html=True)


def render_stage_arrows(n: int, row_shift: int, col_shift: int, stage: int) -> None:
    if stage == 1:
        direction = "->" if row_shift > 0 else "(no movement)"
        st.info(f"Stage 1: Row Shift by {row_shift} position(s) {direction}")
    elif stage == 2:
        direction = "v" if col_shift > 0 else "(no movement)"
        st.info(f"Stage 2: Column Shift by {col_shift} position(s) {direction}")


def render_before_after(initial: Grid, after_row: Grid, after_col: Grid) -> None:
    c1, c2, c3 = st.columns(3)
    with c1:
        render_grid("Before Shift", initial)
    with c2:
        render_grid("After Stage 1", after_row)
    with c3:
        render_grid("After Stage 2 (Final)", after_col)


def run_animation(initial: Grid, after_row: Grid, after_col: Grid, row_shift: int, col_shift: int) -> None:
    placeholder = st.empty()
    with placeholder.container():
        render_grid("Animation - Initial State", initial)

    time.sleep(0.8)
    with placeholder.container():
        render_stage_arrows(isqrt(len(initial) * len(initial)), row_shift, col_shift, stage=1)
        render_grid("Animation - Stage 1 Complete", after_row)

    time.sleep(0.8)
    with placeholder.container():
        render_stage_arrows(isqrt(len(initial) * len(initial)), row_shift, col_shift, stage=2)
        render_grid("Animation - Stage 2 Complete", after_col)
