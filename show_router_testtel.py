from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
from datetime import datetime
#import openpyxl as xl
#from openpyxl.styles import Font

all_devices = []

d = {}
d['host'] = '10.64.74.10'
#d['host'] = '10.79.19.10'
d['username'] = 'admin'
d['password'] = 'Fiss@1234'
d['device_type'] = 'cisco_ios_telnet'
d['global_delay_factor'] = 2
all_devices.append(d)

for a_device in all_devices:
    try:
        commandL='sh inventory | inc PID'
        net_connect = ConnectHandler(**a_device)
        output = net_connect.send_command(commandL)
        n= output.find("C1111")
        if n>0 :
            print(output)
        else :
            print("Router C881G")
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
