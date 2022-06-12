#Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

#set executable path
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless = False)

#visit the Mars NASA news website
url = 'https://redplanetscience.com'
browser.visit(url)

#optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


#set up HTML parser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')

slide_elem.find('div', class_='content_title')

# Use the parent element to find the first `div` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').text
news_title

# Use the parent element to find the second `div` tag and save it as `news_summary` for the summary of the news
news_summary = slide_elem.find('div', class_= 'article_teaser_body').text
news_summary


# ## JPL Space Images Featured Image

#visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

#Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

#Parse the reulting HTML with soup
html = browser.html
img_soup = soup(html,'html.parser')

#find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

#use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url



#reading the first table from https://galaxyfacts-mars.com/ and turning it into a DataFrame
df = pd.read_html('https://galaxyfacts-mars.com/')[0]
df.head()

df.columns = ['description', 'Mars', ' Earth']
df.set_index('description', inplace=True)
df

#turns DataFrame into HTML code
df.to_html()

#shuts down automated browser server
browser.quit()


