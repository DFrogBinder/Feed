import json
import datetime as dt
import rfeed

# Load the JSON file containing stock ticker names
with open('stocks.json', 'r') as f:
    data = json.load(f)

# Create a list of items for the RSS feed
items = []
for stock in data["stocks"]:
    # Create an item for each stock
    item = rfeed.Item(
        title=f"{stock['ticker']} News",
        link=f"https://finance.yahoo.com/quote/{stock['ticker']}",
        description=f"Latest news about {stock['ticker']}"
    )
    items.append(item)

# Create the RSS feed
feed = rfeed.Feed(
    title="Stock News",
    link="https://www.example.com/rss",
    description="Latest news about selected stocks",
    language="en-US",
    lastBuildDate=dt.datetime.today(),
    items=items
)

# Print the RSS feed in XML format
print(feed.rss())