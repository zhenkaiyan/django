#!/usr/bin/python
#-*- coding:utf-8 -*-
# ScriptName: 2.py
# Create Date: 2015-07-16 14:24
# Modify Date: 2015-07-16 14:24
#***************************************************************#
import urllib2,urllib
import json
import time
import datetime
class ZabbixApi:
    def __init__(self,api_info):
        self.api_info = api_info
        self.header = {"Content-type":"application/json"}
        self.api_data = {
                "jsonrpc": "2.0",
                "method": "",
                "params": "",
                "id": 0,
                }
        self._set_auth()
    def _set_auth(self):
        self.api_data['method'] = 'user.login'
        self.api_data['params'] = {
                'user': self.api_info['user'],
                'password': self.api_info['password']
                }
        response = self._request()
#        print response
        self.api_data['auth'] = response['result']
        self.api_data['id'] = 1

    def _request(self):
        post_data = json.dumps(self.api_data)
        req = urllib2.Request(self.api_info['url'],post_data)
        for k,v in self.header.items():
            req.add_header(k,v)
        try:
            result = urllib2.urlopen(req)
        except urllib2.URLError as e:
            print e.code()
        else:
            response = json.loads(result.read())
            result.close()
            return response
    def get_data(self,method,params):
        self.api_data['method'] = method
        self.api_data['params'] = params
        return self._request()


if __name__ == "__main__":
    api_info = {
            'url': 'http://10.128.250.51/api_jsonrpc.php',
            'user': 'yanzhenkai',
            'password': 'welcome@zabbix'
            }
    zbx = ZabbixApi(api_info)
    #print zbx.get_data('hostgroup.get',{'output':'extend','filter':{'name':["dev.others"]}})
    #print zbx.get_data('hostgroup.get',{'output':'extend'})
    nowTime = datetime.datetime.now()
    endTime = int(time.mktime(datetime.datetime(nowTime.year,nowTime.month,nowTime.day,0,0,0).timetuple()))
    startTime = int(time.mktime(datetime.datetime(nowTime.year,nowTime.month-1,nowTime.day,0,0,0).timetuple()))
    print endTime
    print startTime
    print zbx.get_data('alert.get',{'output':'extend',"time_from":"1436112000"})

