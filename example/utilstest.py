########### below only needed if pydtc not installed. #################
import sys, os
sys.path.insert(0,
    os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')))
#######################################################################
import time
from pydtc import timeout, retry, TimeoutException

@retry(TimeoutException, retries=2, delay=2)
@timeout(4)
def test(err_within_timerange=False):
    for i in range(10):
        print(f'{i+1} seconds.')
        time.sleep(1)
        if err_within_timerange:
            raise TimeoutException(999)

try:
    test()
except TimeoutException as e:
    print(e)

try:
    test(True)
except TimeoutException as e:
    print(e)