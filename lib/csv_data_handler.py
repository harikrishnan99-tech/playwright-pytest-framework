from utils.csv_reader import read_csv_data


class DataHandler:
    data_sources = {
        "account_data": "account_data.csv",
        "wordings_data": "wordings_data.csv"
    }

    @staticmethod
    def get_data(key, marker_value):
        file = DataHandler.data_sources.get(key)
        if not file:
            raise ValueError(f"No data source defined for key: {key}")

        all_data = read_csv_data(file)
        for row in all_data:
            if row.get("marker") == marker_value:
                return row
        raise ValueError(f"No data found for marker: {marker_value} in {file}")
