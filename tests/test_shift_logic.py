from src.utils.shiftLogic import (
    analyze_complexity,
    apply_two_stage_mesh_shift,
    is_perfect_square,
    row_shift_stage,
)


def test_is_perfect_square() -> None:
    assert is_perfect_square(16)
    assert is_perfect_square(64)
    assert not is_perfect_square(15)


def test_row_shift_stage() -> None:
    grid = [["D0", "D1", "D2", "D3"]]
    shifted = row_shift_stage(grid, 1)
    assert shifted == [["D3", "D0", "D1", "D2"]]


def test_two_stage_for_16_5() -> None:
    initial, after_row, after_col = apply_two_stage_mesh_shift(16, 5)
    assert initial[0][0] == "D0"
    assert after_row[0] == ["D3", "D0", "D1", "D2"]
    assert after_col[1][0] == "D3"


def test_complexity_formula() -> None:
    analysis = analyze_complexity(16, 5)
    assert analysis.row_shift == 1
    assert analysis.col_shift == 1
    assert analysis.mesh_steps == 2
    assert analysis.ring_steps == 5
