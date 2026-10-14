import datetime
import time
import math
import random
import string
import uuid
import os

while True:
    print("\n--------------------------")
    print("Welcome to Multi-Utility Toolkit")
    print("1. Datetime and time operation")
    print("2. Mathematical operation")
    print("3. Random Data Generation")
    print("4. Generate unique Identifiers(UUID)")
    print("5. File Operations (Custom Module)")
    print("6. Explore Module Attributes (dir())")
    print("7. Exit")

    ch = input("Enter Your Choice:")

    if ch == "1":
        print("\nDatetime and time operation:")
        print("1. Display Current Date and Time")
        print("2. Calculate Difference Between Two Dates")
        print("3. Format Date into Custom Format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        c = input("Enter your Choice:")

        if c == "1":
            print("Current Date and Time:", datetime.datetime.now())

        elif c == "2":
            d1 = datetime.date.fromisoformat(input("Enter the first date (YYYY-MM-DD):"))
            d2 = datetime.date.fromisoformat(input("Enter the second date (YYYY-MM-DD):"))
            print("Difference:", abs((d2-d1).days), "days")

        elif c == "3":
            d = datetime.datetime.now()
            print("Formatted Date:", d.strftime("%d-%m-%Y"))

        elif c == "4":
            input("Press Enter to start stopwatch")
            start = time.time()
            input("Press Enter to stop stopwatch")
            print("Elapsed Time:", round(time.time()-start, 2), "seconds")

        elif c == "5":
            n = int(input("Enter Countdown time in Seconds:"))
            time.sleep(n)
            print("Time's up!")

    elif ch == "2":
        print("\nMathematical operation:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")

        c = input("Enter Your Choice:")

        if c == "1":
            n = int(input("Enter a Number:"))
            print("Factorial:", math.factorial(n))

        elif c == "2":
            p = float(input("Enter Principal amount:"))
            r = float(input("Enter rate of interest (in %):"))
            t = float(input("Enter time (in years):"))
            print("Compound Interest:", round(p*(1+r/100)**t-p, 2))
            print("Total Amount:", round(p*(1+r/100)**t, 2))

        elif c == "3":
            a = float(input("Enter the degrees:"))
            print("Sin:", round(math.sin(math.radians(a)), 4))
            print("Cos:", round(math.cos(math.radians(a)), 4))

        elif c == "4":
            r = float(input("Enter radius of circle:"))
            print("Area of Circle:", round(math.pi*r*r, 2))

        elif c == "5":
            continue

    elif ch == "3":
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")

        c = input("Enter Your Choice:")

        if c == "1":
            print("Random Number:", random.randint(1, 100))

        elif c == "2":
            n = int(input("Enter list length:"))
            print("Random List:", [random.randint(1, 100) for _ in range(n)])

        elif c == "3":
            n = int(input("Enter password length:"))
            chars = string.ascii_letters + string.digits + "!@#$%"
            print("Generated Password:", "".join(random.choices(chars, k=n)))

        elif c == "4":
            print("Generated OTP:", random.randint(100000, 999999))

    elif ch == "4":
        print("Generated UUID:", uuid.uuid4())

    elif ch == "5":
        print("\nFile Operations:")
        name = input("Enter file name:")
        print("1. Create File")
        print("2. Write File")
        print("3. Read File")
        print("4. Append File")
        c = input("Enter Your Choice:")

        if c == "1":
            open(name, "w").close()
            print("File created successfully!")

        elif c == "2":
            with open(name, "w") as f:
                f.write(input("Enter data to write:"))
            print("Data written successfully!")

        elif c == "3":
            if os.path.exists(name):
                with open(name, "r") as f:
                    print("File Content:", f.read())
            else:
                print("File not found!")

        elif c == "4":
            with open(name, "a") as f:
                f.write("\n" + input("Enter data to append:"))
            print("Data appended successfully!")

    elif ch == "6":
        m = input("Enter module name to explore:")
        try:
            print("Available Attributes:", dir(__import__(m))[:20])
        except ImportError:
            print("Module not found!")

    elif ch == "7":
        print("Thank you for using the Multi-Utility Toolkit!")
        break

    else:
        print("Invalid Choice!")
