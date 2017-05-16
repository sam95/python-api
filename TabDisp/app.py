import cherrypy
import os
from backgroundThread import CrawlThread
import resources


class CrawlObject(object):
    @cherrypy.expose
    def index(self):
        return file('index.html')


if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    example = CrawlThread(resources.TIME)
    cherrypy.quickstart(CrawlObject(), '/', conf)
