import scrapy
import re
import itertools

class QuotesSpider(scrapy.Spider):
    name = 'Email Scraper'

    custom_settings = {
            'AUTOTHROTTLE_ENABLED': True,
            'CONCURRENT_REQUESTS_PER_DOMAIN': 4,
            'DOWNLOAD_DELAY': 0.25,
            'COOKIES_ENABLED': False,
    }

    search_engines = [
            'https://www.google.com/search?q=',
            'https://www.bing.com/search?q=',
            'https://ca.search.yahoo.com/search?p=',
    ]

    def __init__(self):
        self.search_terms = [line.rstrip('\n').replace(' ', '+') 
                for line in open('/home/hassan/wind-turbine')]

        self.start_urls = [x[0] + x[1] + '+turbine+contact' for x in 
                list(itertools.product(self.search_engines, [t for t in self.search_terms]))]

    def find_email(self, response):
        """ Find the email addresses within the webpage. """
        text = ''.join(response.xpath("//body//text()").extract()).strip()
        emailregex = re.compile(r'\w+(?:@|\s*\[at\]\s*)\w+(?:\.|\s*\[dot\]\s*)com', re.IGNORECASE)
        emails = emailregex.findall(text)
        if emails != []:
            emails = set(emails)
            print(emails)
            for email in emails:
                yield { 
                        'cur_link': self.cur_link[self.cur_link.find("=")+1:self.cur_link.find("+turbine+contact")].replace('+', ' '), 
                        'email': email 
                      }

    def parse(self, response):
        """ Get webpage links from search engines. """

        links = set({})
        
        self.cur_link = response.request.url
        if self.cur_link.find('google') >= 0:
            for x in range(3, 16):
                link = response.css(f'div#main div:nth-child({x}) a::attr("href")').get()
                if link != None and link.startswith('/url?q='):
                    link = link[7:]
                    links.add(link)

        elif self.cur_link.find('bing') >= 0:
            for x in range(1, 11):
                link = response.css(f'ol#b_results li:nth-child({x}) h2 a::attr("href")').get()
                if link != None and link[0] != '/':
                    links.add(link)

        elif self.cur_link.find('yahoo') >= 0:
            for x in range(1, 10):
                link = response.css(f'div#web ol li:nth-child({x}) a::attr("href")').get()
                if link != None:
                    links.add(link)

        for link in links:
            print(link)
            yield response.follow(link, self.find_email)
