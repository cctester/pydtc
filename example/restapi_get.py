########### below only needed if pydtc not installed. #################
import sys, os
sys.path.insert(0,
    os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')))
#######################################################################
from pydtc import api_get, api_update

# Fake Online REST API for Testing and Prototyping
# https://jsonplaceholder.typicode.com/

r = api_get('https://jsonplaceholder.typicode.com/todos/1')

print(r.values())

update = api_update('https://jsonplaceholder.typicode.com/todos/1', {'title': 'foo'}, method='patch')

print(update)
