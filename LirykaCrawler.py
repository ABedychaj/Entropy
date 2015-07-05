# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re


def liryka_spider(max_pages=2):
    page = 1
    while page < max_pages:
        url = 'http://wolnelektury.pl/katalog/rodzaj/liryka/?page=' \
              + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        href = list()
        for elem in soup(text=re.compile(r'TXT')):
            OnlyPolishTexts = \
                elem.parent.parent.parent.parent.parent.parent
            if str(OnlyPolishTexts).find(u'Język:') == -1:
                href.append('https://wolnelektury.pl'
                            + elem.parent.get('href'))
        print(href)
        page += 1
        get_text(href)


def get_text(href_list):
    for href in href_list:
        source_code = requests.get(href)
        LastSign = source_code.text.rfind('-----')
        groups = re.search('txt/(.*)\.txt', href, flags=0)
        f = open(''.join(['H:/Teksty/Liryka/', groups.group(1), '.txt']),
                 'w',
                 encoding='utf-8')
        for t in range(0, LastSign):
            f.write(source_code.text[t])

liryka_spider(114)
