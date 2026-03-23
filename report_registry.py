from reports.median_coffee import MedianCoffeeReport


REPORTS = {
    MedianCoffeeReport.name: MedianCoffeeReport,
}


def get_report(report_name: str):
    if report_name not in REPORTS:
        raise ValueError(f"Unknown report: {report_name}")

    return REPORTS[report_name]()
