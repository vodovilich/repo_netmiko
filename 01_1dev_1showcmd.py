from netmiko import ConnectHandler
iol_01 = {
        'device_type': 'cisco_ios',
        'host': '192.168.100.8', 
        'username': 'gandalf', 
        'password': 'grey'}
iol_02 = {
        'device_type': 'cisco_ios',
        'host': '192.168.100.9',
        'username': 'gandalf',
        'password': 'grey'}

net_connect = ConnectHandler(**iol_01)
#print(net_connect.find_prompt())

output = net_connect.send_command('show ip int br')
print(output)

