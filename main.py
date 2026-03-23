import argparse
import sys

from reader import read_files
from utils.grouping import group_by_student
from utils.table import print_table
from report_registry import get_report


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Paths to CSV files",
    )

    parser.add_argument(
        "--report",
        required=True,
        help="Report name (e.g. median-coffee)",
    )

    args = parser.parse_args()

    try:
        data = read_files(args.files)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

    grouped = group_by_student(data)

    try:
        report = get_report(args.report)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    result = report.generate(grouped)

    print_table(result)


if __name__ == "__main__":
    main()
