# -*- coding: utf-8 -*-
import os
import zipfile


def getdir(path):
    dirpath = []
    for category in os.listdir(path):
    #判断是否是文件
        if os.path.isdir(os.path.join(path,category))==True:
        #设置新文件名
            dirpath.append(os.path.join(path,category))
    return dirpath

def getzipdir(file_dir):
    L=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[0][0] != '.':
                if os.path.splitext(file)[1] == '.zip':
                    L.append(os.path.join(root, file))
    return L

def zipindirname(file_dir):
    print file_dir
    zf = zipfile.ZipFile(file_dir)
    name=zf.namelist()[0].rsplit("-",1)[0]
    zf.close()
    return name

def changename(updir, name):
    if os.path.isdir(updir) == True:
        for category in os.listdir(updir):
            if os.path.isfile(os.path.join(path,category))==True:
                if os.path.splitext(os.path.join(path,category))[1] == '.zip':
                    os.rename(os.path.join(path,category),os.path.join(path,name+'.zip'))

def changezipname(zipdir, newname):
    os.rename(zipdir,os.path.join(os.path.dirname(zipdir),newname+'.zip'))

if __name__ == '__main__':
    path = os.getcwd()
    print("current dir:",path)
    dirpath = getdir(path)
    #print("dirlist:",dirpath)
    zipdir = []
    for p in dirpath:
        zipdir.append(getzipdir(p))
    #print("zippath:",zipdir)
    fatherlist = []
    newfalist = []
    print(zipdir)
    for zp in zipdir:
        try:
            zp = zp[0]
        except Exception as e:
            print(e)
            print("zp is ")
            print(zp)
        try:
            zipname = zipindirname(zp)
        except:
            name = zp.split('/')
            print name
            name = './' + name[-2] 
            os.system('rm -rf ' + name)
            continue
        changezipname(zp, zipname)
        fathername = os.path.dirname(zp)
        fathernamenew = os.path.join(os.path.dirname(os.path.dirname(zp)),zipname)
        try:
            os.rename(fathername,fathernamenew)
        except Exception as e:
            print(e)
            print('rename dir fail!'+fathername+"->"+fathernamenew+"\r\n")
            pass
        else:
            print('rename dir success!'+fathername+"->"+fathernamenew+"\r\n")
    print("success!")

    all = os.listdir('.')
    count = 0
    for i in all:
        
        if os.path.isdir(i):
            all2 = os.listdir('./'+i)
            if i+'.zip' not in all2:
                print i
                print all2
                count+=1
                os.system('cp -r '+i+' '+'../Java2')
                os.system('rm -rf '+i)
    print count


