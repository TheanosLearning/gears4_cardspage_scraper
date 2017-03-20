# gears4_cardpage_scraper

### Scrapes [gearsofwar.com](https://gearsofwar.com/en-us/cards) for any upcoming cards data, new characters & packs.

View the data I have scraped in the [data](https://github.com/TheanosLearning/gears4_cardspage_scraper/tree/master/data) folder:

* [initialState.json](https://github.com/TheanosLearning/gears4_cardspage_scraper/blob/master/data/initialState.json)
* [text.json](https://github.com/TheanosLearning/gears4_cardspage_scraper/blob/master/data/text.json)

> Data will be updated every week or upon request.

Or run the project yourself:

Assuming you have [python](https://www.python.org/) and [anaconda](https://www.continuum.io/downloads) installed

1. Create a new environment ```conda create --name scrapy```

2. Switch to it ```source activate scrapy```

3. Install Scrapy ```conda install Scrapy```

4. Create a new Scrapy project ```scrapy startproject gears4_cardspage_scraper```

5. Copy the contents of ```cardspage_spider.py``` and place it in the ```/spiders``` directory

6. Create a ```data``` directory in project root ```mkdir data```

7. Execture the script to crawl & scrape the page ```scrapy crawl cardspage```

8. ```text.json``` & ```initialState.json``` will be written to your ```/data``` folder
