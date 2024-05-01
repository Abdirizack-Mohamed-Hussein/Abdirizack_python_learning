# TASK 15: Using Python 
# Write a program that takes input of someone's basic salary and benefits, 
# adds them to find the gross salary then uses  the gross salary to find the NHIF. 
# To find the Kenya NHIF Rate using THIS LINK:  

# variables
basic_salary=float(input("Enter your basic salary: "))
benefits=float(input("Enter your benefits: "))

gross_salary=basic_salary + benefits

if gross_salary<=5999:
    nhf=150
elif gross_salary>=6000 and gross_salary<=7999:
    nhf=300
elif gross_salary>=8000  and gross_salary<=11999:
    nhf=400
elif gross_salary>=12000  and gross_salary<=14999:
    nhf=500
elif gross_salary>=15000  and gross_salary<=19999:
    nhf=600
elif gross_salary>=20000  and gross_salary<=24999:
    nhf=750
elif gross_salary>=25000  and gross_salary<=29999:
    nhf=850
elif gross_salary>=30000  and gross_salary<=34999:
    nhf=900
elif gross_salary>=35000  and gross_salary<=39999:
    nhf=950
elif gross_salary>=40000  and gross_salary<=44999:
    nhf=1,000
elif gross_salary>=45000  and gross_salary<=49999:
    nhf=1,100
elif gross_salary>=50000  and gross_salary<=59999:
    nhf=1,200
elif gross_salary>=60000  and gross_salary<=69999:
    nhf=1,300
elif gross_salary>=70000  and gross_salary<=79999:
    nhf=1,400
elif gross_salary>=80000  and gross_salary<=89999:
    nhf=1,500
elif gross_salary>=90000  and gross_salary<=99999:
    nhf=1,600
else:
    nhf=1700
# print(nhf)

# TASK 16: Using Python 
# Continue with the program above, then use  the gross salary to find the NSSF. 
# To find the Kenya NSSF Rate using. Compute NSSF using 6% of the Gross Salary. 
# BUT ONLY A MAXIMUM OF 18,000 CAN BE USED IN NSSF. 

# variables

if gross_salary<=18000:
    NSSF=0.06*gross_salary
else:
    NSSF=18000*0.06
# print(NSSF)

# Task 17: Using Python
# Continue with the same program and calculate an individual’s NHDF using:
#  i.e NHDF = gross_salary *  0.015
if gross_salary<=5999:
    NHDF = gross_salary *  0.015
elif gross_salary>=6000 and gross_salary<=7999:
    NHDF = gross_salary *  0.015
elif gross_salary>=8000  and gross_salary<=11999:
   NHDF = gross_salary *  0.015
elif gross_salary>=12000  and gross_salary<=14999:
    NHDF = gross_salary *  0.015
elif gross_salary>=15000  and gross_salary<=19999:
    NHDF = gross_salary *  0.015
elif gross_salary>=20000  and gross_salary<=24999:
    NHDF = gross_salary *  0.015
elif gross_salary>=25000  and gross_salary<=29999:
   NHDF = gross_salary *  0.015
elif gross_salary>=30000  and gross_salary<=34999:
   NHDF = gross_salary *  0.015
elif gross_salary>=35000  and gross_salary<=39999:
    NHDF = gross_salary *  0.015
elif gross_salary>=40000  and gross_salary<=44999:
    NHDF = gross_salary *  0.015
elif gross_salary>=45000  and gross_salary<=49999:
    NHDF = gross_salary *  0.015
elif gross_salary>=50000  and gross_salary<=59999:
    NHDF = gross_salary *  0.015
elif gross_salary>=60000  and gross_salary<=69999:
    NHDF = gross_salary *  0.015
elif gross_salary>=70000  and gross_salary<=79999:
   NHDF = gross_salary *  0.015
elif gross_salary>=80000  and gross_salary<=89999:
    NHDF = gross_salary *  0.015
elif gross_salary>=90000  and gross_salary<=99999:
    NHDF = gross_salary *  0.015
else:
    NHDF = gross_salary *  0.015
# print(NHDF)


# Task 18: Using Python
# Calculate the taxable income.
# i.e taxable_income = gross_salary - (NSSF + NHDF) 

if gross_salary<=5999:
    taxable_income = gross_salary - (NSSF + NHDF)
elif gross_salary>=6000 and gross_salary<=7999:
    taxable_income = gross_salary - (NSSF + NHDF)
elif gross_salary>=8000  and gross_salary<=11999:
   taxable_income = gross_salary - (NSSF + NHDF)
elif gross_salary>=12000  and gross_salary<=14999:
    taxable_income = gross_salary - (NSSF + NHDF)
elif gross_salary>=15000  and gross_salary<=19999:
    taxable_income = gross_salary - (NSSF + NHDF)
elif gross_salary>=20000  and gross_salary<=24999:
   taxable_income = gross_salary - (NSSF + NHDF)
elif gross_salary>=25000  and gross_salary<=29999:
   taxable_income = gross_salary - (NSSF + NHDF)
elif gross_salary>=30000  and gross_salary<=34999:
   taxable_income = gross_salary - (NSSF + NHDF)
elif gross_salary>=35000  and gross_salary<=39999:
   taxable_income = gross_salary - (NSSF + NHDF)
elif gross_salary>=40000  and gross_salary<=44999:
    taxable_income = gross_salary - (NSSF + NHDF)
elif gross_salary>=45000  and gross_salary<=49999:
    taxable_income = gross_salary - (NSSF + NHDF)
elif gross_salary>=50000  and gross_salary<=59999:
    taxable_income = gross_salary - (NSSF + NHDF)
elif gross_salary>=60000  and gross_salary<=69999:
    taxable_income = gross_salary - (NSSF + NHDF)
elif gross_salary>=70000  and gross_salary<=79999:
   taxable_income = gross_salary - (NSSF + NHDF)
elif gross_salary>=80000  and gross_salary<=89999:
    taxable_income = gross_salary - (NSSF + NHDF)
elif gross_salary>=90000  and gross_salary<=99999:
    taxable_income = gross_salary - (NSSF + NHDF)
else:
    taxable_income = gross_salary - (NSSF + NHDF)
# print(taxable_income)


# TASK 19: Using Python 
# Continue with the same program and find the person's PAYEE using the taxable income above.
r=2400
if taxable_income>=0 and taxable_income<=24000:
    PAYEE=0
elif taxable_income>24000 and taxable_income<=32333:
    PAYEE=(24000*0.1) +(0.25*(taxable_income-24000))-r

elif taxable_income>32333 and taxable_income<=500000:
  PAYEE=(24000*0.1) +(0.25*8333)+(0.3*(taxable_income-32333))-r

elif taxable_income>500000 and taxable_income<=800000:
    PAYEE=(24000*0.1) +(0.25*8333) +(0.325*(taxable_income-500000))-r


else:
    # taxable_income<=800000 and taxable_income>=1600000
    PAYEE=PAYEE=(24000*0.1) +(0.25*8333) +(0.35*(taxable_income-800000))-r
# print(PAYEE)



# Task 20: Using Python
# Continue with the same program and calculate an individual’s Net Salary using:
#  net_salary = gross_salary - (nhif + nhdf +  nssf + payee)

net_salary = gross_salary - (nhf + NHDF +  NSSF + PAYEE)
print(net_salary)