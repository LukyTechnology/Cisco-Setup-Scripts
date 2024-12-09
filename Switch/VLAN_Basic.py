import netmiko

ip_address = input('Enter the IP Address of the device: ')
user = input('Enter the username: ')
secret = input('Enter the password: ')

ssh = netmiko.ConnectHandler(
    device_type ='cisco_ios',
    host = ip_address,
    username = user,
    password = secret,
)


# Funkcia na Exit
def ssh_exit():
    ssh.send_command('exit')



ssh.enable()

VStatus = ssh.send_command('show vlan')
print(VStatus)

ssh.config_mode()

ID = input('Enter the VLAN ID: ')
Name = input('Enter the VLAN Name: ')

ssh.send_command('vlan ' + ID)
ssh.send_command('name ' + Name)

ssh_exit()

VStatus = ssh.send_command('do show vlan')
print(VStatus)

ssh.disconnect()