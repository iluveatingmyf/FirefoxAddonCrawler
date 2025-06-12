import scrapy
import scrapy_selenium
import re
from datetime import datetime
import dateutil.parser as dparser
import json

original_url = 'http://addons.opera.com'
derived_url = 'https://addons.opera.com/zh-cn/extensions/category/translation/'
class OperaAddonListSpider(scrapy.Spider):
    name = 'opera_addon_list'
    allowed_domains = ['addons.opera.com']
    start_urls = ['http://addons.opera.com/']



    def start_requests(self):
        # List of urls for crawling
        urls = []
        #categories = ['developer-tools', 'fun','translation','downloads','appearance','search','productivity','news-weather','social','music','accessibility','shopping']
        categories = ['translation']
        # READ and GENERATE urls with keywords 
        for keyword in categories:
            combined_url ='https://addons.opera.com/zh-cn/extensions/category/'+ keyword+'?order=popular'
            urls.append(combined_url)
        
        # SEND and REQUEST the urls using selenium driver/chrome
        for url in urls:
            print(url)
            yield scrapy_selenium.SeleniumRequest(url=url, callback=self.parse)

 # 解析response
    # @response :response from selenium requests
    def parse(self, response):
        pass
        ul = response.css('.grid')
        extensions = ul.xpath('li')
        for extension in extensions:
            # Extract metadata of each extensions
            url = extension.xpath('a/@href').extract()[0]
            #url = 'https://addons.opera.com' + url_component[0]
            div = extension.xpath('a/div')
            name = div.css('h4.h-pkg-name::text').get()
            des = div.css('p.description::text').get()

            others = div.css('p.rating')
            rating = others.css('span.meter').extract()[0].split('>')[1].split('=')[-1]
            count = others.css('span.total::text').get()

            if url is not None:
                details_link = original_url + url
                # yield scrapy.Request(next_page, callback=self.parse)
                # yield scrapy_selenium.SeleniumRequest(url=details_link, callback=self.parse_extension, cb_kwargs={'name':name, 'user_numbers' :user_numbers[0], 'rating' :float(rating[0]), 'creator' :creator, 'key' :key})
                yield scrapy_selenium.SeleniumRequest(url=details_link, callback=self.parse_extension,
                                                      cb_kwargs={'name': name, 'user_numbers': count,
                                                                 'rating': rating,'des': des, 'url':details_link})

            '''to the next page'''
            #pagination = response.xpath('/html/body/div/section/article').css('div.pagination')
            #next_page = pagination.xpath('ul').css('li.next_page').xpath('a/@href').extract()
            #if next_page is not None:
            #    next_page_url = derived_url + next_page[0]
            #    yield scrapy_selenium.SeleniumRequest(url=next_page_url, callback=self.parse)

    # PARSING extensions
    # @parameters take parameters that are parsed data from previous request
    def parse_extension(self, response, name, user_numbers, rating, des, url):
        print('===============================')
        previous_data = {
            "name": name,
            "user_numbers": user_numbers,
            "rating": rating,
            "description": des,
            "url" : url
        }
        print(previous_data)
        with open('opera_translation_url.txt', 'a') as f:
            f.write(url)
            f.write('\n')
        with open('opera_translation.txt', 'a') as f:
            f.write(str(previous_data))
            f.write('\n')
