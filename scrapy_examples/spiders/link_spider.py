# Follows links recursively and scraps the `URL`, the ``<title>`` and the `html document`.
# on all pages under a path on a given domain.

# Import scrapy library.
import scrapy
# Add extra libraries.
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class MySpider(CrawlSpider):

    # The spider's name must be unique in a project.
    name = 'link_spider'

    # Allow crawling only inside these domains.
    # Be careful with the subdomains. Use the www.example.com to restrict on
    # the primary domain.
    allowed_domains = [
        'example.com',
    ]

    # You can have multiple starting points if some areas of the site are not
    # discoverable or you don't want to follow links and specify a list of
    # pages.
    start_urls = [
        'http://example.com/',
    ]

    rules = (
        # To filter the crawled  links use the allow=() and deny=() parameters
        # for the LinkExtractor().
        # For example the `LinkExtractor(allow=r'maths/')` allows only URLs
        # containing the string `math/`.
        # For more information:
        # https://doc.scrapy.org/en/latest/topics/link-extractors.html#scrapy.linkextractors.lxmlhtml.LxmlLinkExtractor
        Rule(LinkExtractor(), callback='parse_url', follow=True),
    )

    # Function called by the `Rule` to create the results.
    def parse_url(self, response):
        # `yield` is like `return` but returns a `generator`.
        # for more information:
        # https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/
        # http://stackoverflow.com/a/231855/1692965
        yield {
            # Get the URL
            'url': response.url,
            # Get the html document
            'html': response.body,
            # Get the <title>
            'title': response.xpath('//title/text()').extract_first(),
        }
