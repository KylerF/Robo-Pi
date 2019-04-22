#! /usr/bin/python
 
from gps import *
import time

gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE) 

def get_gps():
    report = gpsd.next()

    return report

print('latitude\tlongitude\ttime utc\t\t\taltitude\tepv\tept\tspeed\tclimb') # '\t' = TAB to try and output the data in columns.


try:
    while True:
        report = get_gps()
        
        if report['class'] == 'TPV':
            lat = getattr(report,'lat',0.0)
            lon = getattr(report,'lon',0.0)
            tim = getattr(report,'time','')
            alt = getattr(report,'alt',0.0) 
            epv = getattr(report,'epv',0.0)
            ept = getattr(report,'ept',0.0)
            speed = getattr(report,'speed',0.0)
            climb = getattr(report,'climb',0.0)
        
            print(lat, '\t', lon, '\t', tim, '\t\t\t', alt, '\t', epv, '\t', ept, '\t', speed, '\t', climb)
           
        time.sleep(1) 

except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print("Done.\nExiting.")
