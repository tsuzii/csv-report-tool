import csv


def read_files(file_paths: list[str]) -> list[dict]:
    records = []

    for path in file_paths:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                records.append(
                    {
                        "student": row["student"],
                        "date": row["date"],
                        "coffee_spent": int(row["coffee_spent"]),
                        "sleep_hours": float(row["sleep_hours"]),
                        "study_hours": int(row["study_hours"]),
                        "mood": row["mood"],
                        "exam": row["exam"],
                    }
                )

    return records
