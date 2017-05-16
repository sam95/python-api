import threading
import time
import redis
from selenium import webdriver
from crawler import table_obtain


class CrawlThread(object):

    def __init__(self, interval=1):
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        r = redis.StrictRedis(host='localhost', port=6379, db=0)
        driver = webdriver.PhantomJS()
        while True:
            table_obtain(r, driver)
            time.sleep(self.interval)
