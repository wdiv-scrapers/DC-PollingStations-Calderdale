from dc_base_scrapers.hashonly_scraper import HashOnlyScraper


stations_url = "http://dataworks.calderdale.gov.uk/api/3/action/package_show?id=polling-stations"
districts_url = "http://dataworks.calderdale.gov.uk/api/3/action/package_show?id=polling-station-districts"
council_id = 'E08000033'


stations_scraper = HashOnlyScraper(stations_url, council_id, 'stations')
stations_scraper.scrape()
districts_scraper = HashOnlyScraper(districts_url, council_id, 'districts')
districts_scraper.scrape()
