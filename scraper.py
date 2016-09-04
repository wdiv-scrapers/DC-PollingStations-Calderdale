from ckan_scraper import scrape_resources
from geojson_scraper import scrape


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


stations_url = scrape_resources(
    base_url,
    stations_info['dataset'],
    stations_info['return_format'],
    stations_info['extra_fields'],
    'utf-8')
districts_url = scrape_resources(
    base_url,
    districts_info['dataset'],
    districts_info['return_format'],
    districts_info['extra_fields'],
    'utf-8')


if stations_url:
    scrape(stations_url, council_id, 'utf-8', 'stations')
if districts_url:
    scrape(districts_url, council_id, 'utf-8', 'districts')
