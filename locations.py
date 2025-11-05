import json

# creates a list of links associated with posts specifically from my "Bay Area Life" folder

with open('saved_collections.json', 'r') as file:
    data = json.load(file)

posts = set()
correct_collection = False
    
for item in data['saved_saved_collections']:
    title = item.get('title')
    collection = item.get('string_map_data', {}).get('Name', {})
    
    if title == "Collection":
        folder_name = collection.get('value', '')
        correct_collection = (folder_name == 'Bay Area Life')
    
    href = collection.get('href')
    
    if correct_collection and href:
        link = item['string_map_data']['Name']['href']
        posts.add(link)
        
# TODO:
    # go through links and scrape instagram website to find locations
    # add locations to a CSV
    # call google maps API to create a list out of the CSV
