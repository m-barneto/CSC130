OVERTIME_MULT = 1.5

hourlyWage = float(input("Enter hourly wage: $"))
regHours = float(input("Enter the regular hours: "))
overHours = float(input("Enter the overtime hours: "))

weeklyPay = hourlyWage * regHours + hourlyWage * OVERTIME_MULT * overHours
print("The total weekly pay is", "${:,.2f}".format(weeklyPay))
