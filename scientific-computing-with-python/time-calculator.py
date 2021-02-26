def add_time(start, duration, day=None):
  days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
  if day is not None: # if day of the week is passed as an argument
    day = day[:1].upper() + day[1:].lower() # ensure day is properly capitalized
    dindex = days.index(day) # day index
  dlater = 0 # days later
  scol = len(start) - 6 # start colon
  dcol = len(duration) - 3 # duration colon
  shrs = int(start[:scol]) # start hours
  smins = int(start[scol + 1:scol + 3]) # start minutes
  period = start[scol + 3:] # AM or PM
  dhrs = int(duration[:dcol]) # duration hours
  dmins = int(duration[dcol + 1:dcol + 3]) # duration minutes
  if period == ' PM': # if start time is after noon
    shrs += 12 # convert start hours to 24 hour format
  thrs = shrs + dhrs # total hours
  tmins = smins + dmins # total minutes
  while tmins >= 60: # while total minutes is greater than 60
    tmins -= 60 # reduce total minutes by 60
    thrs += 1 # add 1 to total hours
  while thrs >= 24: # if total hours is greater than 60
    thrs -= 24 # reduce total hours by 24
    dlater += 1 # increase days later by 1
    if day is not None: # if day of the week has been passed as an argument
      dindex += 1 # increase day index by 1
  if day is not None: # if day of the week has been passed as an argument
    while dindex > 6: # while day index is greater than 6
      dindex -= 7 # reduce day index by 7
  if thrs >= 12 and thrs < 24: # convert total hours back to 12 hour time
    if thrs > 12: # if total hours is greater than 12
      thrs -= 12 # reduce total hours by 12
    period = ' PM' # set period to PM
  else: # if total hours is less than 12
    if thrs == 0: # if total hours is 0
      thrs += 12 # increase total hours by 12
    period = ' AM' # set period to AM
  thrs = str(thrs) # convert total hours to a string
  tmins = str(tmins) # convert total minutes to a string
  if len(tmins) < 2: # if total minutes is a single digit
    tmins = '0' + tmins # add a leading 0 to total minutes
  ntime = thrs + ':' + tmins + period # new time
  if day is not None: # if day of the week is passed as an argument
    ntime += ', ' + days[dindex] # new time
  if dlater == 1: # if days later is 1
    ntime += ' (next day)' # add ' (next day)' to new time
  elif dlater > 1: # if days later is greater than 1
    ntime += f' ({dlater} days later)' # add ' (n days later)' to new time
  return ntime

print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM
 
print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday
 
print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM
 
print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)
 
print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)
 
print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)
