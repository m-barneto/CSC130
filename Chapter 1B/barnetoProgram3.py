print(f"{'Name':<13}{'Rate':<14}{'Hours':<14}{'Total Pay':<14}")
with open("payroll_data.txt", "r") as f:
    for line in f:
        values = line.split(" ")
        name = values[0]
        rate = float(values[1])
        hours = float(values[2])
        print("{0:<13}{1:<14.2f}{2:<14.2f}{3:<14.2f}".format(name, rate, hours, rate * hours))