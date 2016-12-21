# Scrap a single page and get all the metadata.

# Import scrapy library.
import scrapy


class MetaSpider(scrapy.Spider):

    name = 'meta_spider'

    allowed_domains = [
        'southampton.ac.uk',
    ]

    start_urls = [
        'http://www.southampton.ac.uk/maths/undergraduate/courses/g120_mathematical_studies.page',
    ]

    # The default function `parse(self, response)` called by Scrapy to create the results.
    def parse(self, response):
        # Get the URL of the curent page
        page_url = response.url
        # Get the status (200, 301, 404)
        page_status = response.status
        # Get the <title>
        page_title = response.xpath('//title/text()').extract_first()
        # Create list with the <meta> name
        page_meta_list_name = response.xpath('//meta/@name').extract()
        # Create list with the <meta> content
        page_meta_list_value = response.xpath('//meta/@content').extract()
        # Create a joined list like:  [["meta-name-1", "meta-content-1"],
        # ["meta-name-1", "meta-content-1"]]
        page_meta_list_array = []
        for i in range(len(page_meta_list_name)):
            page_meta_list_array.append(
                [page_meta_list_name[i], page_meta_list_value[i]])
        # Create a dictionary combining the two metatag lists
        page_meta_list_dictionary = {}
        for i in range(len(page_meta_list_name)):
            page_meta_list_dictionary[
                page_meta_list_name[i]] = page_meta_list_value[i]
        # Get <meta name="keywords"> value
        page_meta_keywords = response.xpath(
            '//meta[@name=\'keywords\']/@content').extract_first()
        # Get <meta name="non-existing-tag"> to check what happend when we
        # target something that does not exist
        page_meta_non_existing_tag = response.xpath(
            '//meta[@name=\'non-existing-tag\']/@content').extract_first()
        # Get a spesific tag
        page_meta_spesific = response.xpath(
            '/html/head/meta[3]').extract_first()

        yield {
            'html': response.body,
            'url': page_url,
            'status': page_status,
            'title': page_title,
            'meta-list-array': page_meta_list_array,
            'meta-list-dictionary': page_meta_list_dictionary,
            'meta-keywords': page_meta_keywords,
            'meta-non-existing-tag': page_meta_non_existing_tag,
            'meta-spesific': page_meta_spesific,
        }
