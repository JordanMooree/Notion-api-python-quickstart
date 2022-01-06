# Notion Application
import json, requests


file = open('SECRET.json') # Opens the file

data = json.load(file) # loads the data then stores in variable called data

# Secret here:
secret = data['id']

# Database information here:
database = data['database_tasks']

file.close() # close file

url = 'https://api.notion.com/v1/pages'

# Headers
headers = {
    'Authorization': f'Bearer {secret}',
    'Content-Type': 'application/json',
    'Notion-Version': '2021-08-16'
}

# Data input
data_input = {
    "parent": { "database_id": f"{database}" },
    "properties": {
      "Name": {
        "title": [
          {
            "text": {
              "content": "Yurts in Big Sur, California"
            },
            "multi_select": {
              "content": "Yurts in Big Sur, California"
            }
            
          }
        ]
      }
    }
  }

  
# check request 
response = requests.post(url, headers=headers, json=data_input)
print(response.json())


