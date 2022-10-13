'''
Created on 15.09.2022
    
@author: thsetzer
'''

import testPackage.ClassWithMethodExchangingItemsinListManyTimes as ex
import time

def main():
    start = time.time()
    superSmallList = ["Juergen", 33343334443]
    myExchanger = ex.Exchanger()
    myExchanger.exchange(superSmallList, 1000000)
    end = time.time()
    print(f"Runtime of the program is {end - start}")
    # Runtime of the program is 4.875604152679443
main()

#in python shell:
# open folder with cd "/Users/thsetzer/Library/CloudStorage/OneDrive-ku.de/WFI_WI/Lehre (OneDrive)/22_23_WSEM/SEP_Python/code/Workspace/SEP22/testPackage"
# python3
# import sys
# sys.path.append("/Users/thsetzer/Library/CloudStorage/OneDrive-ku.de/WFI_WI/Lehre (OneDrive)/22_23_WSEM/SEP_Python/code/Workspace/SEP22")
# sys.path.append(".") # can be skipped
# exec(open("callExchanger.py").read())
# python3 callExchanger
# look at __pycache_- folder
