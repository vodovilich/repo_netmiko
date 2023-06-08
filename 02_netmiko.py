from netmiko import ConnectHandler
net_connect = ConnectHandler(device_type='cisco_ios',
                             host = '192.168.100.13',
                             username = 'gandalf',
                             password = 'grey')
output = net_connect.send_config_set(['logging buffered 20000'])
print(output)
