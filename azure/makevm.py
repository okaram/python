from azure import *
from azure.servicemanagement import *

subscription_id = 'e1b9949f-8fef-4751-8363-7eb960298a63'
certificate_path = '/home/curri/AzureCert.pem'

sms = ServiceManagementService(subscription_id, certificate_path)

name = 'okaramvm2'
location = 'West US'

# later find out about affinity_group
#sms.create_hosted_service(service_name=name,label=name,location=location)


# Name of an os image as returned by list_os_images

image_name='b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-14_10-amd64-server-20141204-en-us-30GB'
media_link = 'http://portalvhdsw37ybpl14kktk.blob.core.windows.net/vhd-store/'+image_name+'.vhd'

# Destination storage account container/blob where the VM disk
# will be created
#media_link = 'https://okhdinisght.blob.core.windows.net/vhds/myimage1.vhd'

# Linux VM configuration, you can use WindowsConfigurationSet
# for a Windows VM instead
linux_config = LinuxConfigurationSet('myhostname', 'myuser', '1QAZ2wsx!')
linux_config.disable_ssh_password_authentication=False

os_hd = OSVirtualHardDisk(image_name,media_link)

vm1=sms.create_virtual_machine_deployment(service_name=name,
    deployment_name=name,
    deployment_slot='production',
    label=name,
    role_name=name,
    system_config=linux_config,
    os_virtual_hard_disk=os_hd,
    role_size='A0')    
    
