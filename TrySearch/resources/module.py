import json
import requests
import Keys
from twython import Twython


def search_google(query):
    url = "https://www.googleapis.com/customsearch/v1"
    my_params = {"key": Keys.GOOGLE_KEY, "q": query,
                 "cx": Keys.GOOGLE_CX}
    response = requests.get(url, params=my_params)
    resp = json.loads(response.text)
    try :
        return resp["items"][0]["title"]
    except Exception as e:
        return "Google could not produce any result"


def search_duckgo(query):
    url = "http://api.duckduckgo.com"
    my_params = {"q": query, "format": "json"}
    response = requests.get(url, params=my_params)
    resp = json.loads(response.text)
    try :
        return resp["RelatedTopics"][0]["Text"]
    except Exception as e:
        return "Duckduck go could not produce any result"


def search_twitter(query):
    twitter = Twython(Keys.APP_KEY_TWITTER, Keys.APP_SECRET_TWITTER,
                      Keys.TOKEN_KEY_TWITTER,
                      Keys.TOKEN_SECRET_TWITTER)

    results = twitter.search(q=query)
    try :
        if results.get('statuses'):
            return results.get('statuses')[0]["text"]
    except Exception as e:
        return "Twitter could not produce any result"