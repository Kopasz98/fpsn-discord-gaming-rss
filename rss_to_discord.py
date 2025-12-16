import feedparser
import requests
import json
import os

WEBHOOK_URL = os.environ["DISCORD_WEBHOOK"]

RSS_FEEDS = [
    "https://gamerant.com/feed/gaming/",
    "https://feeds.ign.com/ign/all",
    "https://kotaku.com/rss",
    "https://www.gamespot.com/feeds/mashup/",
    "https://www.gameinformer.com/rss.xml",
    "https://n4g.com/rss/news",
    "https://www.gamesradar.com/rss",
    "https://www.theverge.com/gaming/rss/index.xml",
    "https://www.techradar.com/rss",
    "https://www.engadget.com/rss.xml",
    "https://www.digitaltrends.com/gaming/feed/",
    "https://www.thegamer.com/feed/",
    "https://www.videogameschronicle.com/feed/",
    "https://www.pcgamer.com/rss/",
    "https://www.eurogamer.net/feed",
    "https://www.polygon.com/rss/index.xml",
    "https://www.rockpapershotgun.com/feed",
    "https://www.destructoid.com/feed/",
    "https://www.giantbomb.com/feeds/news/",
    "https://www.siliconera.com/feed/",
    "https://www.shacknews.com/rss",
    "https://www.gamezone.com/feed/",
    "https://rss.slashdot.org/Slashdot/slashdotGames",
    "https://gamefaqs.gamespot.com/feeds/news.xml",
    "https://www.dexerto.com/feed/",
    "https://stealthoptional.com/feed/",
    "https://siege.gg/rss",
    "https://racinggames.gg/feed/",
    "https://mtgrocks.com/feed/",
    "https://epicstream.com/feed",
    "https://www.bluesnews.com/feed/",
    "https://www.metacritic.com/rss/games",
    "https://www.gametrailers.com/rss",
    "https://www.neogaf.com/rss",
    "https://www.gamechannel.hu/feed",
    "https://prohardver.hu/hirfolyam/rss.html",
    "https://www.pcguru.hu/rss",
    "https://www.gamestar.hu/rss",
    "https://hu.ign.com/rss",
    "https://play3.hu/feed",
    "https://www.xboxhungary.net/feed",
    "https://www.playdome.hu/rss",
    "https://www.konzolvilag.hu/rss",
    "https://ultimateconsole.hu/feed",
    "https://felhokarcolo.hu/rss",
]

POSTED_FILE = "posted.json"

if os.path.exists(POSTED_FILE):
    with open(POSTED_FILE, "r") as f:
        posted = set(json.load(f))
else:
    posted = set()

for feed_url in RSS_FEEDS:
    feed = feedparser.parse(feed_url)
    for entry in feed.entries[:5]:
        link = entry.get("link")
        if link and link not in posted:
            data = {
                "content": f"🎮 **{entry.title}**\n{link}"
            }
            requests.post(WEBHOOK_URL, json=data)
            posted.add(link)

with open(POSTED_FILE, "w") as f:
    json.dump(list(posted), f)
