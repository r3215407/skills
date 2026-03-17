import json
import os

def read_json_result(file_path):
    """
    Reads a JSON file and returns the data.
    """
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return None
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

if __name__ == "__main__":
    # Path to your result.json
    # You can change this to the absolute path if needed
    file_name = "result.json"
    
    # Updated to include 'skills' in the path and added a relative path check
    script_dir = os.path.dirname(os.path.abspath(__file__))
    paths_to_check = [
        os.path.join(script_dir, "/../../../../", file_name),
        os.path.join("d:\\work\\code\\skills\\.agent\\skills\\extract-data\\", file_name)
    ]
    
    result_data = None
    for path in paths_to_check:
        print(path)
        if os.path.exists(path):
            print(f"Reading from: {path}")
            result_data = read_json_result(path)
            break
            
    if result_data:
        try:
            # Extracting cover_urls based on user's specified path:
            # result_data['data']['asset_list'][0]['image']['item_list'] -> each ['common_attr']['cover_url']
            data = result_data.get('data', {})
            asset_list = data.get('asset_list', [])
            
            if asset_list and len(asset_list) > 0:
                item_list = asset_list[0].get('image', {}).get('item_list', [])
                
                print(f"Successfully loaded data. Found {len(item_list)} items in item_list.")
                
                cover_urls = []
                for item in item_list:
                    cover_url = item.get('common_attr', {}).get('cover_url')
                    if cover_url:
                        cover_urls.append(cover_url)
                
                print("\nExtracted Cover URLs:")
                for i, url in enumerate(cover_urls, 1):
                    print(f"{i}: {url}")
            else:
                print("Error: 'asset_list' is empty or missing in 'data'.")
        except Exception as e:
            print(f"An error occurred during extraction: {e}")
    else:
        print("Could not find or read result.json. Please ensure the file exists.")
