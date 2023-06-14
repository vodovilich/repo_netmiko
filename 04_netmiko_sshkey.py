from netmiko import ConnectHandler

#iol01 configured for frodo_id_rsa.pub

iol_01 = {
        'device_type': 'cisco_ios',
        'host': '192.168.100.13', 
        'username': 'frodo', 
        'use_keys': True,
        'timeout': 15,
        'key_file': '/home/gandalf/.ssh/frodo_rsa'}

#'ssh_config_file': '/Users/username/.ssh/ssh_config'

net_connect = ConnectHandler(**iol_01, disabled_algorithms = {'pubkeys': ['rsa-sha2-256', 'rsa-sha2-512']})
output = net_connect.send_command('show ip int br')
print(output)
