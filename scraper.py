from dc_base_scrapers.datapress_scraper import DataPressScraper
from dc_base_scrapers.hashonly_scraper import HashOnlyScraper


base_url = 'https://dataworks.calderdale.gov.uk/api/dataset/'

stations_info = {
    'dataset': 'polling-stations',
    'extra_fields': [],
    'return_format': 'json',
}

districts_info = {
    'dataset': 'polling-station-districts',
    'extra_fields': [],
    'return_format': 'json'
}

council_id = 'E08000033'

stations_meta_scraper = DataPressScraper(
    base_url,
    council_id,
    stations_info['dataset'],
    stations_info['return_format'],
    stations_info['extra_fields'],
    'utf-8')
stations_meta_scraper.scrape()

districts_meta_scraper = DataPressScraper(
    base_url,
    council_id,
    districts_info['dataset'],
    districts_info['return_format'],
    districts_info['extra_fields'],
    'utf-8')
districts_meta_scraper.scrape()

stations_url = "%s%s" % (base_url, stations_info['dataset'])
districts_url = "%s%s" % (base_url, districts_info['dataset'])

stations_scraper = HashOnlyScraper(stations_url, council_id, 'stations')
stations_scraper.scrape()
districts_scraper = HashOnlyScraper(districts_url, council_id, 'districts')
districts_scraper.scrape()
