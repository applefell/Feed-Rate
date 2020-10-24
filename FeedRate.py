spindle_speed = float(input("What is your spindle speed?"))
fpt = float(input("What is your feed per tooth?"))
num_teeth = float(input("How many teeth/flutes are on your cutting tool?"))

feed = (spindle_speed * fpt * num_teeth)/12

print("Your feed rate is " + str(feed) + " feet per minute")