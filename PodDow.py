import feedparser
import urllib.request
from pathlib import Path

url = 'https://www.omnycontent.com/d/playlist/9b7dacdf-a925-4f95-84dc-ac46003451ff/662ff2d4-9b7f-4388-8a94-acb8002fd595/480aa1a5-4ada-4846-ae18-acb8002fd59e/podcast.rss'
d = feedparser.parse(url) 
d['feed']['title']

for i in d.entries:
    filename = i.title
    
    #Get episode
    ep = ""
    j = 0
    while ord(filename[0]) <= 57 and ord(filename[0]) >= 48 and not filename[j] == "-":
        ep += filename[j]
        j+=1
        
    new_ep = "(Ep." + ep + ")"
    
    #prep filename
    filename = filename.replace(":", ";")
    filename = filename.replace(ep, new_ep)
    filename = filename.replace("-", " ")
    filename = filename.replace("/", "-")
    filename = filename.replace("?", "")
    filename = filename.replace("*", "")
    filename = filename.replace("<", "")
    filename = filename.replace(">", "")
    filename += " - Jason Weiser.mp3"
    
    #already exists?
    file = Path(filename)
    if not file.is_file():
        print("\nDownloading -> " + filename + "\n...")
        data = urllib.request.urlretrieve(i.enclosures[0].url, filename)
        print("Done!\n\n")

quit()