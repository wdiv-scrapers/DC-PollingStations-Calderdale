from dc_base_scrapers.ckan_scraper import CkanScraper
from dc_base_scrapers.geojson_scraper import GeoJsonScraper


base_url = 'http://dataworks.calderdale.gov.uk/api/3/action/package_show?id='

stations_info = {
    'dataset': 'polling-stations',
    'extra_fields': [],
    'return_format': 'geojson',
}

districts_info = {
    'dataset': 'polling-station-districts',
    'extra_fields': [
        'coverage_start_date',
        'coverage_end_date',
    ],
    'return_format': 'geojson'
}

council_id = 'E08000033'


stations_meta_scraper = CkanScraper(
    base_url,
    stations_info['dataset'],
    stations_info['return_format'],
    stations_info['extra_fields'],
    'utf-8')
stations_url = stations_meta_scraper.scrape()

districts_meta_scraper = CkanScraper(
    base_url,
    districts_info['dataset'],
    districts_info['return_format'],
    districts_info['extra_fields'],
    'utf-8')
districts_url = districts_meta_scraper.scrape()


if stations_url:
    stations_scraper = GeoJsonScraper(
        stations_url, council_id, 'utf-8', 'stations')
    stations_scraper.scrape()

if districts_url:
    districts_scraper = GeoJsonScraper(
        districts_url, council_id, 'utf-8', 'districts')
    districts_scraper.scrape()
