import sys

def simpleInt(pr, intr, time):
    return (pr*intr*time)/100

if __name__ == "__main__ ":
    p = int(sys.argv[1])
    i = float(sys.argv[2])
    t = int(sys.argv[3])

    si = simple_interest(p, r, t)  
    print("Simple Interest:", si) 
