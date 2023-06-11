from netmiko import ConnectHandler
import getpass

passwd = getpass.getpass('Password: ')

iol_01 = {
        'device_type': 'cisco_ios',
        'host': '192.168.100.13', 
        'username': 'gandalf', 
        'password': passwd }
iol_02 = {
        'device_type': 'cisco_ios',
        'host': '192.168.100.12',
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




