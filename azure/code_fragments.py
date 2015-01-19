d1=[ d for d in sms.list_disks() if d.attached_to and d.attached_to.role_name=='okaramvm7']
a=sms.get_disk(d1[0].name)

