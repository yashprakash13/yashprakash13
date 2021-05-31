from pathlib import Path
import datetime

import feedparser

def update_readme_medium_posts(medium_feed, readme_base, join_on):
    d = feedparser.parse(medium_feed)
    posts = []
    for item in d.entries:
        if item.get('tags'):
            posts.append(f" - [{item['title']}]({item['link']})")
    posts_joined = '\n'.join(posts)
    return readme_base[:readme_base.find(rss_title)] + f"{join_on}\n{posts_joined}"

rss_title = "### My latest stories on Medium" # Anchor for where to append posts
readme = Path('../README.md').read_text()
updated_readme = update_readme_medium_posts("https://medium.com/feed/@ipom", readme, rss_title)
with open('../README.md', "w+") as f:
    f.write(updated_readme)
