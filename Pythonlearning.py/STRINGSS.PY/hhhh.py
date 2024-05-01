a=2**32
print(a)
b=a/2
print(b)

import time
my_time=int(input("Enter time in seconds: "))
for i in range(my_time,0,-1):
    print(i)
    time.sleep(1)    
print("HAPPY NEW YEAR!")    