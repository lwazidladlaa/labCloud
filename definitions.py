import requests
import requests
import json
import pandas


def get_data_from_api(word):
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/"+ word.lower()
    response = requests.get(url)
    return json.loads(response.text)
    

def get_definition_leading(word):
    data = get_data_from_api(word)
    definition = data[0]["meanings"][0]["definitions"][0]["definition"]
    if definition:
        return definition

def get_synonym_leading(word):
    data = get_data_from_api(word)
    synonyms = data[0]["meanings"][0].get("synonyms", [])
    if synonyms:
        return synonyms[0] 
    else:
        return ""   

def get_phonetics_URL_leading(word):
    data = get_data_from_api(word)
    phonetics_url = data[0]["phonetics"][0]["audio"]
    if phonetics_url:
        return phonetics_url
    else:
        return ""


word = "cloud"
print(get_definition_leading(word))
print(get_synonym_leading(word))
print(get_phonetics_URL_leading(word))
