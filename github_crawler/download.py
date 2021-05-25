#coding=utf-8
import re
"""
目标：提供一个函数能够从网上下载资源
输入：
    url列表
    保存路径
输出：
    保存到指定路径中的文件
要求：
    能够实现下载过程，即从0%到100%可视化
"""
# =====================================================
from six.moves import urllib
import os
import sys


def download_and_extract(filepath, save_dir):
    """根据给定的URL地址下载文件

    Parameter:
        filepath: list 文件的URL路径地址
        save_dir: str  保存路径
    Return:
        None
    """
    remain_txt = open('remaining_PHP.txt','a')           #need to edit
    count = 0
    for txt, index in zip(filepath, range(len(filepath))):
        #txt = txt.split()                                        #need to edit
        #print('0', txt,type(txt))
        #url = txt[0]                                             #need to edit
        url = txt
        #print('1',url)
        language ='PHP' #txt[1]                                        #need to edit
        filename = re.findall("/(.*?)/archive/refs/heads/master.zip",url)[0]
        #print(filename)
        filename = filename[filename.rfind('/')+1:len(filename)]
        #print('2',filename)
        try:
            save_dir_this = os.path.join(save_dir, filename)
            if not os.path.exists(save_dir_this):
                os.makedirs(save_dir_this)
            save_path = os.path.join(save_dir_this, filename+'.zip')
            if not os.listdir(save_dir_this):
                urllib.request.urlretrieve(url, save_path)
                print(filename, 'has been Reloaded.\n')
                desc_path = os.path.join(save_dir_this, 'desc.yml')
            else:
                print(filename,'has already been loaded. ')
            if not os.path.exists(desc_path):
                desc = open(desc_path,'w')
                desc.write("name: " + filename + '\nlanguage: ' + language + '\ntime: \ndescription: ')
                desc.close()
        except:  #urllib.error.ContentTooShortError:
            print ('Sorry! Network conditions is not good.',filename,'not Reloaded.\n')
            if not os.listdir(save_dir_this):
                os.rmdir(save_dir_this)
            remain_txt.write(url+'\n')
            count = count + 1
            #urllib.urlretrieve(url,filename)

        #urllib.request.urlretrieve(url, save_path)
        sys.stdout.write('\r>> Downloading %.1f%%\n' % (float(index + 1) / float(len(filepath)) * 100.0))
        sys.stdout.flush()
    print('\nSuccessfully downloaded')
    print('\n',len(filepath)-count, 'succeeded and', count, 'failed.')
    remain_txt.close()


def _get_file_urls(file_url_txt):
    """根据URL路径txt文件，获取URL地址列表

    Parameter:
        file_url_txt: str  txt文件本地路径
    Return:
        filepath: list  URL列表
    """
    filepath = []
    file = open(file_url_txt, 'r')
    for line in file.readlines():
        line = line.strip()
        filepath.append(line)
    file.close()
    return filepath


if __name__ == '__main__':
    file_url_txt = 'clean_url_php_new.txt'              #need to edit
    save_dir = 'PHP'                               #need to edit
    filepath = _get_file_urls(file_url_txt)[100:300]
    download_and_extract(filepath, save_dir)
