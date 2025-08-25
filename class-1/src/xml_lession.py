import xml.etree.ElementTree as ET


rss = """<?xml version="1.0"?>
<rss version="2.0">
  <channel>
    <title>Demo Feed</title>
    <item>
      <title>Alert A</title>
      <link>https://example.com/a</link>
      <pubDate>Mon, 11 Aug 2025 10:00:00 GMT</pubDate>
    </item>
    <item>
      <title>Alert B</title>
      <link>https://example.com/b</link>
      <pubDate>Mon, 11 Aug 2025 11:00:00 GMT</pubDate>
    </item>
  </channel>
</rss>"""

root = ET.fromstring(rss)
# print("this is the root: ", root)
channel = root.find("channel")
# print("this is the channel: ", channel)
items = channel.findall("item")
# print("this is the item: ", items)

row = []
for item in items:
    row.append(
        {
            "title": item.findtext("title"),
            "link": item.findtext("link"),
            "data": item.findtext("pubDate")
        }
    )

# print(row)

tree = ET.parse('class-1/data/country_data.xml')
root = tree.getroot()
data = root.findall("country")
my_countries = []
for country in data:
    my_countries.append(
        {
            "rank": country.findtext("rank"),
            "country": country.attrib['name'],
            "year": country.findtext("year"),
            "gdppc": country.findtext("gdppc"),
            "neighbor": country.findtext("neighbor"),
        }
    )

print(my_countries)