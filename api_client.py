from http_client import HTTPClient
from config import ACCESS_TOKEN, ACCOUNT_ID, API_VERSION, API_HOST

class FacebookAdsAPI:
    def __init__(self):
        self.client = HTTPClient(API_HOST)
        self.headers = {
            'Authorization': f'Bearer {ACCESS_TOKEN}',
            'Accept': 'application/json'
        }

    def _make_request(self, endpoint, params=None):
        path = f"/{API_VERSION}/{endpoint}"
        try:
            return self.client.request('GET', path, self.headers, params)
        except Exception as e:
            raise Exception(f"API request failed: {str(e)}")
        finally:
            self.client.close()

    def get_campaigns(self):
        endpoint = f"{ACCOUNT_ID}/campaigns"
        params = {
            'fields': 'id,name,objective,status,start_time,daily_budget,bid_strategy,spend_cap'
        }
        return self._make_request(endpoint, params)['data']

    def get_ad_sets(self):
        endpoint = f"{ACCOUNT_ID}/adsets"
        params = {
            'fields': 'id,name,campaign_id,status,targeting,daily_budget,optimization_goal,bid_amount'
        }
        return self._make_request(endpoint, params)['data']

    def get_ads(self):
        endpoint = f"{ACCOUNT_ID}/ads"
        params = {
            'fields': 'id,name,adset_id,status,created_time,updated_time,creative'
        }
        return self._make_request(endpoint, params)['data']

    def get_insights(self, level='ad'):
        endpoint = f"{ACCOUNT_ID}/insights"
        params = {
            'level': level,
            'fields': 'ad_id,impressions,clicks,spend,ctr,cpc,reach,frequency',
            'date_preset': 'last_30d'
        }
        return self._make_request(endpoint, params)['data']