from netmiko import ConnectHandler
from getpass import getpass
from netmiko.exceptions import AuthenticationException, SSHException, NetMikoTimeoutException

user = input("Please insert your username: ")
password = getpass("Please insert your password: ")

ciscoRouter = {
    'ip': '192.168.136.15',
    'username': user,
    'password': password,
    'device_type': 'cisco_ios',
}

try:
	c = ConnectHandler(**ciscoRouter)
	output = c.send_command('show run')
	f = open('backup.conf', 'x')
	f.write(output)
	print("Success!")
	f.close()
except (AuthenticationException):
	print("An authentication error has occured while connecting to the device.")
except (NetMikoTimeoutException):
	print("The device timed out while trying to connect.")
except (SSHException):
	print("An error occurred while trying to connect to the device. Is SSH enabled?")

