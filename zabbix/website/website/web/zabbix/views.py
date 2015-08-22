from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from django import forms
from getalert import ZabbixApi
import time,datetime
class UserForm(forms.Form):
    username = forms.CharField(label='username',max_length=100)
    password = forms.CharField(label='password',widget=forms.PasswordInput())
# Create your views here.
def index(request):
	#return render_to_response('index.html',{'user':'zabbix','title':'zabbix'})
	if request.method == 'POST':
        	uf = UserForm(request.POST)
       		if uf.is_valid():
		    username = uf.cleaned_data['username']
		    password = uf.cleaned_data['password']
		    user = User.objects.filter(username__exact = username,password__exact = password)
		    if user:
			return render_to_response('dashboard.html',{'username':username})
            	    else:
                	return HttpResponseRedirect('/index.html/')
    	else:
        	uf = UserForm()
   	return render_to_response('index.html',{'uf':uf})
def tool(request):
	return render_to_response('tools.html')
def dash(request):
	return render_to_response('dashboard.html')
def test(request):
	return render_to_response('test.html')
def zb_bak(request):
    api_info = {
            'url': 'http://10.128.250.51/api_jsonrpc.php',
            'user': 'yanzhenkai',
            'password': 'welcome@zabbix'
            }
    zbx = ZabbixApi(api_info)
    nowTime = datetime.datetime.now()
    endTime = time.mktime(datetime.datetime(nowTime.year,nowTime.month,nowTime.day,0,0,0).timetuple())
    startTime = time.mktime(datetime.datetime(nowTime.year,nowTime.month,nowTime.day-1,0,0,0).timetuple())
    result = zbx.get_data('alert.get',{'output':'extend',"time_from":endTime})
    #print len(result["result"])
    data = []
    length = len(result["result"])
    mem_da = load_da = ICMP_da = disk_da = oth_d = 0 
    for i in range(0,length):
        data.append(result["result"][i]["subject"].split(":")[2])
    for i in range(0,length):
        teda = data[i]
        if "Memory" in teda:
            mem_da += 1
        elif "load" in teda:
            load_da += 1
        elif "ICMP" in teda:
            ICMP_da += 1
        elif "disk" or "Disk"in teda:
            disk_da += 1
        else:
            oth_d += 1
    return render_to_response('zabbix.html',{"memory":mem_da,"disk":disk_da,"load":load_da,"PING":ICMP_da})
def zb(request):
    mem_da = 23
    disk_da = 168
    load_da = 58
    ICMP_da = 40
    return render_to_response('zabbix.html',{"memory":mem_da,"disk":disk_da,"load":load_da,"PING":ICMP_da})
