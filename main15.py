def palin(r):
    end = len(r)-1
    start = 0
    while (start < end):
        if (r[start]!=r[end]):
            return False
        start +=1
        end -=1
    return True

r = (1,2,3,3,2,1)
if (palin(r)):
    print("The tuple is a flip-flop")
else:
    print("Tuple is not a flip-flop")