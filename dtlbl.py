#date checker
#date format checker second solution
import time
import datetime
import numpy
import pandas as pd
import csv
import re

outPutDateFormat = "%d/%m/%Y"
datesample = pd.read_csv('set2.csv')
dateslist = datesample["words"].values.astype(str).tolist()
    


def check_format(datec):    
    format_ok = False
    for mask in ['%Y%m%d','%Y-%m-%d','%d-%m-%Y','%m%d%Y','%A, %d, %B, %y','%d%m/%Y','%d%m-%Y','%Y/%m/%d','%m/%d/%Y','%d/%m/%Y','%d/%m/%y','%m/%d/%y','%m-%d-%y','%m-%d-%Y','%d-%m-%y','%d-%m-%y']:
        try:
            time.strptime(datec, mask)
            format_ok = True
            break
        except ValueError:
            pass
    if format_ok:
        date0=datetime.datetime.strptime(datec ,mask)
        date1=datetime.date.strftime(date0, outPutDateFormat)
        return date1
    else:
        return "incorrect date format" 
    return None
 
def main():
    RE = r"(\d{1,2})(\/)*(\d{1,2})(\/)*(\d{2,4})"
    f = open('datecorrections.csv', 'w')
    datelist=[]
    List_RE=['RE']
    for date in dateslist:       
        for pattern in List_RE:
            regex = re.compile(eval(pattern))
            m = regex.finditer(date)
            if m :
                for m1 in m:
                    datelist.append(m1.group(0))
    #print(datelist)
    f = open('datecorrections.csv', 'w')
    for date in datelist:
        wf = csv.writer(f)
        wf.writerow([date,check_format(date)])
        

if __name__=="__main__":
    main()
    
  
  
#label checker
import pandas as pd
import csv

#reading the data
categories=['B-fromloc.station_code','O','B-toloc.station_code','B-fromloc.station_name','I-fromloc.station_name','B-toloc.station_name','I-toloc.station_name','B-fromloc.city_name','I-fromloc.city_name','B-toloc.city_name','I-toloc.city_name','B-class_type','I-class_type','B-quota_type','I-quota_type','B-depart_date','B-return_date','B-round_trip','I-round_trip']
datesample = pd.read_csv('set2.csv')
dateslist = datesample["labels"].values.astype(str).tolist()

#lgc
def returnMatches(a,b):
    if a in b:
        return a
    else:
        return "No match"
f = open('datecorrections.csv', 'w')
for date in dateslist:
    wf = csv.writer(f)
    wf.writerow([date,returnMatches(date,categories)])

#if __name__=="__main__":
#returnMatches(categories,dateslist)
