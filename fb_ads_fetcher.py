from api_client import FacebookAdsAPI
from data_handler import DataHandler

def main():
    print("Starting Facebook Ads data collection...")
    
    try:
        # Initialize API client
        api = FacebookAdsAPI()
        
        # Fetch all data
        print("Fetching campaigns...")
        campaigns = api.get_campaigns()
        print(f"✓ Found {len(campaigns)} campaigns")
        
        print("Fetching ad sets...")
        ad_sets = api.get_ad_sets()
        print(f"✓ Found {len(ad_sets)} ad sets")
        
        print("Fetching ads...")
        ads = api.get_ads()
        print(f"✓ Found {len(ads)} ads")
        
        print("Fetching insights...")
        insights = api.get_insights()
        print(f"✓ Found {len(insights)} insight records")
        
        # Save all data
        DataHandler.save_all_data(campaigns, ad_sets, ads, insights)
        
        print("\nData collection completed successfully!")
        print("Check the 'data' directory for the output files")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())