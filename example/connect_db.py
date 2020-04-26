########### below only needed if pydtc not installed. #################
import sys, os
sys.path.insert(0,
    os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')))
#######################################################################
import pydtc

conn = pydtc.connect('mysql', 'localhost', 'user', 'pass', options="/mysql?serverTimezone='UTC'")
df = conn.read_sql('select * from column_stats')
print(df[:2].to_string())
conn.close()