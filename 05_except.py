from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException
from netmiko.exceptions import AuthenticationException
from netmiko.exceptions import SSHException


import yaml

SSH_FILE = '05_secret.yml'

with open(SSH_FILE, 'r') as s:
    sfile = yaml.safe_load(s)
    ssh_user = sfile['SSH_USERNAME']
    ssh_key = sfile['SSH_CONFIG']

DEVLIST_FILE = '05_devlist.yml'

def main():
    with open(DEVLIST_FILE, 'r') as f:
        for ip in yaml.safe_load(f):

            iol_rtr = {
                    'device_type': 'cisco_ios',
                    'host': ip, 
                    'username': 'gandalf', 
                    'use_keys': True,
                    'timeout': 15,
                    'key_file': '/home/gandalf/.ssh/id_rsa'}

    #'ssh_config_file': '/Users/username/.ssh/ssh_config'
            print(f"\n\nConnecting to {ip}...\n")
            try:
                net_connect = ConnectHandler(**iol_rtr, disabled_algorithms = {'pubkeys': ['rsa-sha2-256', 'rsa-sha2-512']})
                output = net_connect.send_command('show ip int br')
                print(output)
            except (NetmikoTimeoutException, AuthenticationException):
               print (f"Connection to {ip} failed with TIMEOUT" )

if __name__ == "__main__":
    main()