import json
import rfeed

# Load the JSON file containing stock ticker names
with open('stocks.json', 'r') as f:
    stocks = json.load(f)

# Create a list of items for the RSS feed
items = []
for stock in stocks:
    # Create an item for each stock
    item = rfeed.Item(
        title=f"{stock} News",
        link=f"https://finance.yahoo.com/quote/{stock}",
        description=f"Latest news about {stock}"
    )
    items.append(item)

# Create the RSS feed
feed = rfeed.Feed(
    title="Stock News",
    link="https://www.example.com/rss",
    description="Latest news about selected stocks",
    language="en-US",
    lastBuildDate=datetime.datetime.now(),
    items=items
)

# Print the RSS feed in XML format
print(feed.rss())