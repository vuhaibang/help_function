# String to time
# https://www.journaldev.com/23365/python-string-to-datetime-strptime

from datetime import datetime
datetime_str = '09/19/18 13:55:26'
type = '%m/%d/%y %H:%M:%S'
datetime_object = datetime.strptime(datetime_str, type)

time_str = '13::55::26'
time_object = datetime.strptime(time_str, '%H::%M::%S').time()

from dateutil.parser import parse
dt = parse("Today is January 1, 2047 at 8:21:00AM", fuzzy=True)

# Time to string
from datetime import datetime
datetime_for_string = datetime(2016,10,1,0,0)
datetime_string_format = '%b %d %Y, %H:%M:%S'
datetime.strftime(datetime_for_string,datetime_string_format)

# Time delta

import dateutil.relativedelta
d = datetime.datetime.strptime("2013-03-31", "%Y-%m-%d")
d2 = d - dateutil.relativedelta.relativedelta(months=1)

from datetime import timedelta
dt_new = dt_pdt + timedelta(hours=3, days=1)



