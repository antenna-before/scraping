import os
# from urllib.request import urlretrieve  # 第一种方法
import requests  # 第二种方法
from bs4 import BeautifulSoup

'''
If the target directory already exists, raise an OSError if exist_ok is False. Otherwise no exception is raised.  
This is recursive. 如果已存在要创建的文件夹，则会报错，除非使用了exist_ok=True
'''
os.makedirs('img', exist_ok=True)  #


URL = 'https://www.ce.jhu.edu/dalrymple/classes/602/'
# html = requests.get(URL).text
# soup = BeautifulSoup(html, 'lxml')
# img_ul = soup.find_all('ul', {'class': 'tut-course-thumbnail'})
# # print(html)
# print(img_ul)

img_ul = []

for i in range(3, 20):
    pdf_str = 'Class' + str(i) + '.pdf'
    img_ul.append(pdf_str)


for ul in img_ul:
    src = ul
    print(src)

    # 得到具体的图片连接
    # stream=True：时时刻刻下载？
    r = requests.get(URL + src, stream=True)

    img_name = src.split('/')[-1]  # 去掉字符串最后一个/之前的东东，作为文件名

    with open('pdf/'+ img_name, 'wb') as f:  # ‘wb’ 以二进制方式写入文件
        for chunk in r.iter_content(chunk_size=128):  # 离散的下载写入，而不是全部下载到内存之后再保存
            f.write(chunk)

    print('Saved :{}'.format(img_name))