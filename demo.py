import time

a = 3
b = 2

def signal():
    return a > b


def none_signal():
    print("It's ok")

def revers_signal(s):
    if s:
        print("Close all")
        print("B")
    else: 
        print("Close all")
        print("S")

while True:
    s = signal()

    if s == s:
        none_signal()
    else:
        revers_signal(s)
    time.sleep(5)



