import requests

#https://github.com/thundercomb/poetrydb#readme
def fetch_daily_prompt():
    try:
        response = requests.get('https://poetrydb.org/linecount/2.json')
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return data[0]['lines']
    except requests.RequestException as e:
        print(f"Error fetching prompt: {e}")
        return 'Default prompt if API fails'