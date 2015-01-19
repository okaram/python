from azure import *
from azure.servicemanagement import *
from sys import argv
subscription_id = 'e1b9949f-8fef-4751-8363-7eb960298a63'
certificate_path = '/home/curri/AzureCert.pem'

sms = ServiceManagementService(subscription_id, certificate_path)

if len(argv)==2:
	vmname=argv[1]
	servicename=argv[1]
elif len(argv)==3:
	vmname=argv[1]
	servicename=argv[2]
else :
	print("Usage: deletevm vmname [servicename]")
	exit()
	
sms.delete_deployment(servicename,vmname,True)
