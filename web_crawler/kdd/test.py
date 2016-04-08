#!/usr/bin/env python2.7

#
# Paper Parser
#
# Author: Gary Huang <gh.nctu+code@gmail.com>
#
from lxml import html
import requests


def clear(data):
    return filter(None, [item.strip() for item in data])


def paper_parser(url):

    page = requests.get(url)
    tree = html.fromstring(page.content)

    title = tree.xpath('//*[@id="divmain"]/div/h1/strong/text()')[0]
    authors = clear(tree.xpath('//*[@id="divmain"]/table[1]/tr/td[1]/table[2]/tr/td[2]//text()'))
    affiliations = clear(tree.xpath('//*[@id="divmain"]/table[1]/tr/td[1]/table[2]/tr/td[3]//text()'))

    return {title: dict(zip(authors, affiliations))}


def save_papers(papers, fileName):
    fout = open(fileName, 'w')
    for key in papers:
        fout.write('#'+key+'\r\n')
        for author in papers[key]:
            fout.write(author+'\t'+papers[key][author]+'\r\n')
    fout.close()


if __name__ == '__main__':
    try:
        url = 'http://dl.acm.org/citation.cfm?id=2787509'
        fileName = 'test.csv'

        print 'Download paper ..'
        paper = paper_parser(url)

        print 'Write to '+fileName+' ..'
        save_papers(paper, fileName)
    except KeyboardInterrupt:
        pass

