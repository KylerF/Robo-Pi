import sqlite3
from gps import *
import time 

# Create and return connection to database
def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn

    except Exception as e:
        print(e)                                                         
        return None

# Insert a new GPS data row
def log_gps(conn, report):
    cur = conn.cursor()

    if report['class'] == 'TPV':
        lat = getattr(report,'lat',None)
        lon = getattr(report,'lon',None)
        tim = getattr(report,'time',None)
        alt = getattr(report,'alt',None) 
        epv = getattr(report,'epv',None)
        ept = getattr(report,'ept',None)
        speed = getattr(report,'speed',None)
        climb = getattr(report,'climb',None)
        
        row = (lat,lon,tim,alt,epv,ept,speed,climb)
        sql = ''' INSERT INTO gps_tpv(lat,lon,time,alt,epv,ept,speed,climb)
                      VALUES(?,?,?,?,?,?,?,?) '''
        
        cur.execute(sql, row)
    
    return cur.lastrowid

# Log GPS data every second
def main():
    conn = create_connection('robo-db')
    gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)

    try:
        while True:
            report = gpsd.next()
            log_gps(conn, report)

            time.sleep(1)
    
    except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
        print("\nExiting.")

if __name__ == "__main__":
    main()
