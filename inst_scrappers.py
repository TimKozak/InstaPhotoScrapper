import requests
from bs4 import BeautifulSoup as bs
import selenium.webdriver as webdriver
import urllib.request
import os


def get_html(url: str):
    """
    Get page HTML structure.
    tag: either page url or instagram tag
    """
    driver = webdriver.Chrome(
        '/Users/tim/Desktop/TEENMARKET/WebScraping/chromedriver')
    driver.get(url)

    soup = bs(driver.page_source, features="html.parser")

    return soup


def scrap_insta_tag(inst) -> str:
    """
    Scrap @instagram_tag from instagram account HTML.
    """
    try:
        inst_tag = inst.body.div.section.main.div.header.section.div.h2.string
    except AttributeError:
        inst_tag = inst.body.div.section.main.div.header.section.div.h1.string

    return inst_tag


def scrap_insta_name(inst) -> str:
    """
    Scrap name from instagram account HTML.
    """
    inst_name = inst.body.div.section.main.div.header.find('h1').string
    return inst_name


def scrap_insta_image(inst) -> str:
    """
    Scrap image source from instagram account HTML.
    """
    inst_img = inst.body.div.section.main.div.header.div.div.span.img.get(
        'src')

    return inst_img


def scrap_insta_description(inst) -> str:
    """
    Scrap description from instagram account HTML.
    """
    description = inst.body.div.section.main.div.header.section.find_all(
        'div')[4].span.get_text()

    return description


def scrap_insta_product(inst) -> list:
    """
    Scrap post images from instagram account HTML.
    """
    image_divs = inst.body.div.section.main.div.find_all('a')

    product_images = []

    for image in image_divs:
        images = image.find_all('img')

        for image in images:
            img = image.attrs['srcset']
            product_images.append(img[img.find('480w')+5:-5])

    return product_images


def scrap_insta_profile_info(inst) -> list:
    """
    Scrap instagram profile and return info:
    ["tag", "name", "description", "image"]
    """
    profile_info = [scrap_insta_tag(inst),
                    scrap_insta_name(inst),
                    scrap_insta_image(inst),
                    scrap_insta_description(inst)]

    return profile_info


# unfinished functions
def scrap_insta_subscribers(inst) -> int:
    """
    Scrap instagram subscribers.
    """
    pass


def scrap_insta_subscriptions(inst) -> int:
    """
    Scrap instagram subscriptions.
    """
    pass


def scrap_insta_posts_count(inst) -> int:
    """
    Scrap instagram posts count.
    """
    pass
