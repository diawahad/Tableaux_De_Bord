# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 10:46:43 2018

@author: samba
"""
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "projet"
    # la liste des années de publication d'article sur le E_commerce
    start_urls = [
        'https://www.journaldunet.com/ebusiness/commerce/list/2007-12-1/',
        'https://www.journaldunet.com/ebusiness/commerce/list/2006-11-1/',
        'https://www.journaldunet.com/ebusiness/commerce/list/2008-12-1/',
        'https://www.journaldunet.com/ebusiness/commerce/list/2009-12-1/',
        'https://www.journaldunet.com/ebusiness/commerce/list/2010-12-1/',
        'https://www.journaldunet.com/ebusiness/commerce/list/2011-12-1/',
        'https://www.journaldunet.com/ebusiness/commerce/list/2012-12-1/',
        'https://www.journaldunet.com/ebusiness/commerce/list/2013-12-1/',
        'https://www.journaldunet.com/ebusiness/commerce/list/2014-12-1/',
        'https://www.journaldunet.com/ebusiness/commerce/list/2015-12-1/',
        'https://www.journaldunet.com/ebusiness/commerce/list/2016-12-1/',
        'https://www.journaldunet.com/ebusiness/commerce/list/2017-12-1/',
        'https://www.journaldunet.com/ebusiness/commerce/list/2018-2-1/'
        
    ]
    # la fonction permet de recuperer pour chaque année les liens des articles qui parle du E_commerce
    # return un fichier json avec les liens des articles
    def parse(self, response):
        for quote in response.selector.xpath('//html'):
            yield {
                'lien': quote.select('//li/h4/a/@href').extract(),
                'tittle': quote.select('//li/div/div[@class="grid_left"]/a/@title').extract(),
            }
        next_page = response.selector.xpath('//section[@class="ccmcss_paginator ccmcss_paginator--date"]/div[1]/ul/li/a[@class=""]/@href').extract()
        print(next_page)
        for i in range (len(next_page)):
            yield scrapy.Request(next_page[i])
    

"""
scrapy crawl projet -o lien.json
"""

    
    
    
    
    