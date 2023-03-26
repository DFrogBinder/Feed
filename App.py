import xml.etree.ElementTree as ET
from flet import App, List, Label

class NewsItem:
    def __init__(self, title, link):
        self.title = title
        self.link = link

class MyApp(App):
    def __init__(self):
        super().__init__()
        self.news_items = []

    def on_start(self):
        # Load the news items from the XML file
        tree = ET.parse('news.xml')
        root = tree.getroot()
        for item in root.findall('item'):
            title = item.find('title').text
            link = item.find('link').text
            self.news_items.append(NewsItem(title, link))

        # Create a list to display the news items
        news_list = List()
        for item in self.news_items:
            # Create a label for each news item
            label = Label(item.title)
            news_list.add(label)
        self.root.add(news_list)

if __name__ == '__main__':
    MyApp().run()