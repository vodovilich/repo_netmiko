from netmiko import ConnectHandler
net_connect = ConnectHandler(device_type='cisco_ios',
                             host = '192.168.100.6',
                             username = 'gandalf',
                             password = 'grey')
output = net_connect.send_config_set(['logging buffered 20000'])
print(output)

"""
(netmiko-venv) gandalf@debian11:~/Python/repo_netmiko$ python3 02_1dev_1confcmd.py 
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
iol-rtr157-02(config)#logging buffered 20000
iol-rtr157-02(config)#end
iol-rtr157-02#
"""