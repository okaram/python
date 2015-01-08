from azure import *
from azure.servicemanagement import *

subscription_id = 'e1b9949f-8fef-4751-8363-7eb960298a63'
certificate_path = '/home/curri/AzureCert.pem'

sms = ServiceManagementService(subscription_id, certificate_path)


result = sms.list_os_images()

print("Name\tLabel\tOS\tCategory\tLocation")
for image in result:
	print(image.name+'\t'+image.label)
