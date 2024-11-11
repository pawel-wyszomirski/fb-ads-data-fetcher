import json
from datetime import datetime
import os

class DataHandler:
    @staticmethod
    def save_to_json(data, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    @staticmethod
    def create_timestamp():
        return datetime.now().strftime('%Y%m%d_%H%M%S')

    @staticmethod
    def save_all_data(campaigns, ad_sets, ads, insights):
        timestamp = DataHandler.create_timestamp()
        
        # Ensure data directory exists
        os.makedirs('data', exist_ok=True)
        
        DataHandler.save_to_json(campaigns, f'data/campaigns_{timestamp}.json')
        DataHandler.save_to_json(ad_sets, f'data/ad_sets_{timestamp}.json')
        DataHandler.save_to_json(ads, f'data/ads_{timestamp}.json')
        DataHandler.save_to_json(insights, f'data/insights_{timestamp}.json')