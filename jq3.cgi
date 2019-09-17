#!/usr/bin/env python3

# https://datatables.net/manual/server-side

import cgi
import cgitb; cgitb.enable()
import sys
import time
import json

def make_name(i):
    return {
        "Name" : f"Name <b>#{i}</b>",
        "URL"  : f"https://www.simson.net/page-{i}",
        "date" : "2019-10-10 10:10:11"
        }

if __name__=="__main__":
    print("Content-type: text/text\r\n\r\n")
    form = cgi.FieldStorage()
    print(form,file=sys.stderr)
    # https://datatables.net/manual/server-side
    ret = {"sEcho" : 1,
               "recordsTotal":1000,
               "recordsFiltered":2,
               "data" : [make_name(i) for i in range(1000)]
               }

    print( json.dumps( ret ) )
    
        
        
    
    
