height = float(input("Enter the height from which the ball is dropped: "))
bounce = float(input("Enter the bounciness index of the ball: "))
numBounces = int(input("Enter the number of times the ball is allowed to continue bouncing: "))
distTraveled = 0.0
for i in range(numBounces):
    distTraveled += height + height * bounce
    height = height * bounce

print("Total distance traveled is:", distTraveled, "units.")
