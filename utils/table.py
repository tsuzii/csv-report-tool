from tabulate import tabulate


def print_table(data: list[tuple[str, float]]):
    headers = ["student", "median_coffee"]

    table = tabulate(data, headers=headers, tablefmt="grid")

    print(table)
