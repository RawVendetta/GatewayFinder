import os
banner = print('''
                888                                         
                888                                         
                888                                         
 .d88b.  8888b. 888888 .d88b. 888  888  888 8888b. 888  888 
d88P"88b    "88b888   d8P  Y8b888  888  888    "88b888  888 
888  888.d888888888   88888888888  888  888.d888888888  888 
Y88b 888888  888Y88b. Y8b.    Y88b 888 d88P888  888Y88b 888 
 "Y88888"Y888888 "Y888 "Y8888  "Y8888888P" "Y888888 "Y88888 
     888                                                888 
Y8b d88P                 [IP FINDER]V.1.1          Y8b d88P 
 "Y88P"                                             "Y88P"  
''')
#get gateway
getipr = os.popen('ip r')
getopt = [getipr.read()]
#global vars
creds1 = 'admin:password'
creds2 = 'admin:admin'
creds3 = 'N/A:N/A'
creds4 = 'root:!root'
creds5 = 'N/A:admin'
creds6 = 'N/A:public'
creds7 = 'Admin:1988'
creds8 = 'root:default'
creds9 = 'admin:1234'
creds10 = 'N/A:connect'
creds11 = 'admin:firetide'

def grabimports():
	os.system('pip3 install webbrowser')
def browser():
	import webbrowser
	option = int(input('[1]OpenInBrowser [2]Quit\nChoice:'))
	if option == 1:
		webbrowser.open('http://' + ip)
grabimports	
for ipaddr in getopt:
	if '192.168.1.1' in getopt[0]:
		ip = '192.168.1.1'
		print('Your gateway is:\n192.168.1.1')
		print('Possible creds:\n' + creds1 + '\n' + creds2 + '\n' + creds5 + '\n' + creds8 + '\n----------------')
		browser()
	elif '192.168.0.1' in getopt[0]:
		ip = '192.168.0.1'
		print('Your gateway is:192.168.0.1')
		print('Possible creds:\n' + creds1 + '\n' + creds2 + + '\n' + creds5  +'\n----------------')
		browser()
	elif '192.168.2.1' in getopt[0]:
		ip = '192.168.2.1'
		print('Your gateway is:\n192.168.2.1')
		print('Possible creds:\n' + creds1 + '\n' + creds2 + '\n' + creds9 + '\n----------------')
		browser()
	elif '192.168.1.254' in getopt[0]:
		ip = '192.168.1.254'
		print('Your gateway is:\n192.168.1.254')
		print('Possible creds:\n' + creds3 + '\n' + creds10 + '\n----------------')
		browser()
	elif '192.168.200.254' in getopt[0]:
		ip = '192.168.200.254'
		print('Your gateway is:\n192.168.200.254')
		print('Possible creds:\n' + creds4 + '\n----------------')
		browser()
	elif '192.168.1.250' in getopt[0]:
		ip = '192.168.1.250'
		print('Your gateway is:\n192.168.200.250')
		print('Possible creds:\n' + creds5 + '\n----------------')
		browser()
	elif '192.168.98.11' in getopt[0]:
		ip = '192.168.98.11'
		print('Your gateway is:192.168.98.11')
		print('Possible creds:\n' + creds6 + '\n----------------')
		browser()
	elif '192.168.2.1' in getopt[0]:
		ip = '192.168.2.1'
		print('Your gateway is:192.168.2.1')
		print('Possible creds:\n' + creds3 + '\n----------------')
		browser()
	elif '192.168.1.240' in getopt[0]:
		ip = '192.168.1.240'
		print('Your gateway is:192.168.1.240')
		print('Possible creds:\n' + creds7 + '\n----------------')
		browser()
	elif '192.168.224.160' in getopt[0]:
		ip = '192.168.224.160'
		print('Your gateway is:192.168.224.160')
		print('Possible creds:\n' + creds7 + '\n----------------')
		browser()
	else:
		print('Gateway not found')
