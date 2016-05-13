# coding: utf-8
import urllib, re
from utils import FileUtils

class HttpTool(objects):
    def __init__(self):
        pass

    def get_imgs_from_html_page(self, save_path, url):
        cxt = ''.join(urllib.urlopen(url).readlines())

        img_list = re.findall('http\S*(?:jpg|png|gif)', cxt)
        for img in img_list:
            urllib.urlretrieve(img, save_path + FileUtils.unique_file_name_from_url(img))
