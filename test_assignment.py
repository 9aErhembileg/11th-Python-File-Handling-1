import pytest
from assignment import grade_report, calculate_balance


@pytest.mark.parametrize(
    "grades, expected_output",
    [
        (
            # Case 1 — Example from exercise
            "Alice,89\nBob,72\nCharlie,95\nDiana,62\n",
            "Average: 79.5\nHighest: Charlie (95)\nLowest: Diana (62)",
        ),
        (
            # Case 2 — All equal scores
            "A,50\nB,50\nC,50\n",
            "Average: 50.0\nHighest: A (50)\nLowest: A (50)",
        ),
        (
            # Case 3 — Two students only
            "Anna,100\nTom,0\n",
            "Average: 50.0\nHighest: Anna (100)\nLowest: Tom (0)",
        ),
    ],
)
def test1(tmp_path, grades, expected_output):
    input_file = tmp_path / "grades.txt"
    output_file = tmp_path / "report.txt"
    input_file.write_text(grades)

    grade_report(input_file, output_file)
    result = output_file.read_text().strip()

    # normalize newlines to make test platform-independent
    assert result == expected_output


@pytest.mark.parametrize(
    "transactions, expected_balance",
    [
        (
            # Case 1 — Example from exercise
            "+200\n-50\n+100\n-30\n",
            "Final Balance: 220",
        ),
        (
            # Case 2 — Only positive transactions
            "+10\n+20\n+30\n",
            "Final Balance: 60",
        ),
        (
            # Case 3 — Only negative transactions
            "-5\n-15\n-10\n",
            "Final Balance: -30",
        ),
        (
            # Case 4 — Empty file
            "",
            "Final Balance: 0",
        ),
    ],
)
def test2(tmp_path, transactions, expected_balance):
    input_file = tmp_path / "transactions.txt"
    output_file = tmp_path / "summary.txt"
    input_file.write_text(transactions)

    calculate_balance(input_file, output_file)
    result = output_file.read_text().strip()

    assert result == expected_balance
