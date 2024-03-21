import requests
from bs4 import BeautifulSoup
import os
import threading

def download_image(url, directory):
    # 发送HTTP请求获取图片数据
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        # 提取图片文件名
        file_name = url.split('/')[-1]
        # 拼接保存路径
        save_path = os.path.join(directory, file_name)
        # 保存图片数据到文件
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"图片下载完成: {file_name}")
    else:
        print(f"图片下载失败: {url}")

def scrape_images(url_prefix, page_range, directory):
    # 创建保存图片的目录
    os.makedirs(directory, exist_ok=True)
    
    for page_num in page_range:
        # 构建完整的网页URL
        if page_num == 1:
            url = url_prefix
        else:
            url = f"{url_prefix}/{page_num}/"
        # 发送HTTP请求获取网页内容
        response = requests.get(url)
        if response.status_code == 200:
            # 使用BeautifulSoup解析网页内容
            soup = BeautifulSoup(response.text, 'html.parser')
            # 查找class为"single-content"的div
            div_tag = soup.find('div', class_='single-content')
            if div_tag:
                # 查找<div>标签下的<p>标签
                p_tags = div_tag.find_all('p')
                # 遍历每个<p>标签
                for p_tag in p_tags:
                    # 查找<p>标签下的<img>标签
                    img_tag = p_tag.find('img')
                    if img_tag:
                        # 提取图片URL
                        img_url = img_tag['data-lazy-src']
                        # 下载图片
                        if img_url.startswith('http://img.177picyy.com/uploads/2019/03b/'):
                            t = threading.Thread(target=download_image, args=(img_url, directory))
                            t.start()

            else:
                print(f"第 {page_num} 页：未找到符合条件的div标签")
        else:
            print(f"第 {page_num} 页：网页请求失败")

# 测试
url_prefix = 'http://www.177picyy.com/html/2019/04/2846078.html'  # 网页URL前缀
page_range = range(1, 13)  # 要爬取的页面范围
directory = 'images'  # 替换为你要保存图片的目录

scrape_images(url_prefix, page_range, directory)
