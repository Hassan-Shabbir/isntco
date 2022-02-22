import scrapy
from urllib.parse import urlparse
import re
import itertools

class QuotesSpider(scrapy.Spider):
    name = 'Scraper'

    custom_settings = {
        'AUTOTHROTTLE_ENABLED': True,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 4,
        'DOWNLOAD_DELAY': 10,
        'COOKIES_ENABLED': False
    }

    def start_requests(self):
        # !!! CHANGE BELOW
        all_of = ['fish', 'meal']
        any_of = ['peru', 'super', 'prime', 'white']
        none_of = []
        exact_word = []
        lang = ['lang_en']
        country = ['pe']
        # !!! CHANGE ABOVE

        def f(a): return '+'.join(a)
        def f_or(a): return '+OR+'.join(a)
        def f_none(a): return '+-' + '+-'.join(a)

        search_terms = [
            f'https://www.google.com/search?as_q={f(all_of)}&as_epq={f(exact_word)}&as_oq={f(any_of)}&as_eq={f(none_of)}&lr={f(lang)}&cr={"country" + f(country).upper()}&as_qdr=all&as_sitesearch=&as_occt=any&safe=images&as_filetype=&tbs=',
            f'https://www.google.com/search?as_q={f(all_of)}&as_epq={f(exact_word)}&as_oq={f(any_of)}&as_eq={f(none_of)}&lr={f(lang)}&cr={"country" + f(country).upper()}&as_qdr=all&as_sitesearch=&as_occt=any&safe=images&as_filetype=&tbs=&start=10',
            f'https://www.google.com/search?as_q={f(all_of)}&as_epq={f(exact_word)}&as_oq={f(any_of)}&as_eq={f(none_of)}&lr={f(lang)}&cr={"country" + f(country).upper()}&as_qdr=all&as_sitesearch=&as_occt=any&safe=images&as_filetype=&tbs=&start=20',
            f'https://www.google.com/search?as_q={f(all_of)}&as_epq={f(exact_word)}&as_oq={f(any_of)}&as_eq={f(none_of)}&lr={f(lang)}&cr={"country" + f(country).upper()}&as_qdr=all&as_sitesearch=&as_occt=any&safe=images&as_filetype=&tbs=&start=30',
            f'https://www.google.com/search?as_q={f(all_of)}&as_epq={f(exact_word)}&as_oq={f(any_of)}&as_eq={f(none_of)}&lr={f(lang)}&cr={"country" + f(country).upper()}&as_qdr=all&as_sitesearch=&as_occt=any&safe=images&as_filetype=&tbs=&start=40',
            f'https://www.google.com/search?as_q={f(all_of)}&as_epq={f(exact_word)}&as_oq={f(any_of)}&as_eq={f(none_of)}&lr={f(lang)}&cr={"country" + f(country).upper()}&as_qdr=all&as_sitesearch=&as_occt=any&safe=images&as_filetype=&tbs=&start=50',
            f'https://www.google.com/search?as_q={f(all_of)}&as_epq={f(exact_word)}&as_oq={f(any_of)}&as_eq={f(none_of)}&lr={f(lang)}&cr={"country" + f(country).upper()}&as_qdr=all&as_sitesearch=&as_occt=any&safe=images&as_filetype=&tbs=&start=60',
            f'https://www.google.com/search?as_q={f(all_of)}&as_epq={f(exact_word)}&as_oq={f(any_of)}&as_eq={f(none_of)}&lr={f(lang)}&cr={"country" + f(country).upper()}&as_qdr=all&as_sitesearch=&as_occt=any&safe=images&as_filetype=&tbs=&start=70',
            f'https://www.google.com/search?as_q={f(all_of)}&as_epq={f(exact_word)}&as_oq={f(any_of)}&as_eq={f(none_of)}&lr={f(lang)}&cr={"country" + f(country).upper()}&as_qdr=all&as_sitesearch=&as_occt=any&safe=images&as_filetype=&tbs=&start=80',
            f'https://www.google.com/search?as_q={f(all_of)}&as_epq={f(exact_word)}&as_oq={f(any_of)}&as_eq={f(none_of)}&lr={f(lang)}&cr={"country" + f(country).upper()}&as_qdr=all&as_sitesearch=&as_occt=any&safe=images&as_filetype=&tbs=&start=90',
            f'https://www.google.com/search?as_q={f(all_of)}&as_epq={f(exact_word)}&as_oq={f(any_of)}&as_eq={f(none_of)}&lr={f(lang)}&cr={"country" + f(country).upper()}&as_qdr=all&as_sitesearch=&as_occt=any&safe=images&as_filetype=&tbs=&start=100',
            # f'https://duckduckgo.com/?q={f(all_of + any_of)}+%22{f(exact_word)}%22{f_none(none_of)}&t=h_&ia=web'
            # # f'https://search.yahoo.com/search?n=30&ei=UTF-8&va_vt=any&vo_vt=any&ve_vt=any&vp_vt=any&vst=0&vf=all&vc={f(country)}&vm=i&fl=1&vl={f(lang)}&p={f(all_of)}+{f_or(any_of)}+%22{f(exact_word)}%22{f_none(none_of)}&vs=',
        ]

        print(search_terms)
        for search_term in search_terms:
            yield scrapy.Request(url=search_term, callback=self.parse)

    def parse(self, response):
        """ Get webpage links from search engines. """
        links = set({})
        cur_link = response.request.url

        for x in range(50):
            link = response.css(f'a::attr("href")').get()
            if link != None and link.startswith('/url?q='):
                link = link[7:]
                links.add(link)
                yield response.follow(link, self.print_info)

        for x in range(20):
            link = response.css(f'div#web ol li:nth-child({x}) a::attr("href")').get()
            if link != None:
                links.add(link)
                yield response.follow(link, self.print_info)
                    
        for x in range(10):
            link = response.css(f'div#r1-{x} a::attr("href")').get()
            if link != None:
                links.add(link)
                yield response.follow(link, self.print_info)

    def print_info(self, response):
        # Find the main info and email addresses within the webpage.
        text = ''.join(response.xpath("//body//text()").extract()).strip()
        emailregex = re.compile(r'\w+(?:@|\s*\[at\]\s*)\w+(?:\.|\s*\[dot\]\s*)com', re.IGNORECASE)
        emails = list(set(emailregex.findall(text)))
        print(emails)

        parsed_uri = urlparse(response.url)
        domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri).replace('https?://(www)?.', '')

        # def strip_s(s): return re.sub('\s+', ' ', s)
        # def strip_html(s): return re.sub('</?.*?>', '', strip_s(s))
        # def strip_q(s): return re.sub('".*?', '', re.sub('.*?"', '', strip_s(s)))
        def rep(s):
            if s == None: s
            else: s.replace('[\r\n\s ]+', ' ')

        yield { 
                'domain': domain,
                'title': response.css('title::text').get(),
                'description': response.css('meta[description]').get(),
                'keywords': response.css('meta[keywords]').get(),
                'emails': ';'.join(emails),
                'h1': rep(response.css('h1::text').get()),
                'h2': rep(response.css('h2::text').get()),
                'h3': rep(response.css('h3::text').get()),
                'link': response.request.url,
                # 'domain': domain,
                # 'title': strip_html(response.css('title::text').get()),
                # 'description': strip_q(response.css('meta[description]').get()),
                # 'keywords': strip_q(response.css('meta[keywords]').get()),
                # 'cur_link': response.request.url,
                # 'emails': ';'.join(emails),
                # 'h1': strip_s(response.css('h1::text').get()),
                # 'h2': strip_s(response.css('h2::text').get()),
                # 'h3': strip_s(response.css('h3::text').get())
            }
