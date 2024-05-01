#TASK 15
basic_salary = float(input("Enter your basic salary: "))
benefits = float(input("Enter your benefits: "))
gross_salary = basic_salary + benefits

def calculate_nhif(gross_salary):
    if gross_salary <= 5999:
        nhf = 150
    elif 6000 <= gross_salary <= 7999:
        nhf = 300
    elif 8000 <= gross_salary <= 11999:
        nhf = 400
    elif 12000 <= gross_salary <= 14999:
        nhf = 500
    elif 15000 <= gross_salary <= 19999:
        nhf = 600
    elif 20000 <= gross_salary <= 24999:
        nhf = 750
    elif 25000 <= gross_salary <= 29999:
        nhf = 850
    elif 30000 <= gross_salary <= 34999:
        nhf = 900
    elif 35000 <= gross_salary <= 39999:
        nhf = 950
    elif 40000 <= gross_salary <= 44999:
        nhf = 1000
    elif 45000 <= gross_salary <= 49999:
        nhf = 1100
    elif 50000 <= gross_salary <= 59999:
        nhf = 1200
    elif 60000 <= gross_salary <= 69999:
        nhf = 1300
    elif 70000 <= gross_salary <= 79999:
        nhf = 1400
    elif 80000 <= gross_salary <= 89999:
        nhf = 1500
    elif 90000 <= gross_salary <= 99999:
        nhf = 1600
    else:
        nhf = 1700
    return nhf

nhif = calculate_nhif(gross_salary)

print("Gross Salary:", gross_salary)
print("NHIF:", nhif)

#TASK 16
def calculate_nssf(gross_salary): #.....def calculate_nssf(gross_salary,rate=0.06) default parameter
    if gross_salary <= 18000:
        nssf = 0.06 * gross_salary
    else:
        nssf=1080   #NSSF=0.06*18000
    return nssf

nssf = calculate_nssf(gross_salary)

print("Gross Salary:", gross_salary)
print("NSSF:", nssf)

#TASK 17
def calculate_NHDF(gross_salary):    #def calculate_NHDF(gross_salary,rate=0.015): default parameter
    if gross_salary <= 5999:
        NHDF = gross_salary * 0.015
    elif 6000 <= gross_salary <= 7999:
        NHDF = gross_salary * 0.015
    elif 8000 <= gross_salary <= 11999:
        NHDF = gross_salary * 0.015
    elif 12000 <= gross_salary <= 14999:
        NHDF = gross_salary * 0.015
    elif 15000 <= gross_salary <= 19999:
        NHDF = gross_salary * 0.015
    elif 20000 <= gross_salary <= 24999:
        NHDF = gross_salary * 0.015
    elif 25000 <= gross_salary <= 29999:
        NHDF = gross_salary * 0.015
    elif 30000 <= gross_salary <= 34999:
        NHDF = gross_salary * 0.015
    elif 35000 <= gross_salary <= 39999:
        NHDF = gross_salary * 0.015
    elif 40000 <= gross_salary <= 44999:
        NHDF = gross_salary * 0.015
    elif 45000 <= gross_salary <= 49999:
        NHDF = gross_salary * 0.015
    elif 50000 <= gross_salary <= 59999:
        NHDF = gross_salary * 0.015
    elif 60000 <= gross_salary <= 69999:
        NHDF = gross_salary * 0.015
    elif 70000 <= gross_salary <= 79999:
        NHDF = gross_salary * 0.015
    elif 80000 <= gross_salary <= 89999:
        NHDF = gross_salary * 0.015
    elif 90000 <= gross_salary <= 99999:
        NHDF = gross_salary * 0.015
    else:
        NHDF = gross_salary * 0.015
    return NHDF

NHDF = calculate_NHDF(gross_salary)
print(NHDF)

#TASK 18
def calculate_taxable_income(gross_salary, NSSF, NHDF):
    taxable_income = 0
    if gross_salary <= 5999:
        taxable_income = gross_salary - (NSSF + NHDF)
    elif 6000 <= gross_salary <= 7999:
        taxable_income = gross_salary - (NSSF + NHDF)
    elif 8000 <= gross_salary <= 11999:
        taxable_income = gross_salary - (NSSF + NHDF)
    elif 12000 <= gross_salary <= 14999:
        taxable_income = gross_salary - (NSSF + NHDF)
    elif 15000 <= gross_salary <= 19999:
        taxable_income = gross_salary - (NSSF + NHDF)
    elif 20000 <= gross_salary <= 24999:
        taxable_income = gross_salary - (NSSF + NHDF)
    elif 25000 <= gross_salary <= 29999:
        taxable_income = gross_salary - (NSSF + NHDF)
    elif 30000 <= gross_salary <= 34999:
        taxable_income = gross_salary - (NSSF + NHDF)
    elif 35000 <= gross_salary <= 39999:
        taxable_income = gross_salary - (NSSF + NHDF)
    elif 40000 <= gross_salary <= 44999:
        taxable_income = gross_salary - (NSSF + NHDF)
    elif 45000 <= gross_salary <= 49999:
        taxable_income = gross_salary - (NSSF + NHDF)
    elif 50000 <= gross_salary <= 59999:
        taxable_income = gross_salary - (NSSF + NHDF)
    elif 60000 <= gross_salary <= 69999:
        taxable_income = gross_salary - (NSSF + NHDF)
    elif 70000 <= gross_salary <= 79999:
        taxable_income = gross_salary - (NSSF + NHDF)
    elif 80000 <= gross_salary <= 89999:
        taxable_income = gross_salary - (NSSF + NHDF)
    elif 90000 <= gross_salary <= 99999:
        taxable_income = gross_salary - (NSSF + NHDF)
    else:
        taxable_income = gross_salary - (NSSF + NHDF)
    return taxable_income

taxable_income = calculate_taxable_income(gross_salary, nssf, NHDF)
print(taxable_income)

#TASK 19
def calculate_PAYEE(taxable_income):
    r = 2400
    if 0 <= taxable_income <= 24000:
        PAYEE = 0
    elif 24000 < taxable_income <= 32333:
        PAYEE = (24000 * 0.1) + (0.25 * (taxable_income - 24000)) - r
    elif 32333 < taxable_income <= 500000:
        PAYEE = (24000 * 0.1) + (0.25 * 8333) + (0.3 * (taxable_income - 32333)) - r
    elif 500000 < taxable_income <= 800000:
        PAYEE = (24000 * 0.1) + (0.25 * 8333) + (0.325 * (taxable_income - 500000)) - r
    else:
        PAYEE = (24000 * 0.1) + (0.25 * 8333) + (0.35 * (taxable_income - 800000)) - r
    return PAYEE

PAYEE = calculate_PAYEE(taxable_income)
print(PAYEE)

#TASK 20
def calculate_net_salary(gross_salary, NHIF, NHDF, NSSF, PAYEE):
    net_salary = gross_salary - (NHIF + NHDF + NSSF + PAYEE)
    return net_salary

net_salary = calculate_net_salary(gross_salary, nhif, NHDF, nssf, PAYEE)
print(net_salary)
