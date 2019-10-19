########### below only needed if pydtc not installed. #################
import sys, os
sys.path.insert(0,
    os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')))
#######################################################################
import pydtc

conn = pydtc.connect('mysql', '127.0.0.1', 'user', 'pass', database='default', serverTimezone='UTC')
df = conn.read_sql('select * from tbl')
conn.close()