from collections import defaultdict


def group_by_student(records: list[dict]) -> dict[str, list[int]]:
    grouped = defaultdict(list)

    for record in records:
        student = record["student"]
        coffee = record["coffee_spent"]

        grouped[student].append(coffee)

    return dict(grouped)
