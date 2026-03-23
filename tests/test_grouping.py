from utils.grouping import group_by_student


def test_group_by_student():
    data = [
        {"student": "A", "coffee_spent": 100},
        {"student": "A", "coffee_spent": 200},
        {"student": "B", "coffee_spent": 300},
    ]

    result = group_by_student(data)

    assert result == {
        "A": [100, 200],
        "B": [300],
    }
