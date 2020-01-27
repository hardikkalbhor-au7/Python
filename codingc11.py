def check():
    datafile = open('ccqueston.txt')
    found = False
    for line in datafile:
        if "python" in line:
            found = True
            break

check()
if True:
    print("true")
else:
    print("false")