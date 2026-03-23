from reports.median_coffee import MedianCoffeeReport


def test_median_coffee_report():
    grouped = {
        "A": [100, 200, 300],
        "B": [50, 150],
    }

    report = MedianCoffeeReport()
    result = report.generate(grouped)

    assert result == [
        ("A", 200),
        ("B", 100),
    ]
