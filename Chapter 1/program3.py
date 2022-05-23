copies = int(input("How many copies are you buying? "))

if copies >= 1 and copies <= 10:
    unitPrice = 99
elif copies > 10 and copies <= 50:
    unitPrice = 89
elif copies > 50 and copies <= 100:
    unitPrice = 79
elif copies >= 101:
    unitPrice = 69

print("Unit price:", "${:,.2f}".format(unitPrice))
print("Total price:", "${:,.2f}".format(unitPrice * copies))
