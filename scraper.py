from dc_base_scrapers.geojson_scraper import GeoJsonScraper


stations_url = "http://inspire.eden.gov.uk/inspireeden/EDEN/wms?service=WFS&version=1.3.0&request=GetFeature&typeNames=PollingStations&outputFormat=json&srsName=EPSG%3A4326"
districts_url = "http://inspire.eden.gov.uk/inspireeden/EDEN/wms?service=WFS&version=1.3.0&request=GetFeature&typeNames=PollingDistricts&outputFormat=json&srsName=EPSG%3A4326"
council_id = 'E07000030'


stations_scraper = GeoJsonScraper(stations_url, council_id, 'utf-8', 'stations')
stations_scraper.scrape()
districts_scraper = GeoJsonScraper(districts_url, council_id, 'utf-8', 'districts')
districts_scraper.scrape()
