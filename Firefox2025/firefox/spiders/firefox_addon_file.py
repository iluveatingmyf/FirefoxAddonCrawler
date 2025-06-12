import scrapy
import json
import scrapy_selenium
import re


class FirefoxAddonFileSpider(scrapy.Spider):
    name = 'firefox_addon_file'
    allowed_domains = ['addons.mozilla.org']
    start_urls = ['http://addons.mozilla.org/']

    def start_requests(self):
        
        urls =[]
        f = open('recommanded100.txt', 'r')
        ext_list = f.readlines()
        for line in ext_list:
            #print(line.replace('\'','\"'))
            try:
                ext_info = json.loads(line.replace('\'','\"'))
                ext_id = ext_info['key']
                combined_url = 'https://addons.mozilla.org/zh-CN/firefox/addon/'+ext_id+'/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=search'
                urls.append(combined_url)
            except Exception as e:
                print(line)
                error = open('error.txt', 'a')
                error.write(line)
                continue
            #break
        # SEND and REQUEST the urls using selenium driver/chrome
        for url in urls:
            yield scrapy_selenium.SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response):
        pass
        link_list = []
        # get full response
        extensions = response.css('.Addon-summary-and-install-button-wrapper')
        for extension in extensions:
            # Extract metadata of each extensions
            string = extension.css('.InstallButtonWrapper').get()
            s_list = string.split("\"")
            link = s_list[-2]
            print('--------------------')
            print(link)
            print('--------------------')
            output = open('recommanded100_url.txt', 'a')
            output.write(link)
            print(link)
            output.write('\n')

            #yield scrapy_selenium.SeleniumRequest(url=link, callback=self.parse_link)
            #break
            #print(re.findall(pattern, string))
            #name = extension.css('a').get()
        #extensions = response.css('a').get()

           # if details_link is not None:
           #     details_link = response.urljoin(details_link)
                # yield scrapy.Request(next_page, callback=self.parse)
                #yield scrapy_selenium.SeleniumRequest(url=details_link, callback=self.parse_extension, cb_kwargs={'name':name, 'user_numbers' :user_numbers[0], 'rating' :float(rating[0]), 'creator' :creator, 'key' :key})
            #    yield scrapy_selenium.SeleniumRequest(url=details_link, callback=self.parse_extension, cb_kwargs={'name':name, 'user_numbers' :user_numbers[0], 'rating' :float(rating[0]), 'creator' :creator, 'key' :key})
        # NEXT PAGE and repeat parse method.
        #next_page = response.css('a.Button.Button--cancel.Paginate-item.Paginate-item--next::attr("href")').get()
        #if next_page is not None:
      #      next_page = response.urljoin(next_page)
      #      yield scrapy_selenium.SeleniumRequest(url=next_page, callback=self.parse)

    #def parse_link(self, response):
        #pass
        #print('idhsahdsfkhafdasd')
        #print(response)