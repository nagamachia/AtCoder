N = input()

a = N[-1]

if a == "3":
    print("bon")
elif a in ["0","1","6","8"]:
    print("pon")
else:
    print("hon")