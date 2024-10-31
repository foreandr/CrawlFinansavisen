
import hyperSel
import hyperSel.log_utilities
import hyperSel.nodriver_utilities
import hyperSel.request_utilities
import hyperSel.selenium_utilities
import hyperSel.soup_utilities
import hyperSel.spider_universal
import nodriver as nd
import asyncio
from bs4 import BeautifulSoup
import send_telegram
import re

import time
from datetime import datetime
keywords = []
root_url = ""

def custom_finance_get_request():
    # f
    pass

def scrape_forum_pagination_check(forum_page_url):
    current_date = datetime.now().strftime("%d.%m.%Y")
    driver = hyperSel.selenium_utilities.open_site_selenium(forum_page_url, show_browser=True)
    input("--")
    # soup = hyperSel.request_utilities.get_soup(forum_page_url)
    # hyperSel.log_utilities.log_function(soup)
    return False

def get_data():
    forum_root_url_template = "https://www.finansavisen.no/forum/?page=$$$"


    # get all pages with today's date
    page_numbers_to_scrape = 1
    while True:
        forum_page_url = forum_root_url_template.replace("$$$", str(page_numbers_to_scrape))
        print("forum_page_url:", forum_page_url)
        if not scrape_forum_pagination_check(forum_page_url):
            break
        page_numbers_to_scrape +=1

    # hyperSel.selenium_utilities.open_site_selenium()

    return [{},{}]


def organize_data(data):
    return [{},{}]


def sort_and_filter(data):
    return [{},{}]


def send_data(data):
    send_telegram.send_message_to_me(data)

def get_num_forum_pages():
    return 1



def get_all_post_divs(soup):
    for tag in soup.find_all("div", class_="align-right mb-3"):
        # Extract data for each post div using `tag`
        username = tag.find("a", href=True).text.strip() if tag.find("a", href=True) else None
        post_date = tag.find("span", class_="d-flex align-items-center mr-2").text.strip() if tag.find("span", class_="d-flex align-items-center mr-2") else None
        views_tag = tag.find("i", class_="fa fa-faded fa-eye mr-1")
        views = views_tag.find_next("span").text.strip() if views_tag and views_tag.find_next("span") else None
        quoted_user = tag.find("blockquote").find("em").text.strip() if tag.find("blockquote") and tag.find("blockquote").find("em") else None
        quoted_content = tag.find("blockquote").find("del").text.strip() if tag.find("blockquote") and tag.find("blockquote").find("del") else None
        post_content = tag.find("div", class_="post content text-left").text.strip() if tag.find("div", class_="post content text-left") else None
        edited_date = tag.find("span", class_="text-left d-flex post-isedited").text.strip() if tag.find("span", class_="text-left d-flex post-isedited") else None
        reply_link = tag.find("a", class_="text-xs-small")["href"] if tag.find("a", class_="text-xs-small") else None

        # Print the extracted data
        print(f"Username: {username}")
        print(f"Post Date: {post_date}")
        print(f"Views: {views}")
        print(f"Quoted User: {quoted_user}")
        print(f"Quoted Content: {quoted_content}")
        print(f"Post Content: {post_content}")
        print(f"Edited Date: {edited_date}")
        print(f"Reply Link: {reply_link}")
        print("--" * 20)  # Separator for each post


async def scrape_all_content_from_specific_post(browser, url_template):
    for i in range(1, get_num_forum_pages() + 1):
        forum_page_url = url_template.replace("$$$", str(i))
        print(i, forum_page_url)

        # Await soup fetching
        soup = await hyperSel.nodriver_utilities.get_site_soup(browser, forum_page_url, wait=20)
        posts = get_all_post_divs(soup)


        hyperSel.log_utilities.log_function(soup)
    
    # Return "hello world" after completing all scraping tasks
    return "hello world"

            

def main():
    # 1. GET ALL DATA
    data = get_data()

    # 2. ORGANIZE DATA
    # data = organize_data(data)

    # 3. SORT/FILTER DATA BY KEYWORD(S)
    # sort_and_filter(data)

    # 4. SEND DATA VIA TELEGRAM
    # send_data(data)

async def get_single_page_data():
    # Open the browser asynchronously and wait for it to be ready
    browser = await hyperSel.nodriver_utilities.open_nodriver(headless=False, proxy=None, max_attempts=3)

    # Define URL template and call the scraping function asynchronously
    # https://www.finansavisen.no/forum/thread/165943/view/0/0?page=$$$
    # https://secure.lni.wa.gov/verify/Results.aspx#%7B%22pageNumber%22%3A0%2C%22SearchType%22%3A2%2C%22SortColumn%22%3A%22Rank%22%2C%22SortOrder%22%3A%22desc%22%2C%22pageSize%22%3A10%2C%22ContractorTypeFilter%22%3A%5B%5D%2C%22SessionID%22%3A%22zp3io2zc3cp3dgjgomf1jo35%22%2C%22SAW%22%3A%22%22%2C%22Name%22%3A%22Last%20name%20or%20business%20name%22%2C%22searchCat%22%3A%22Name%22%2C%22searchText%22%3A%22Last%20name%20or%20business%20name%22%2C%22firstSearch%22%3A1%7D
    url_template = "https://www.chewy.com/"
    result = await scrape_all_content_from_specific_post(browser, url_template)  # Capture returned value
    input("--")
    hyperSel.nodriver_utilities.custom_kill_browser(browser)
    return result  # Return "hello world"

def load_file_to_soup(filename):
    # Open the file and read its contents
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    # Convert content to BeautifulSoup object
    soup = BeautifulSoup(content, 'html.parser')
    return soup

def parse_single_page_soup(soup):
    pass

if __name__ == '__main__':
    result = asyncio.run(get_single_page_data())
    #print("result:", result)
    #print("\n\n\n")
    #soup = load_file_to_soup("./demo_html.txt")
    #posts = get_all_post_divs(soup)
    pass