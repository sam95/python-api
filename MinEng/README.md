# SimpleElastic
A simple elasticsearch like search engine built using Python Flask REST API

### Request and Response examples
An api endpoint for indexing


    POST /index
    {
        "id": "1",
        "title": "quick fox",
        "data": "A fox is usually quick and brown."
    }
    
__200 OK__

    POST /index
    {
        "id": "2",
        "title": "lazy dog",
        "data": "A quick brown fox jumped over lazy dog. A fox is always jumping."
    }

__200 OK__

An api endpoint for search

```
GET /search/quick fox

[
  {
    "data": "A fox is usually quick and brown.",
    "id": "1",
    "title": "quick fox"
  },
  {
    "data": "A quick brown fox jumped over lazy dog. A fox is always jumping.",
    "id": "2",
    "title": "lazy dog"
  }
]
```
##### API Endpoints with querystring search paramter examples for specific fields

```
GET /search/content?title=lazy

[
  {
    "data": "A quick brown fox jumped over lazy dog. A fox is always jumping.",
    "id": "2",
    "title": "lazy dog"
  }
]
```

Search Endpoints with both `title` and `data` parameters
```
GET /search/content?title=quick&data=dog
[
  {
    "data": "A fox is usually quick and brown.",
    "id": "1",
    "title": "quick fox"
  },
  {
    "data": "A quick brown fox jumped over lazy dog. A fox is always jumping.",
    "id": "2",
    "title": "lazy dog"
  }
]
```

Endpoints for POST : **/index**

Endpoints for GET : **/search/< query >**

Endpoints for Specific records : **/search/content?title="superman"**

Tested and run with Postman REST API client.

#### Pre-requisites

Please install requirements before running the app.

    sudo pip install -r requirements.txt

#### Running the app

    python app.py
    