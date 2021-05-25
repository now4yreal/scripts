# coding=utf-8
import sys  
  
reload(sys)  
sys.setdefaultencoding('utf8')
import os
import json
import requests
from bs4 import BeautifulSoup
import re 
## get file:url map table
file_url_all = {}
with open('clean_url_java.txt', 'r') as f:
    files = f.read()
    files = files.split('\n')


for f in files:
    # f is 'https://github.com/egametang/ET/archive/refs/heads/master.zip'
    index = f.find('/')
    index = f.find('/',index + 1)
    index = f.find('/',index + 1)
    index = f.find('/',index + 1)
    index1 = f.find('/',index + 1)

    name = f[index + 1: index1]
    url = f[:index1]
    file_url_all[name] = url

all = os.listdir('.')
count = 0
for i in all:
    if os.path.isdir(i):
        if i not in file_url_all.keys():
            os.system('cp -r '+i+' ../Java2')
            os.system('rm -rf '+i)


# print file_url_all
##


## get about and time
def getabout(url):
	
	print(url)
	user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
	headers = { 'User-Agent' : user_agent }
	r = requests.get(url=url, headers=headers)
	contents = r.content
	#print(contents)
	print("contents 'About' get!")
	soup = BeautifulSoup(contents,"html.parser")
	g_about = str(soup.find('p', class_='f4 mt-3'))
	g_time = str(soup.find('relative-time', class_='no-wrap'))
	pattern = re.compile(r'<[^>]+>', re.S)
	pattern2 = re.compile(r'datetime="(.*?)T')
	g_about = pattern.sub('', g_about).strip().replace("\n","")
	g_time = re.findall(pattern2,g_time)
	return g_about,g_time
## 

##
# 翻译函数，word 需要翻译的内容
def translate(word):
    # 有道词典 api
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
    # 传输的参数，其中 i 为需要翻译的内容
    key = {
        'type': "AUTO",
        'i': word,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "ue": "UTF-8",
        "action": "FY_BY_CLICKBUTTON",
        "typoResult": "true"
    }
    # key 这个字典为发送给有道词典服务器的内容
    response = requests.post(url, data=key)
    # 判断服务器是否相应成功
    if response.status_code == 200:
        # 然后相应的结果
        return json.loads(response.text)['translateResult'][0][0]['tgt']
    else:
        print("有道词典调用失败")
        # 相应失败就返回空
        exit(-1)
        return None
def writeyml(ymldir,name,language,zhabout,time):
    fp = open(ymldir, 'w')
    if time == []:
        time = ['2021-05-21']
    fp.write("name: "+name+"\n")
    fp.write("language: "+language+"\n")     
    fp.write("time: "+time[0]+"\n")
    fp.write("description: \""+zhabout+"\"\n")

    fp.close()
##


dir_all = os.listdir('.')
print dir_all

for dir in dir_all:
    if os.path.isdir(dir) == True:
        url = file_url_all[dir]
        about, time = getabout(url)
        about = translate(about)
        print about
        #exit(-1)
        writeyml('./' + dir + '/desc.yml', dir, 'Java', about, time)
        os.system('cp -r '+dir+' ../Java1')
        os.system('rm -rf ' + dir)
    
