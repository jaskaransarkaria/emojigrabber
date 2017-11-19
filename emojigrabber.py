#use flask to grab related images/videos/gifs

from flask import Flask, render_template
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver

app = Flask(__name__)

def make_soup(url):

    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, 'html.parser')
    return soupdata

@app.route("/")
def welcome():
    return render_template('home.html')

@app.route("/happy")
def happy():
    driver = webdriver.Chrome()
    driver.get('https://78.media.tumblr.com/b81b1584bd08034e0c164b6313c28b39/tumblr_n7tvg8qdVn1tchubjo1_500.gif')
    happy_emoji = driver.current_url
    driver.implicitly_wait(30)

    return render_template('happy.html', gif = happy_emoji)

@app.route("/sad")
def sad():
    driver = webdriver.Chrome()
    driver.get('http://static.skaip.org/img/emoticons/180x180/f6fcff/cry.gif')
    sad_emoji = driver.current_url
    driver.implicitly_wait(30)

    return render_template('sad.html', gif = sad_emoji)

if __name__ == '__main__':
  app.run()