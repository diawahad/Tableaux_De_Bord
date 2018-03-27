# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 17:51:15 2018

@author: sceli
"""
#scrapy crawl mycrawler
import scrapy
import json
class MySpider(scrapy.Spider):
    name = "mycrawler"
    allowed_domains = ["journaldunet.com"]
    # lire le fichier contenant les liens
    with open('C:/Users/samba/Desktop/info sid/M2/projet_tab_bord/wade_scrapy/wade_scrapy/spiders/lien2759.json', 'r') as file:
        data = json.load(file)
    # affectée la liste contenant les liens a start_urls
    start_urls = data['lien']
    
    # la fonction nous permet de recuperer dans chaque lien les informations dont ont besoin
    # et return un fichier json
    def parse(self, response):
        for quote in response.selector.xpath('//html'):
            yield {
                "content" : quote.select("//div[@class='entry']/p/text()|//div[@class='entry']/p/a/text()").extract(),
                "tags" : quote.select("//section[@class='app_list_2']/aside[@class='app_tags_list see-also']/ul/li/a/text()").extract(),
                "date" : quote.select("//div[@class='entry']/aside[@class='app_author_box abs']/div/div/div/time/text()").extract(),
                "author" : quote.select("//div[@class='entry']/aside[@class='app_author_box abs']/div/div/div/dl/dt/a[@rel='author']/text()").extract(),
                "intro" : quote.select("//p[@class='app_entry_lead']/text()").extract(),
                "title" : quote.select("//title/text()").extract(),
                "titletable" : quote.select("//table/caption/text()").extract(),
                "colnames" :quote.select("//table/thead/tr/th/text()").extract(),
                "record" : quote.select("//table/tbody/tr/th/text()|//table/tbody/tr/td/text()").extract(),
                
            }
    