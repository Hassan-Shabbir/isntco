import scrapy
import re
import itertools

class QuotesSpider(scrapy.Spider):
    name = 'Email Scraper'

    custom_settings = {
            'AUTOTHROTTLE_ENABLED': True,
            'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
            'DOWNLOAD_DELAY': 3,
            'COOKIES_ENABLED': False,
    }

    # search_engines = [
    #         'https://www.google.com/search?q=',
    #         'https://www.bing.com/search?q=',
    #         'https://ca.search.yahoo.com/search?p=',
    # ]

    def start_requests(self):
        # self.search_terms = 

        # [line.rstrip('\n').replace(' ', '+') for line in open('/home/hassan/wind-turbine')]

        # self.start_urls = [x[0] + x[1] + '+turbine+contact' for x in list(itertools.product(self.search_engines, [t for t in self.search_terms]))]

        start_urls = [
            'https://healthyoilseeds.com/',
            'https://johnsonseeds.com/',
            'https://konuklarbakliyat.com/index.html',
            'https://www.alliancezone.ca/products/lentils-peas-and-beans/',
            'https://www.buvite.com/our-products.php',
            'https://www.grainmillers.com/grain-products/',
            'https://www.hfifamily.com/healthy-ingredients/',
            'https://www.makspm.com/products',
            'https://www.scoular.com/food-ingredient-products/flours/steamed-chickpea-flour/?gclid=Cj0KCQiA3rKQBhCNARIsACUEW_YCbnKE_T11iLHUMOX363HjVMjoB_kYlmv3poZN0Np7h2ptNlGowgAaAjRiEALw_wcB#',
            'https://www.stolmina.eu/en/',
            'https://www.tafoods.ca/bulk-processing',
            'https://www.thomasnet.com/articles/top-suppliers/flax-seed-suppliers-manufacturers/',
            'https://www.viterra.ca/en',
            'https://www.zayma.com.mx/agroproductos/',
            'http://bescograin.ca',
            'http://neprairiegrain.com/',
            'http://psinternational.net',
            'http://www.adroitoverseas.com',
            'http://www.agricom.com',
            'http://www.agrocorp.ca',
            'http://www.agtfoods.com',
            'http://www.allcommodities.ca',
            'http://www.avenafoods.com',
            'http://www.broadgrain.com',
            'http://www.canadiangraininc.com',
            'http://www.cargill.ca',
            'http://www.cbconstantini.com',
            'http://www.ceresglobalagcorp.com',
            'http://www.chsinc.com',
            'http://www.commodious.ca',
            'http://www.delmarcommodities.com',
            'http://www.dspdirect.ca',
            'http://www.etgworld.com',
            'http://www.exportpackers.com',
            'http://www.fieldfarms.ca',
            'http://www.g3.ca',
            'http://www.gavilon.com',
            'http://www.globeways.com',
            'http://www.gltraders.com',
            'http://www.grainex.net',
            'http://www.greatwesternrail.com',
            'http://www.jglgrain.com',
            'http://www.jkmilling.ca',
            'http://www.johnsonseeds.com',
            'http://www.lineargrain.com',
            'http://www.marinacommodities.com',
            'http://www.marketplacecommodities.com',
            'http://www.maviga.com',
            'http://www.mingintl.com',
            'http://www.northwestterminal.com',
            'http://www.otfarms.ca',
            'http://www.parrishandheimbecker.com',
            'http://www.patersonglobalfoods.com',
            'http://www.prairiepulse.com',
            'http://www.primeseeds.com',
            'http://www.providencegrain.ca',
            'http://www.purewest.ag',
            'http://www.rayglen.com',
            'http://www.richardson.ca',
            'http://www.scoular.com',
            'http://www.scoularspecialcrops.com',
            'http://www.seaboardspecialcrops.com',
            'http://www.section12foods.com',
            'http://www.seed-ex.com',
            'http://www.shafercommodities.com',
            'http://www.simpsonseeds.com',
            'http://www.southlandpulse.com',
            'http://www.stonehengeglobal.ca',
            'http://www.sunrisefoods.ca',
            'http://www.swt.ca',
            'http://www.theredwoodgroup.com',
            'http://www.uscommodities-ag.com',
            'http://www.vanderveencommodities.com/',
            'http://www.veiklegrain.com',
            'http://www.victoriapulse.ca',
            'http://www.viterra.com',
            'http://www.wagrain.ca',
            'http://www.wilburellis.com',
            'http://www.xptgrain.ca',
            'http://www.yourgrain.ca',
            'http://www.zeghersseed.com',
            'http://www/rudyagro.ca',
            'http://www/westlandagro.ca',
            'https://albertapulse.com/dealer/northern-grain-ltd/',
            'https://bellepulses.ca/',
            'https://meritfoods.com/',
            'https://naturalspecialty.net/',
            'https://www.adm.com/',
            'https://www.google.ca/search?q=BORNHORST+SEEDS+LTD&sxsrf=APq-WBvGgkCl5m6wV5_obx4jBwb_dVfkOg%3A1645212723425&source=hp&ei=M_QPYsmDFparptQP7vSosAY&iflsig=AHkkrS4AAAAAYhACQ0qq3p9xxULAp1w-D-_o8esP9IsB&ved=0ahUKEwiJ6dL__on2AhWWlYkEHW46CmYQ4dUDCAk&uact=5&oq=BORNHORST+SEEDS+LTD&gs_lcp=Cgdnd3Mtd2l6EAMyCwguEIAEEMcBEK8BMgYIABAWEB5QAFgAYNMBaABwAHgAgAGMAYgBjAGSAQMwLjGYAQCgAQKgAQE&sclient=gws-wiz',
            'https://www.google.ca/search?q=CHAPLIN+GRAIN+CORP&sxsrf=APq-WBs_xW0XCDpdODFuZtaWcgWkJipShA%3A1645212817027&ei=kfQPYvWbAeqnptQPyY-1kAo&ved=0ahUKEwi1qKes_4n2AhXqk4kEHclHDaIQ4dUDCA4&uact=5&oq=CHAPLIN+GRAIN+CORP&gs_lcp=Cgdnd3Mtd2l6EAMyCwguEIAEEMcBEK8BSgQIQRgASgQIRhgAUABYAGCAAWgAcAB4AIABb4gBb5IBAzAuMZgBAKABAqABAcABAQ&sclient=gws-wiz',
            'https://www.google.ca/search?q=GREENFIELDS+AGRICULTURE+CORPORATION&sxsrf=APq-WBvYZh2yAMpPdV-Zzg4wf1Qb4kuS2w%3A1645213077934&source=hp&ei=lfUPYvaHNbCfptQP7MSFwAs&iflsig=AHkkrS4AAAAAYhADpaEk1NVdPIixgLdvqMIHnWuHtyJY&ved=0ahUKEwi2ptiogIr2AhWwj4kEHWxiAbgQ4dUDCAk&uact=5&oq=GREENFIELDS+AGRICULTURE+CORPORATION&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgYIABAWEB5QAFgAYMkBaABwAHgAgAFtiAFtkgEDMC4xmAEAoAECoAEB&sclient=gws-wiz',
            'https://www.graincorp.com.au/',
            'www.andersonsinc.com',
            'www.hdc.on.ca',
            'www.merakicommodities.com',
            'www.roquette.com'
        ]

        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    #def find_email(self, response):
    def parse(self, response):
        """ Find the email addresses within the webpage. """
        text = ''.join(response.xpath("//body//text()").extract()).strip()
        emailregex = re.compile(r'\w+(?:@|\s*\[at\]\s*)\w+(?:\.|\s*\[dot\]\s*)com', re.IGNORECASE)
        emails = emailregex.findall(text)
        if emails != []:
            emails = set(emails)
            print(emails)
            yield { 
                    'url': response.url,
                    'emails': '; '.join(list(emails))
                  }
        else:
            yield { 
                    'url': response.url,
                    'emails': 'NULL'
                  }
            

    #def parse(self, response):
    #    """ Get webpage links from search engines. """

    #    links = set({})
    #    
    #    self.cur_link = response.request.url
    #    if self.cur_link.find('google') >= 0:
    #        for x in range(3, 16):
    #            link = response.css(f'div#main div:nth-child({x}) a::attr("href")').get()
    #            if link != None and link.startswith('/url?q='):
    #                link = link[7:]
    #                links.add(link)

    #    elif self.cur_link.find('bing') >= 0:
    #        for x in range(1, 11):
    #            link = response.css(f'ol#b_results li:nth-child({x}) h2 a::attr("href")').get()
    #            if link != None and link[0] != '/':
    #                links.add(link)

    #    elif self.cur_link.find('yahoo') >= 0:
    #        for x in range(1, 10):
    #            link = response.css(f'div#web ol li:nth-child({x}) a::attr("href")').get()
    #            if link != None:
    #                links.add(link)

    #    for link in links:
    #        print(link)
    #        yield response.follow(link, self.find_email)


