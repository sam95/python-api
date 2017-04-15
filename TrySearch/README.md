#### Multiple Resource Search

A REST API developed in Python-Flask for multiple search on a single query.
The resource sites are
1. Google
2. DuckDuck Go
3. Twitter

Searches multiple resources sites parallely for a single request made to your API.

Reference Docs :

1. https://developers.google.com/custom-search/json-api/v1/using_rest
2. https://duckduckgo.com/api
3. https://dev.twitter.com/rest/public/search

##### Test Example:

    curl “http://localhost:5000.com/the+dark+knight” -XGET
    
##### Output

    {
      "query": "the dark knight", 
      "results": {
        "duckduckgo": {
          "text": "The Dark Knight A 2008 superhero crime thriller film directed, produced, and co-written by Christopher Nolan."
        }, 
        "google": {
          "text": "The Dark Knight (2008) - IMDb"
        }, 
        "twitter": {
          "text": "RT @boydhotbrook: the dark knight (2008)\n\u00ab you either die a hero or you live long enough to see yourself become the villain \u00bb https://t.co/\u2026"
        }
      }
    }
#### Pre-requisites

Please install requirements before running the app.

    sudo pip install -r requirements.txt

#### Running the app

    python app.py
    