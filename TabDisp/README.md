### StandAlone using Cherrypy

Pulls out data from the NSX website, and adds it onto redis. Retrieves it from the redis instance and prints card instances of the data every 5 minutes (300 seconds)


#### Prerequisites
3. PhantomJS installed
4. Selenium webdrivers installed

To install python package requirements

    pip install -r requirements.txt

Every time we try to re-run the app, we need to insure the `index.html` file contains `indexTemplate.html` contents
 
#### Running the app

    python app.py

#### Screenshot

![ScreenShot](screenshot.png)
