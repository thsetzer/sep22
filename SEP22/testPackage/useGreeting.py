'''
Created on 15.09.2022

@author: thsetzer
'''
import testPackage.HelloYou as t

my_greeter = t.Greeting("Setzer")
my_greeter.greed("Thomas")
print(my_greeter.lastname)

my_servus =t.Servus("Müller")
my_servus.greed("Stefan")
print(my_servus.lastname)


# sys.path.append("/Users/thsetzer/Library/CloudStorage/OneDrive-ku.de/WFI_WI/Lehre (OneDrive)/22_23_WSEM/SEP_Python/code/Workspace/SEP22")
#in python shell:
#import sys

# sys.path.append(".")