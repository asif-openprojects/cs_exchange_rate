import json


class ExchangeRateAnalyzer:
    def __init__(self, data_str):
        self.data = json.loads(data_str)
        self.rates = self.data.get('rates', {})

    def find_min_max_rates(self):
        min_date = min(self.rates, key=lambda date: self.rates[date]['NZD'])
        min_rate = self.rates[min_date]['NZD']

        max_date = max(self.rates, key=lambda date: self.rates[date]['NZD'])
        max_rate = self.rates[max_date]['NZD']

        return min_date, min_rate, max_date, max_rate

    def calculate_average_rate(self):
        average_rate = sum(self.rates[date]['NZD'] for date in self.rates) / len(self.rates)
        return average_rate

    def calculate_percentage_change(self):
        previous_rate = None
        change_percentages = {}
        for date in sorted(self.rates.keys()):
            rate = self.rates[date]['NZD']
            if previous_rate is not None:
                change_percent = ((rate - previous_rate) / previous_rate) * 100
                change_percentages[date] = change_percent
            previous_rate = rate
        return change_percentages


