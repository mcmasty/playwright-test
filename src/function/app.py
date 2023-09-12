from playwright.sync_api import sync_playwright
from datetime import datetime


def handler(event, context):
    print(f"Here are the Event Params {event}")
    print(f"Here is the context: {context}")
    with sync_playwright() as p:
        print("Hello There!!")
        browser = p.chromium.launch(args=["--disable-gpu", "--single-process"])
        # browser = p.firefox.launch(args=["--disable-gpu", "--single-process"])
        page = browser.new_page()
        urls = ["http://whatsmyuseragent.org/"]
        for k in event.keys():
            if 'url' in k:
                urls += [event[k]]
        print(urls)
        for u in urls:
            page.goto(u)
            pg_title = page.title()
            print(f"page Tile: {pg_title}")
            print(f"Page Title Reversed: {pg_title[::-1]}")
        print(f"finished at {datetime.now()}")
        browser.close()