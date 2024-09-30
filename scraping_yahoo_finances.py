import requests as req
from bs4 import BeautifulSoup as bs

response = req.get('https://finance.yahoo.com/markets/stocks/most-active/')

page_html = response_jobs.text
soup_page = bs(page_html, 'html.parser')
table_markets = soup_jobs.find('table', class='ResultsContainer')