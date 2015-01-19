from azure import *
from azure.servicemanagement import *
from sys import argv

if len(argv)==2:
	name=argv[1]
else :
	print("Usage: deletevm vmname [servicename]")
	exit()
	
subscription_id = 'e1b9949f-8fef-4751-8363-7eb960298a63'
certificate_path = '/home/curri/AzureCert.pem'

sms = ServiceManagementService(subscription_id, certificate_path)

location = 'West US'

# later find out about affinity_group

if(sms.check_hosted_service_name_availability(name).result):
	sms.create_hosted_service(service_name=name,label=name,location=location)


# Name of an os image as returned by list_os_images

image_name='b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-14_10-amd64-server-20141204-en-us-30GB'
#media_link = 'http://okhdinisght.blob.core.windows.net/vhd-store/'+image_name+'.vhd'

media_link = 'http://okhdinisght.blob.core.windows.net/vhds/'+name+'.vhd'

# Destination storage account container/blob where the VM disk
# will be created
#media_link = 'https://okhdinisght.blob.core.windows.net/vhds/myimage1.vhd'

# Linux VM configuration, you can use WindowsConfigurationSet
# for a Windows VM instead
linux_config = LinuxConfigurationSet('myhostname', 'myuser', '1QAZ2wsx!')
linux_config.disable_ssh_password_authentication=False

os_hd = OSVirtualHardDisk(image_name,media_link)


endpoint_config = ConfigurationSet()
endpoint_config.configuration_set_type = 'NetworkConfiguration'

endpoint1 = ConfigurationSetInputEndpoint(name = 'ssh', protocol = 'tcp', port = '22', local_port = '22', load_balanced_endpoint_set_name = None, enable_direct_server_return = False)

#endpoints must be specified as elements in a list

endpoint_config.input_endpoints.input_endpoints.append(endpoint1)


vm1=sms.create_virtual_machine_deployment(service_name=name,
    deployment_name=name,
    deployment_slot='production',
    label=name,
    role_name=name,
    system_config=linux_config,
    network_config = endpoint_config,
    os_virtual_hard_disk=os_hd,
    role_size='Basic_A0')    
    
