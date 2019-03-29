#!/usr/bin/env python3
from bs4 import BeautifulSoup as bs
import sys
import requests


def tat_ca_giai():
    total = []
    ses = requests.session()
    req = ses.get('https://ketqua.net/')
    soup = bs(req.text, 'html5lib')
    for child in soup.body.table.tbody.stripped_strings:
        total.append(child)
    return total


def trung_lo(input_data):
    total = []
    ses = requests.session()
    req = ses.get('https://ketqua.net/')
    soup = bs(req.text, 'html5lib')
    for child in soup.body.table.tbody.stripped_strings:
        if child.isdigit():
            total.append(child)
    for i in total:
        if int(i[-2:]) == int(input_data):
            result = input_data
            break
        else:
            result = 'Ban khong trung'
    return result


def main():
    if len(sys.argv) >= 2:
        for i in range(1, len(sys.argv)):
            input_data = sys.argv[i]
            print("Bạn đã trúng lô {}".format(trung_lo(input_data)))
    else:
        print(tat_ca_giai())


if __name__ == "__main__":
    main()
