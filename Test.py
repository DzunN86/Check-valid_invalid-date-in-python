def dayNum(m, d, y):

  dayFormula = 31*(m-1) + d
  febVar = (4*m + 23)//10
  
  if m<3:
    return dayFormula-febVar
  elif m>2:
    if y%4 == 0: #Possible leap year
      if y%100==0 and y%400 !=0:
        return dayFormula-febVar        #Not a leap year
      else:
        return dayFormula-febVar + 1      #A leap year
    else:
      return dayFormula-febVar
      
def verifyDate(dateStr):
  day = eval(dateStr[0])
  month = eval(dateStr[1])
  year = eval(dateStr[2])
  
  month31 = [1, 3 , 5, 7, 8, 10, 12]
  month30 = [4, 6, 9, 11]
  
  if month <=12 and month >=1:                     
    #For month = 2 or febuary
    if month == 2:
        if year%4==0:
            if year%100==0 and year%400!=0 and day==29:
                return "INVALID DATE"
            elif day<=29 and day>=1:
                return dayNum(month, day, year)
            else:
                return "INVALID DATE"
        elif day<=28:
            return dayNum(month, day, year)
        else:
            return "INVALID DATE"
    # If month = 31 days
    elif month in month31:
        if day<=31 and day>=1:
            return dayNum(month, day, year)
        else:
            return "INVALID DATE"
    # If month = 30 days
    elif month in month30:
        if day<=30 and day>=1:
            return dayNum(month, day, year)
        else:
            return "INVALID DATE"
  else: # Error with month                                      
      return "INVALID DATE"



def main():
  print("Accepts a date in d/m/y format and outputs if it is valid and the day's number.")
  
  dateStr = input("Please enter date(d/m/y): ")
  dateList = dateStr.split("/")
  print("That day is {0}.".format(verifyDate(dateList)))


main()