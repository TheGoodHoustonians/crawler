import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import constants
import scrapy

class AggregateSpider(scrapy.Spider):
  name = 'aggregatespider'
  start_urls = constants.starting_urls

  def parse(self, response):
    links = response.css('.rescue-all a::attr(href)').extract()

    for next_page in links:
      yield response.follow(next_page, self.parse_org)

  def parse_org(self, response):
    services_links = response.xpath("//a[contains(.//text(), 'Services')]").extract()
    contact_links = response.xpath("//a[contains(.//text(), 'Contact')]").extract()

    for service_page in services_links:
      yield response.follow(service_page, self.parse_service)

    for contact_page in contact_links:
      yield response.follow(contact_page, self.parse_contact)

  def parse_service(self, response):
    print('service!', response.text)

    return

  def parse_contact(self, response):
    print('contact!', response.text)

    return
