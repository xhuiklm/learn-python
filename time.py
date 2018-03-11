import time
localtime= time.localtime(time.time())
localtime2=time.asctime(localtime)
print(localtime2)
print(localtime)
#Tue Feb  6 07:43:30 2018
#time.struct_time(tm_year=2018, tm_mon=2, tm_mday=6, tm_hour=7, tm_min=43, tm_sec=30, tm_wday=1, tm_yday=37, tm_isdst=0)