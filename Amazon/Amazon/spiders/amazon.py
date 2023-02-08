import scrapy

class SpiderAmazon(scrapy.Spider):
    name = 'amazon'
    start_urls = ['https://www.amazon.com.mx/s?k=juguetes+para+perro']
    # start_urls = ['https://www.amazon.com.mx/s?k=whisky']
    custom_settings = {
        'FEED_URI': 'amazon2.json', 
        'FEED_FORMAT': 'json',
        'FEED_EXPORT_ENCODING': 'utf-8',
        'ROBOTSTXT_OBEY': True,
        'USER_AGENT': 'Chrome/104.0.5112.101',
    }


    # Scrapeo recursivo chipotludo 3000.
    def parse(self, response):
        product_links = response.xpath('//div[@data-uuid]//h2/a/@href').getall()
        for link in product_links:
            yield response.follow(link, callback=self.parse_product, cb_kwargs = {'URL': response.urljoin(link)})
           
        next_page_button_link = response.xpath('//span[@class = "s-pagination-strip"]/a[contains(@aria-label, "siguiente") or contains(@aria-label, "next")]/@href').get()
        if next_page_button_link:
            yield response.follow(next_page_button_link, callback=self.parse)

      
    def parse_product(self, response, **kwargs):
        url = kwargs['URL']
        product_name = response.xpath('//div[@id = "centerCol"]//span[@id = "productTitle"]/text()').get()
        price_int = response.xpath('//div[@id = "centerCol"]//span[@class = "a-price-whole"]/text()').get()
        price_float = response.xpath('//div[@id = "centerCol"]//span[@class = "a-price-fraction"]/text()').get()
        if price_int and price_float:
            price = (price_int + "." + price_float)
        else:
            price = response.xpath('//td/span[contains(@class, "a-price")]/span[@class]/text()').getall()[0]

        score = response.xpath('//div[contains(@class, "a-col-left")]//span[@data-hook = "rating-out-of-text"]/text()').get()
        if not score:
            score = 'N/A'

        reviewers = response.xpath('//div[@data-hook = "total-review-count"]/span/text()').get()
        if not reviewers:
            reviewers = 'N/A'
        
        stars = response.xpath('//table[@id = "histogramTable"]//tr//span[@class = "a-size-base"]/a/text()').getall()
        na_stars = response.xpath('//table[@id = "histogramTable"]//tr[@class = "a-histogram-row"]//span[@class = "a-size-base"]/text()').getall()

        ranking = stars + na_stars

        for i in range(len(ranking)):
            ranking[i] = ranking[i].strip()
        
        yield {
            'Producto': product_name.strip(),
            'Precio': price,
            'URL': url,
            'Calif': score,
            'No_Calif': reviewers.strip(),
            ranking[8]: ranking[9],
            ranking[6]: ranking[7],
            ranking[4]: ranking[5],
            ranking[2]: ranking[3],
            ranking[0]: ranking[1],
        }