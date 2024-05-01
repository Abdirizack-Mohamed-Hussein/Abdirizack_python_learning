from datetime import datetime
today=datetime.now()
dob = (input("Enter the date of birth(dd/mm/yy): "))
split_dob=dob.split("/")
year_dob=int(split_dob[2])
month_dob=int(split_dob[1])
date_dob=int(split_dob[0])

int_dob=datetime(day=date_dob,month=month_dob,year=year_dob)
age=today-int_dob
years=age.days//365
months=age.days%365//31
days=age.days%365%31
print(years,months,days)