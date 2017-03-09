# basic datetime

import datetime
"""
CurrentDate = datetime.date.today()
print(datetime.date.today())
print(CurrentDate)
print(datetime.date)

print(CurrentDate.year)
print(CurrentDate.month)
print(CurrentDate.day)
"""

# advanced datetime 

import pytz

# all_timezones -> all timezone list. 
for tz in pytz.all_timezones:
	if "Asia/Seoul" in tz:
		print(tz)

# all_timezones_set -> all timezone set.
for tz in pytz.all_timezones_set:
	if "Asia/Seoul" in tz:
		print(tz)

# 국가코드로 국가이름, 타임존 조회
print(pytz.country_names['KR'])
print(pytz.country_timezones('KR'))
print(pytz.country_names['US'])
print(pytz.country_timezones('US'))

# 타임존 으로 하나의 타임존 인스턴스를 생성하는 함수
for tzs in pytz.all_timezones:
	if 'Asia/Seoul' in tzs:
		tzs_seoul = tzs
		break

a = pytz.timezone(tzs_seoul)
print(type(a))
print(a)

# UTC 적용(pytz.UTC)
print(type(pytz.UTC))
print(pytz.UTC.__class__.__class__)
print(pytz.UTC.dst(datetime.datetime.today()))
print(pytz.UTC.localize(datetime.datetime.today()))
print(pytz.UTC.tzname(datetime.datetime.today()))
print(pytz.UTC.utcoffset(datetime.datetime.today()))
print(pytz.UTC.zone)

# more about slideshare.
