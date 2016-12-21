# Scrapy example spider

This is a test crawler containing the spiders:

- meta_spider (gets the `<meta>` tags from a single page)
- link_spider (follows links recursively and scraps the `URL`, the `<title>` and the `html document` on all pages under a path on a given domain.)

Official page: <https://scrapy.org/><br>
Official documentation: <https://doc.scrapy.org/en/latest/>

## Get started

- Install Python (tested on 2.7.12): <https://www.python.org/downloads/>
- Install Scrapy (tested on 1.2.1): <https://doc.scrapy.org/en/latest/intro/install.html>
- Clone this project: `git clone REPOSITORY`
- Go in the project: `cd scrapy_examples`
- Run `scrapy crawl meta_spider`, if you want to store the data on a json file run: `scrapy crawl meta_spider -o data.json`

## Scrapy Cheatsheet

Initialize a project

```
scrapy startproject projectname
```

File structure

```
projectname/              # Project root
    scrapy.cfg            # Project configuration file
    projectname/
        __init__.py
        items.py          # Define items to scrap
        pipelines.py      # pipeline configuration
        settings.py       # Settings
        spiders/          # Directory for spiders
            __init__.py
```

Initialize a spider (execute inside a project)

```
scrapy genspider example example.com
```

Run a spider

```
scrapy runspider projectname/spiders/spidername.py -o data.json
# or
scrapy crawl spidername -o data.json
```

To debug a variable install `pip install var_dump`

```
# Import library var_dump
from var_dump import var_dump
# Do stuff with the var `my_variable`
# Dump the `my_variable`
var_dump(my_variable)
```

Selectors and output examples

```
def parse(self, response):

      yield {
          'url': response.url,
          'title': response.xpath('//title/text()').extract_first(),
          'titlebar': response.xpath('//*[@id="pagecontainer"]/section/h2/text()').extract()
          'time': response.xpath('//*[@id="display-date"]/time/@datetime').extract()[0]

      }

      for quote in response.css('div.quote'):
          yield {
              'text': quote.css('span.text::text').extract_first(),
              'author': quote.css('span small::text').extract_first(),
              'tags': quote.css('div.tags a.tag::text').extract(),
          }
```
