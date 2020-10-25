#!/home/martin/local/python/parsing/bin/python
import feedparser
import html2markdown

url = 'https://www.archlinux.org/feeds/news/'
number_of_entries = 3

feed_entries = feedparser.parse(url).entries

with open('/tmp/arch_news.html','w') as f:
    f.write('<h1> News feed of wwww.archlinux.org</h1>')
    for i, e in enumerate(feed_entries):
        if i >= number_of_entries:
            break
        f.write('<h2>'+ e.title + '</h2>\n')
        f.write(e.description + '\n')
        f.write(3*'<br>&nbsp;<br>\n')

