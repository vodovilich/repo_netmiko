from netmiko import ConnectHandler
import getpass

passwd = getpass.getpass('Password: ')

iol_01 = {
        'device_type': 'cisco_ios',
        'host': '192.168.100.6', 
        'username': 'gandalf', 
        'password': passwd }
iol_02 = {
        'device_type': 'cisco_ios',
        'host': '192.168.100.7',
        'username': 'gandalf',
        'password': passwd }

with open('03_commands.txt') as hui:
    cmd_list = hui.read().splitlines()
print(cmd_list)

dev_list = [iol_01, iol_02]

for dev in dev_list:
    net_huinect = ConnectHandler(**dev)
    output = net_huinect.send_config_set(cmd_list)
    print(output)

"""
(netmiko-venv) gandalf@debian11:~/Python/repo_netmiko$ python3 03_devlist_cmdfile.py 
Password: 
['logging buffered 65535', '', 'ip access-list extended ACL-1918', ' permit ip 10.0.0.0 0.255.255.255 any', ' permit ip 172.16.0.0 0.15.255.255 any', ' permit ip 192.168.0.0 0.0.255.255 any']
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
iol-rtr157-02(config)#logging buffered 65535
iol-rtr157-02(config)#
iol-rtr157-02(config)#ip access-list extended ACL-1918
iol-rtr157-02(config-ext-nacl)# permit ip 10.0.0.0 0.255.255.255 any
iol-rtr157-02(config-ext-nacl)# permit ip 172.16.0.0 0.15.255.255 any
iol-rtr157-02(config-ext-nacl)# permit ip 192.168.0.0 0.0.255.255 any
iol-rtr157-02(config-ext-nacl)#end
iol-rtr157-02#
configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
iol-rtr157-01(config)#logging buffered 65535
iol-rtr157-01(config)#
iol-rtr157-01(config)#ip access-list extended ACL-1918
iol-rtr157-01(config-ext-nacl)# permit ip 10.0.0.0 0.255.255.255 any
iol-rtr157-01(config-ext-nacl)# permit ip 172.16.0.0 0.15.255.255 any
iol-rtr157-01(config-ext-nacl)# permit ip 192.168.0.0 0.0.255.255 any
iol-rtr157-01(config-ext-nacl)#end
iol-rtr157-01#
"""


