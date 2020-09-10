M82589933 = open("M82589933.txt", "r")
number = M82589933.read().replace("\n","").replace(",","")
M82589933.close()

f = open("M82589933_treated.txt", "a")
f.write(number)
f.close()