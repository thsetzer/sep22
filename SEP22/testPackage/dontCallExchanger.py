
import time

def main():
    start = time.time()
    myList = ["Juergen", 33343334443]
    
    for iteration in range(1000000):
        myList[1], myList[0] = myList[0], myList[1] 
        print("iteration nr", iteration)
    end = time.time()
    print(f"Runtime of the program is {end - start}")
    # Runtime of the program is 4.875604152679443
main()
# Runtime of the program is 5.730135202407837