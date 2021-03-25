from dc_base_scrapers.datapress_scraper import DataPressScraper
from dc_base_scrapers.geojson_scraper import GeoJsonScraper
from dc_base_scrapers.hashonly_scraper import HashOnlyScraper

#
# base_url = 'https://dataworks.calderdale.gov.uk/api/dataset/'
#
# stations_info = {
#     'dataset': 'polling-stations',
#     'extra_fields': [],
#     'return_format': 'json',
# }
#
# districts_info = {
#     'dataset': 'polling-station-districts',
#     'extra_fields': [],
#     'return_format': 'json'
# }

council_id = 'CLD'

# stations_meta_scraper = DataPressScraper(
#     base_url,
#     council_id,
#     stations_info['dataset'],
#     stations_info['return_format'],
#     stations_info['extra_fields'],
#     'utf-8')
#
# stations_meta_scraper.scrape()
#
# districts_meta_scraper = DataPressScraper(
#     base_url,
#     council_id,
#     districts_info['dataset'],
#     districts_info['return_format'],
#     districts_info['extra_fields'],
#     'utf-8')
# districts_meta_scraper.scrape()
# stations_url = "%s%s" % (base_url, stations_info['dataset'])
stations_url = "https://dataworks.calderdale.gov.uk/download/polling-stations/f9b00312-f330-4d18-a944-7cfd36c8d0eb/Polling%20stations.geojson"
# districts_url = "%s%s" % (base_url, districts_info['dataset'])
districts_url = "https://dataworks.calderdale.gov.uk/download/polling-station-districts/2482d9f3-7eae-4ea6-980c-718e9723e64a/Polling%20districts.geojson"

# stations_scraper = HashOnlyScraper(stations_url, council_id, 'stations', 'json')
stations_scraper = GeoJsonScraper(stations_url,council_id, 'utf-8', 'stations', key='POLLING_LETTERS')
stations_scraper.scrape()
districts_scraper = GeoJsonScraper(districts_url,council_id, 'utf-8', 'districts', key='POLLING_LETTERS')
districts_scraper.scrape()
