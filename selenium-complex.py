#!/usr/bin/env python2
# -*- coding: utf8 -*-

# https://github.com/rainsdance/indroid-python-requests

# Junior Application Developer at indroid
# 2. Also make a function which accepts a string and returns the Google results.
# This time do it with a different method: use Python and Selenium,
# which controls a browser (default: Firefox). 

# modification of https://github.com/DanMcInerney/search-google

# imports the sys, time, random, and argparse modules
import sys
import time
import random
import argparse

# imports several functions from the selenium module
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.common.exceptions import NoSuchFrameException
from selenium.webdriver.common.keys import Keys

# defines the search argument which is passed to the script when it's run
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--search', help='Enter the search term')
    return parser.parse_args()

# start the firefox browser
def start_browser():
    br = webdriver.Firefox()
    br.implicitly_wait(10)
    return br

# grab the title and url of the results
def scrape_results(br):
    # Xpath will find a subnode of h3, a[@href] specifies that we only want <a> nodes with
    # any href attribute that are subnodes of <h3> tags that have a class of 'r'
    links = br.find_elements_by_xpath("//h3[@class='r']/a[@href]")
    results = []
    for link in links:
        title = link.text.encode('utf8')
        url = link.get_attribute('href')
        title_url = (title, url)
        results.append(title_url)
    return results

# navigates to the google.com results page with ten results
def go_to_page(br, page_num, search_term):
    page_num = page_num - 1
    start_results = page_num * 10
    start_results = str(start_results)
    url = 'https://www.google.com/webhp?#num=10&start='+start_results+'&q='+search_term
    print '[*] Fetching 10 results from page '+str(page_num+1)+' at '+url
    br.get(url)
    time.sleep(2)

# main script which pulls together the previous scripts to display the results
# in firefox
def main():
    args = parse_args()
    br = start_browser()
    search_term = args.search

    all_results = []
    for page_num in xrange(int(1)):
        page_num = page_num+1 # since it starts at 0
        go_to_page(br, page_num, search_term)
        titles_urls = scrape_results(br)
        for title in titles_urls:
            all_results.append(title)

    for result in all_results:
        title = result[0]
        url = result[1]
        print '[+]', title, '--', url

# gives this module import and testing accessibility
main()
