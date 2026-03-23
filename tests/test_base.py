from reports.base import BaseReport
import pytest


def test_base_report_not_implemented():
    report = BaseReport()

    with pytest.raises(NotImplementedError):
        report.generate({})
