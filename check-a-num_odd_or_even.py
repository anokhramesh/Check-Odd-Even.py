#  Check a user input number is Odd Or Even
while True:
    num =int(input(" Enter a number to check it is Odd Or Even\n"))
    if (num %2)==0:
         print("The number {0} is Even".format(num))
         print("-----------------------------------------")

    else:
        print("The Number {0} is Odd".format(num))
        print("-----------------------------------------")

