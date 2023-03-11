year = int(input("Which Year Do You Want To check?\n"))

if year % 4 == 0:
    if year % 100 ==0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print ("Not Leap Year")
    else:
        print ("Leap Year")
else:
  print(f"Year {year} is NOT a leap year")
