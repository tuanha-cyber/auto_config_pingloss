from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
from datetime import datetime
#import openpyxl as xl
#from openpyxl.styles import Font

all_devices = []

d = {}
d['host'] = '10.79.19.10'
d['username'] = 'admin'
d['password'] = 'Fiss@1234'
d['device_type'] = 'cisco_ios_telnet'
d['global_delay_factor'] = 2
all_devices.append(d)

for a_device in all_devices:
    net_connect = ConnectHandler(**a_device)
    #output = net_connect.send_command('show ip int brief')
    #print(output)
    all_devices.clear()
    e = {}
    e['host'] = '10.33.230.10'
    e['username'] = 'admin'
    e['password'] = 'Fiss@1234'
    e['device_type'] = 'cisco_ios_telnet'
    e['global_delay_factor'] = 2
    all_devices.append(e)

    for a_device in all_devices:
            try:
                cfg_lines=['int f1','speed 100']
                net_connect = ConnectHandler(**a_device)
                output = net_connect.send_config_set(cfg_lines)
                print(output)
                
            except AuthenticationException:
                print('Authentication failure!')
                continue
            except ConnectionRefusedError:
                print('Connection refused error!')
                continue
            except NetMikoTimeoutException:
                print('Timeout to device ...')
                continue
            except Exception as unknown_error:
                print(f'Some other error: {str(unknown_error)}')
                continue
        

        
###    
