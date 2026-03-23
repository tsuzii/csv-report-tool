from statistics import median
from reports.base import BaseReport


class MedianCoffeeReport(BaseReport):
    name = "median-coffee"

    def generate(self, grouped_data):
        result = []

        for student, values in grouped_data.items():
            med = median(values)
            result.append((student, med))

        result.sort(key=lambda x: x[1], reverse=True)

        return result
