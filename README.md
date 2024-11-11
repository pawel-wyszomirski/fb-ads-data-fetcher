# Facebook Ads Data Fetcher

This script demonstrates the structure for fetching and organizing Facebook Ads data. It currently uses sample data, but can be easily modified to use the Facebook Marketing API in a production environment.

## Structure

The script organizes data into four main categories:
- Campaigns
- Ad Sets
- Ads
- Ad Insights

## Output Files

The script generates four JSON files:
- `campaigns.json`: Campaign information
- `ad_sets.json`: Ad sets data
- `ads.json`: Individual ads information
- `ad_insights.json`: Performance metrics

## Usage

Run the script:
```bash
python fb_ads_fetcher.py
```

## Production Setup

To use this with the actual Facebook API:

1. Replace the `load_sample_data()` function with actual API calls
2. Set your Facebook API credentials:
   ```python
   ACCESS_TOKEN = "your_access_token"
   ACCOUNT_ID = "your_account_id"
   ```

## Data Structure

### Campaigns
```json
{
    "id": "123456789",
    "name": "Campaign Name",
    "objective": "CONVERSIONS",
    "status": "ACTIVE",
    "start_time": "2023-01-01T00:00:00+0000",
    "daily_budget": "1000",
    "bid_strategy": "LOWEST_COST_WITHOUT_CAP"
}
```

### Ad Sets
```json
{
    "id": "987654321",
    "name": "Ad Set Name",
    "campaign_id": "123456789",
    "status": "ACTIVE",
    "targeting": {
        "age_min": 18,
        "age_max": 65,
        "genders": [1, 2],
        "geo_locations": {
            "countries": ["US"]
        }
    }
}
```

### Ads
```json
{
    "id": "111222333",
    "name": "Ad Name",
    "adset_id": "987654321",
    "status": "ACTIVE",
    "created_time": "2023-01-01T00:00:00+0000",
    "updated_time": "2023-01-02T00:00:00+0000"
}
```

### Insights
```json
{
    "ad_id": "111222333",
    "impressions": "1000",
    "clicks": "50",
    "spend": "100.00",
    "ctr": "5.00",
    "cpc": "2.00"
}