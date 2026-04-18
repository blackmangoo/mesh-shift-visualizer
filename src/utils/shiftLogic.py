from __future__ import annotations

from dataclasses import dataclass
from math import isqrt
from typing import List

Grid = List[List[str]]


@dataclass(frozen=True)
class ShiftAnalysis:
    p: int
    q: int
    n: int
    row_shift: int
    col_shift: int
    ring_steps: int
    mesh_steps: int


def is_perfect_square(value: int) -> bool:
    if value < 1:
        return False
    root = isqrt(value)
    return root * root == value


def validate_inputs(p: int, q: int) -> tuple[bool, str]:
    if p < 4 or p > 64:
        return False, "p must be between 4 and 64."
    if not is_perfect_square(p):
        return False, "p must be a perfect square."
    if q < 1 or q > p - 1:
        return False, "q must be between 1 and p-1."
    return True, ""


def build_initial_grid(p: int) -> Grid:
    n = isqrt(p)
    return [[f"D{r * n + c}" for c in range(n)] for r in range(n)]


def rotate_row_right(row: List[str], shift: int) -> List[str]:
    if not row:
        return row
    k = shift % len(row)
    if k == 0:
        return row[:]
    return row[-k:] + row[:-k]


def row_shift_stage(grid: Grid, shift: int) -> Grid:
    if not grid:
        return []
    return [rotate_row_right(row, shift) for row in grid]


def col_shift_stage(grid: Grid, shift: int) -> Grid:
    if not grid:
        return []
    n = len(grid)
    k = shift % n
    if k == 0:
        return [row[:] for row in grid]

    out = [["" for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            out[(r + k) % n][c] = grid[r][c]
    return out


def flatten_grid(grid: Grid) -> List[str]:
    return [item for row in grid for item in row]


def apply_two_stage_mesh_shift(p: int, q: int) -> tuple[Grid, Grid, Grid]:
    n = isqrt(p)
    initial = build_initial_grid(p)
    row_shift = q % n
    col_shift = q // n
    after_row = row_shift_stage(initial, row_shift)
    after_col = col_shift_stage(after_row, col_shift)
    return initial, after_row, after_col


def analyze_complexity(p: int, q: int) -> ShiftAnalysis:
    n = isqrt(p)
    row_shift = q % n
    col_shift = q // n
    ring_steps = min(q, p - q)
    mesh_steps = row_shift + col_shift
    return ShiftAnalysis(
        p=p,
        q=q,
        n=n,
        row_shift=row_shift,
        col_shift=col_shift,
        ring_steps=ring_steps,
        mesh_steps=mesh_steps,
    )
