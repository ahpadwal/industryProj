#test file
from netmiko import ConnectHandler
R1 = {  'device_type':'cisco_ios',
	'ip':'192.168.56.104',
	'username':'ashay',
	'password':'Ashay@710'
	}
net_connect = ConnectHandler(**R1)
output = net_connect.send_command("sh int desc")
print output
