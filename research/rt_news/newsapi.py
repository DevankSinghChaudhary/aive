import requests
url = ('https://newsapi.org/v2/everything?'
       'q=iran%20vs%20us%20war&'
       'apiKey=be7a04ea6ab641d8b4223658b80c074d')
response = requests.get(url)
print(response.json())