from netmiko import ConnectHandler

#iol01 configured for frodo_id_rsa.pub

iol_01 = {
        'device_type': 'cisco_ios',
        'host': '192.168.100.7', 
        'username': 'frodo', 
        'use_keys': True,
        'timeout': 15,
        'key_file': '/home/gandalf/.ssh/frodo_id_rsa'}

#'ssh_config_file': '/Users/username/.ssh/ssh_config'

net_connect = ConnectHandler(**iol_01, disabled_algorithms = {'pubkeys': ['rsa-sha2-256', 'rsa-sha2-512']})
output = net_connect.send_command('show ip int br')
print(output)

"""
(netmiko-venv) gandalf@debian11:~/Python/repo_netmiko$ python3 04_netmiko_sshkey.py 
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.7   YES DHCP   up                    up      
Ethernet0/1                unassigned      YES NVRAM  administratively down down    
Ethernet0/2                unassigned      YES NVRAM  administratively down down    
Ethernet0/3                unassigned      YES NVRAM  administratively down down    
Loopback0                  192.168.255.10  YES NVRAM  up                    up    
"""