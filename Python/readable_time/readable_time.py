"""
A script that works using divmod instead of percents to convert milliseconds into a readable format, such as 1 minute and 30 seconds.
This script isn't exactly accurate. This is because it goes by 4 weeks being in a month, 30 days making up that month, and 12 months in a year, thus being 48 weeks. Throughout the year, we sometimes have 31 days, and some leap years also apply in February when appropriate, but this is only intended to give you an estimate.
This is useful for things like server uptime, how long a player has survived for, how much time is left, etc.
"""
def ms_to_readable_time(ms):
 ms = int(ms)
 #We know that 1000ms is equivalent to 1sec, so we divide ms by 1000.
 seconds, ms = divmod(ms, 1000)
 #We know that 60sec is equivalent to 1min, so we divide minutes by 60sec.
 minutes, seconds = divmod(seconds, 60)
 #We know that 60min is equivalent to 1hr, so we divide hours by 60min.
 hours, minutes = divmod(minutes, 60)
 #We know that 24hr is equivalent to 1d, so we divide days by 24hr.
 days, hours = divmod(hours, 24)
 #We know that 7d is equivalent to 1w, so we divide weeks by 7d.
 weeks, days = divmod(days, 7)
 #We know that 4w is equivalent to 1mo, so we divide weeks by 1mo.
 months, weeks = divmod(weeks, 4)
 #We know that 12mo is equivalent to 1yr, so we divide months by 1yr.
 years, months = divmod(months, 12)
 #Now for the readable string format. Taking the above concept that ms/1000 is 1 second, times 60 is one minute, times 60 is one hour, times 24 is 24 hours or 1 day, times 7 is 1 week, times 4 is 1 month, and times 12 is 1 year.
 human_readable = ""
 if years > 0:
  human_readable += f"{years} {'year' if years == 1 else 'years'} "
 if months > 0:
  human_readable += f"{months} {'month' if months == 1 else 'months'} "
 if weeks > 0:
  human_readable += f"{weeks} {'week' if weeks == 1 else 'weeks'} "
 if days > 0:
  human_readable += f"{days} {'day' if days == 1 else 'days'} "
 if hours > 0:
  human_readable += f"{hours} {'hour' if hours == 1 else 'hours'} "
 if minutes > 0:
  human_readable += f"{minutes} {'minute' if minutes == 1 else 'minutes'} "
 if seconds > 0:
  human_readable += f"{seconds} {'second' if seconds == 1 else 'seconds'}"
 return human_readable