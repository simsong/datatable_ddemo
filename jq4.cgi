#!/usr/bin/env python3

# https://datatables.net/manual/server-side

import cgi
import cgitb; cgitb.enable()
import sys
import time
import json

def make_ch(ch):
    return {
        "Name" : f"Search character <b>#{ch}</b>",
        "URL"  : f"https://www.simson.net/page-{ch}",
        "date" : "2019-10-10 10:10:11"
        }

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
    try:
        search = form['search[value]'].value
    except KeyError:
        search = 'A'

    ret = {"recordsTotal":1000,
               "recordsFiltered":2,
               #"data" : [make_name(i) for i in range(len(search))]
               "data" : [make_ch(ch) for ch in search]
               }

    print( json.dumps( ret ) )
    
        
        
    
    
