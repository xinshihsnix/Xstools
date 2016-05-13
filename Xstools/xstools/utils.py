# coding: utf-8
import datetime
import time
import base64


class TimeUtils(object):
    def int_time_to_str_format(cls):
        """ 1343142315.35345 --> '134314231535345' """
        return str(time.time()).replace('.', '')

    def time_now_to_str_format(cls):
        return datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')


class FileUtils(object):
    def unique_file_name_from_url(cls, url):
        """
        http://xxxx/yy.jpg -> 1212353426.jpg
        """
        full_name = url.split('/')[-1]
        postfix = full_name.split('.')[-1]
        unique_full_name = TimeUtils.int_time_to_str_format() + '.' + postfix
        return unique_full_name

    def unique_file_name_from_url(cls, url):
        """
        http://xxxx/yy.jpg -> 1212353426.jpg
        """
        full_name = url.split('/')[-1]
        postfix = full_name.split('.')[-1]
        unique_full_name = TimeUtils.int_time_to_str_format() + '.' + postfix
        return unique_full_name


class StringUtils(object):
    def zip_string(cls, char):
        """ 压缩字符串 """
        pass

    def unzip_string(cls, char):
        """ 解压字符串 """
        pass


class ImgUtils(object):
    def img_to_base64_by_object(cls, img):
            s = base64.b64encode(img)
            return s

    def img_to_base64_by_path(cls, img_path):
        """ 将图片转为字符串 """
        with open(img_path, 'rb') as img_f:
            s = base64.b64encode(img_f.read())
            return s

    @classmethod
    def base64_to_img_as_path(cls, b64, img_path):
        f = open(img_path, 'wb')
        f.write(b64.decode('base64'))
        f.close()