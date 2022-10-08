print("AMOUNT TO BE PAID BASED ON DISTANCE TRAVELLED")
name = str(input("Hello there, what's your name?"))
distance = int(input("Kindly, enter the distance travelled:"))

if distance >= 0 and distance <= 100:
    print("The cost is $5.00 and the distance travelled is {}".format(distance))
elif distance >= 101 and distance <= 500:
    print("The cost is $8.00 and the distance travelled is {}".format(distance))
elif distance >= 501 and distance <= 1000:
    print("The cost is $10.00 and the distance travelled is {}".format(distance))
elif distance > 1000:
    print("The cost is $12.00 and the distance travelled is {}".format(distance))
else:
    print(name,"you have an invalid meeeehn!!!")
