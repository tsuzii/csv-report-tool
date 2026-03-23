from utils.table import print_table


def test_print_table(capsys):
    data = [("A", 100), ("B", 200)]

    print_table(data)

    captured = capsys.readouterr()

    assert "A" in captured.out
    assert "100" in captured.out
