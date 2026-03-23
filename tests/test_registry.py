import pytest
from report_registry import get_report


def test_get_report_success():
    report = get_report("median-coffee")
    assert report is not None


def test_get_report_fail():
    with pytest.raises(ValueError):
        get_report("unknown-report")
