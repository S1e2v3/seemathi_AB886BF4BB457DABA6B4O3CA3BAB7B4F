def isleapyear(year):
  if (year % 4 == 0and year% 100 != 0)or year % 400 == 0:
    return True
  else:
    return False 
year=int(input("enter a year:"))
if isleapyear:
    print(year,"is a leap year.")
else:
    print(year,"is not a leap year.")