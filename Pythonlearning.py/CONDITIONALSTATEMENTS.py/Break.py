numbers=list(range(0,10))
for i in numbers:
    if i==6:
     print(i,"Available")
     break
    else:
       print(i,"Not Available")

      #  # CORRECT PIN
      #  correct_pin=1234
      #  Attempts=3
      #  for i in range(1,4):
      #     pin=int(input("Enter Pin: "))
      #     if pin==correct_pin:
      #        print("Access Granted!")
      #        break
      #     else:
      #        Remaining_Attempts=Attempts-i
      #        if Remaining_Attempts>0:
      #           print("Re-enter Pin")
      #  else:
      #     print("Blocked!")
             