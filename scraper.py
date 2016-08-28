from geojson_scraper import scrape


stations_url = "http://inspire.eden.gov.uk/inspireeden/EDEN/wms?service=WFS&version=1.3.0&request=GetFeature&typeNames=PollingStations&outputFormat=json&srsName=EPSG%3A4326"
districts_url = "http://inspire.eden.gov.uk/inspireeden/EDEN/wms?service=WFS&version=1.3.0&request=GetFeature&typeNames=PollingDistricts&outputFormat=json&srsName=EPSG%3A4326"
council_id = 'E07000030'


scrape(stations_url, council_id, 'utf-8', 'stations')
scrape(districts_url, council_id, 'utf-8', 'districts')
