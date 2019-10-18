########### below only needed if pydtc not installed. #################
import sys, os
sys.path.insert(0,
    os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')))
#######################################################################
import requests
from pydtc import HttpFormAuth

r = requests.get('https://www.example.com/private_page.html', auth=HttpFormAuth('user','pass'))

print(r.status_code)
