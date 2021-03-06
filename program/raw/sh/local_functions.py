from lxml import html
from datetime import date

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

'''
pre-request: pip install lxml
'''

def read_html(fileName):
    return html.parse(fileName).getroot()

def get_report_link_year_and_urls(root):
    elements = root.get_element_by_id('con02-1').xpath('table[1]//a')
    return [(element.text, element.attrib['href']) for element in elements]

def get_current_year():
    return date.today().year
