import urllib.request
import os
import socket
socket.setdefaulttimeout(5.0)
import json

if __name__ == '__main__':
    #urllib.request.urlretrieve('https://addons.opera.com/extensions/download/2048-sidebar/', filename='./123.crx')
        url_list = open('../recommanded100_url.txt')
        readlines = url_list.readlines()
        for line in readlines:
            filename = line.split('/')[-1][:-1]
            filepath = './addons/' + filename
            if filename not in os.listdir('./addons/'):
                try:
                    urllib.request.urlretrieve(line, filename=filepath)
                    print('try')
                except Exception as e:
                    print(e)
                    print("something wrong")
            else:
                print('already in')
