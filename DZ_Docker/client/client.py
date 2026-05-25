import urllib.request
import time

time.sleep(5)

while True:
	try:
    		response = urllib.request.urlopen("http://app:5000/")
    		print("Status:", response.getcode(), flush=True)
    		time.sleep(5)
	except Exception as e:
		print("Server is not ready yet", flush=True)
	time.sleep(5)
