import json, urllib2, time, os, sys, string, fileinput, shutil



filename = '/app/LocastService.bak'
if os.path.exists(filename):
    shutil.copyfile('/app/LocastService.bak', '/app/LocastService.py')


shutil.copyfile('/app/LocastService.py', '/app/LocastService.bak')

zipcode = os.getenv('magic' , '00000')
print zipcode

if (zipcode == "00000"):
	print("BYE.  Exiting...")
	exit()

zipReq = urllib2.Request("http://api.zippopotam.us/us/" + zipcode , headers={'Content-Type': 'application/json'})
zipOpn = urllib2.urlopen(zipReq)
zipRes = json.load(zipOpn)
zipOpn.close()


latitude = str("{:.15f}".format(float(zipRes['places'][0]['latitude'])))
latitude = "'" + latitude + "' + '/' +"
print latitude
longitude = str("{:.15f}".format(float(zipRes['places'][0]['longitude'])))
longitude = "'" + longitude + "',"
print longitude

for line in fileinput.input("/app/LocastService.py", inplace=True):
    print line.replace("self.current_location['latitude'] + '/' + " , latitude),
    
for line in fileinput.input("/app/LocastService.py", inplace=True):
    print line.replace("self.current_location['longitude'], " , longitude),

#time.sleep(86400)