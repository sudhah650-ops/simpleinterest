import sys

def simple_interest(principle, interest, time):
    return (principle*interest*time)/100

if__name__=="__main__":
    p = int(sys.argv[1])
    i = float(sys.argv[2])
    t = int(sys.argv[3])

    print("simple interest is:", simple_interest(p,i,t))