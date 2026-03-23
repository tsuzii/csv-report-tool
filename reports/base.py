class BaseReport:
    name: str

    def generate(self, grouped_data):
        raise NotImplementedError
