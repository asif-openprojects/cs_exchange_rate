import json
from datetime import datetime, timedelta


class Preprocess:
    def __init__(self, json_data):
        self.json_data = json_data
        self.data = None
        self.start_date = None
        self.end_date = None
        self.rates = None
        self.processed_data = None

    def parse_json(self):
        try:
            self.data = json.loads(self.json_data)
            self.start_date = datetime.strptime(self.data['start_date'], '%Y-%m-%d')
            self.end_date = datetime.strptime(self.data['end_date'], '%Y-%m-%d')
            self.rates = self.data['rates']
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
        except KeyError as e:
            print(f"Missing key in JSON: {e}")

    def get_date_range(self):
        date_range = []
        current_date = self.start_date
        while current_date <= self.end_date:
            date_range.append(current_date.strftime('%Y-%m-%d'))
            current_date += timedelta(days=1)
        return date_range

    def interpolate_rate(self, previous_rate, next_rate):
        if previous_rate is None or next_rate is None:
            return previous_rate or next_rate
        return (previous_rate + next_rate) / 2

    def fix_missing_dates_and_rates(self):
        date_range = self.get_date_range()
        previous_rate = None

        for i, date in enumerate(date_range):
            if date not in self.rates:
                # Find the next available rate
                next_rate = None
                for future_date in date_range[i + 1:]:
                    if future_date in self.rates:
                        next_rate = self.rates[future_date]['NZD']
                        break

                # Interpolate the missing rate
                interpolated_rate = self.interpolate_rate(previous_rate, next_rate)
                self.rates[date] = {'NZD': interpolated_rate}

            previous_rate = self.rates[date]['NZD']

        self.processed_data = self.data
        self.processed_data['rates'] = dict(sorted(self.rates.items()))

    def preprocess(self):
        self.parse_json()
        self.fix_missing_dates_and_rates()
        return self.processed_data


