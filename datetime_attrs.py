# Import datetime from the datetime module
from datetime import datetime

# Compute the local datetime: local_dt
this_date = datetime.now()

# attributes of datetime
# _______	Date attributes _____#
this_year = this_date.year
this_month = this_date.month
this_day = this_date.day

print(this_year,this_month,this_day)
# _______	Time attributes _____#

this_hour = this_date.hour
this_minute = this_date.minute
this_second = this_date.second
this_microsecond = this_date.microsecond
this_tzinfo = this_date.tzinfo

print(this_hour,this_minute,this_second,this_microsecond,this_tzinfo)
