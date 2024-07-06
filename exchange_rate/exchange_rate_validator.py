import json
class JsonValidator:
    def __init__(self, json_data):
        self.json_data = json_data
        self.validated_data = None

    def validate(self):
        try:
            data = json.loads(self.json_data)

            # Check for required fields
            required_fields = ["success", "timeseries", "start_date", "end_date", "base", "rates"]
            for field in required_fields:
                if field not in data:
                    raise ValueError(f"Missing required field: {field}")

            # Validate boolean values
            if not isinstance(data["success"], bool) or not isinstance(data["timeseries"], bool):
                raise ValueError("Invalid boolean value for success or timeseries")

            # Validate date formats and order (if needed)
            start_date = data["start_date"]
            end_date = data["end_date"]
            # Additional validation logic for date format and order can be added here

            # Validate base currency (if needed)
            base_currency = data["base"]
            # Additional validation logic for base currency format can be added here

            # Validate rates structure and values
            rates = data["rates"]
            if not isinstance(rates, dict):
                raise ValueError("Rates should be a dictionary")

            for date, rate_info in rates.items():
                if not isinstance(rate_info, dict) or "NZD" not in rate_info:
                    raise ValueError(f"Invalid rate info for date {date}")
                if not isinstance(rate_info["NZD"], (int, float)):
                    raise ValueError(f"Invalid NZD rate value for date {date}")

            # If all validations pass, assign validated data
            self.validated_data = data
            return True

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
        except ValueError as ve:
            print(f"Validation error: {ve}")

        return False


# Example JSON data (replace with your actual JSON string)
json_data = '''
{
  "success": true,
  "timeseries": true,
  "start_date": "2024-06-06",
  "end_date": "2024-07-06",
  "base": "AUD",
  "rates": {
    "2024-06-06": {"NZD": 1.07631},
    "2024-06-07": {"NZD": 1.074866},
    "2024-06-08": {"NZD": 1.07895},
    "2024-06-09": {"NZD": 1.07808},
    "2024-06-10": {"NZD": 1.078204},
    "2024-06-11": {"NZD": 1.075373},
    "2024-06-12": {"NZD": 1.077024},
    "2024-06-13": {"NZD": 1.076672},
    "2024-06-14": {"NZD": 1.075134},
    "2024-06-15": {"NZD": 1.073361},
    "2024-06-16": {"NZD": 1.077516},
    "2024-06-17": {"NZD": 1.079063},
    "2024-06-18": {"NZD": 1.084816},
    "2024-06-19": {"NZD": 1.087336},
    "2024-06-20": {"NZD": 1.087845},
    "2024-06-21": {"NZD": 1.08981},
    "2024-06-22": {"NZD": 1.091934},
    "2024-06-23": {"NZD": 1.08548},
    "2024-06-24": {"NZD": 1.087334},
    "2024-06-25": {"NZD": 1.085985},
    "2024-06-26": {"NZD": 1.092889},
    "2024-06-27": {"NZD": 1.09314},
    "2024-06-28": {"NZD": 1.097649},
    "2024-06-29": {"NZD": 1.097649},
    "2024-06-30": {"NZD": 1.094296},
    "2024-07-01": {"NZD": 1.097228},
    "2024-07-02": {"NZD": 1.096445},
    "2024-07-03": {"NZD": 1.098792},
    "2024-07-04": {"NZD": 1.10017},
    "2024-07-05": {"NZD": 1.098888},
    "2024-07-06": {"NZD": 1.098888}
  }
}
'''

# Instantiate and validate JSON data
validator = JsonValidator(json_data)
if validator.validate():
    validated_data = validator.validated_data
    # Access validated data here
    print(validated_data)
    # Additional processing with validated data

# If validation fails, handle accordingly