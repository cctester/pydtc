########### below only needed if pyw not installed. #################
import sys, os
sys.path.insert(0,
    os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..')))
#####################################################################
import pyw

conn = pyw.connect('mysql', '127.0.0.1', 'cc', 'carl', database='databox')
conn.close()