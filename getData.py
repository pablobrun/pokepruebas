import json
import requests


class getData:

    def get(self, end_point):
        with open('data.json') as json_file:
            data = json.load(json_file)
            nedded_data = requests.get(data['base_url'] + end_point)
            return nedded_data
