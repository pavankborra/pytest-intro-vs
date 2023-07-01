from urllib.request import urlopen
from html.parser import HTMLParser

class WeatherParser(HTMLParser):
    def _init_(self):
        super()._init_()
        self.in_location = False
        self.in_temperature = False
        self.in_description = False
        self.location = ""
        self.temperature = ""
        self.description = ""

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "span" and "class" in attrs:
            classes = attrs["class"].split()
            self.in_location = "wr-c-location__name" in classes
            self.in_temperature = "wr-value--temperature--c" in classes
            self.in_description = "wr-c-weather-type-description" in classes

    def handle_data(self, data):
        if self.in_location:
            self.location = data.strip()
            self.in_location = False
        elif self.in_temperature:
            self.temperature = data.strip()
            self.in_temperature = False
        elif self.in_description:
            self.description = data.strip()
            self.in_description = False

def get_weather(location):
    with urlopen(f"https://www.bbc.co.uk/weather/{location}") as response:
        parser = WeatherParser()
        parser.feed(response.read().decode())
        print(f"Weather in {parser.location}: {parser.description}, Temperature: {parser.temperature}")

def main():
    get_weather('2147714')  # Dubai's location ID on BBC Weather

if _name_ == "_main_":
    main()