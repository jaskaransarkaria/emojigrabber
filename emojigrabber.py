#use flask to grab related images/videos/gifs

from flask import Flask, render_template
import urllib
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from selenium import webdriver
from random import choice

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
    imagesoup = make_soup('https://www.google.com/search?tbm=isch&source=hp&biw=1308&bih=657&ei=7SkRWquUMIiTU-W7oxA&q=happy+emoji&oq=happy&gs_l=img.3.1.35i39k1l2j0l8.5750.6974.0.8807.7.7.0.0.0.0.89.397.5.5.0....0...1.1.64.img..2.5.388.0...0.DYshi0uMhwo')
    img = imagesoup.find_all(jsname="hSRGPd")
    link = choice(img)
    href = "https:://images.google.com/" + link.get('href')

    driver = webdriver.Chrome()
    driver.get('https://78.media.tumblr.com/b81b1584bd08034e0c164b6313c28b39/tumblr_n7tvg8qdVn1tchubjo1_500.gif')
    happy_emoji = driver.current_url
    driver.implicitly_wait(30)
    #soup = make_soup('https://www.goodreads.com/quotes/tag/happy')
    #quote = soup.find_all("div", class_="quoteText", limit=2) #no matter how hard i try I cannot get rid of the CDATA crap!


    return render_template('happy.html', gif = href)

@app.route("/sad")
def sad():
    driver = webdriver.Chrome()
    driver.get('http://static.skaip.org/img/emoticons/180x180/f6fcff/cry.gif')
    sad_emoji = driver.current_url
    driver.implicitly_wait(30)

    #soup = make_soup('https://www.goodreads.com/quotes/tag/sad')
    #quote = soup.find_all("div", class_="quoteText", limit=2) #no matter how hard i try I cannot get rid of the CDATA crap!
    #for i in quote:
        #print(i.text)

    return render_template('sad.html', gif = sad_emoji)

if __name__ == '__main__':
  app.run(debug=True)