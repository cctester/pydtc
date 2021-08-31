########### below only needed if pydtc not installed. #################
import sys, os
sys.path.insert(0,
    os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')))
#######################################################################
import time, os
from pydtc import timeout, retry, DTCTimeoutException

@retry(DTCTimeoutException, retries=2, delay=2)
@timeout(4.1)
def test(err_within_timerange=False):
    for i in range(10):
        print(f'{i+1} seconds.')
        # print(os.getpid())
        time.sleep(1)
        if err_within_timerange:
            raise DTCTimeoutException(999)

if __name__ == "__main__":
    try:
        test()
    except DTCTimeoutException as e:
        print(e)

    try:
        test(True)
    except DTCTimeoutException as e:
        print(e)