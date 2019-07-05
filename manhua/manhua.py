import requests
from pyquery import PyQuery as pq
import json
import time
from openpyxl import Workbook

lines =[]

def get_html(url):
    print('正在爬取第',i, '页')
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    return None
    time.sleep(10)


def parse_html(html):
    doc = pq(html)
    items = doc.find('.item-1').items()
    for item in items:
        data = {}
        data['封面图片'] = item.find('img').attr('src')
        data['漫画名'] = item.find('.title').text()
        data['内容简介'] = item.find('p').text()
        datalist = [data['封面图片'], data['漫画名'], data['内容简介']]
        lines.append(datalist)
        save_to_file(lines)




def save_to_file(lines):
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.append(['封面图片','漫画名', '内容简介'])
    for line in lines:
        worksheet.append(line)
    workbook.save('漫画.xlsx')



def main(page):
    url = 'https://www.hao123.com/manhua/list/?finish=%E5%B7%B2%E5%AE%8C%E7%BB%93&audience=&area=&cate=&order=&pn=' + str(page)
    html = get_html(url)
    lines = parse_html(html)


if __name__ == '__main__':
    for i in range(1,200):
        main(i)
