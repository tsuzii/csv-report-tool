import sys
from main import main


def test_main(monkeypatch, capsys):
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "main.py",
            "--files",
            "data/math.csv",
            "--report",
            "median-coffee",
        ],
    )

    main()

    captured = capsys.readouterr()

    assert "student" in captured.out
