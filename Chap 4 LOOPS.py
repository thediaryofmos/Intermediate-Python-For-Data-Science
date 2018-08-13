# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset>0:
        offset=offset-1
    else:
        offset=offset+1
    print(offset)
##

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for a in areas:
    print (a)
##

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index, a in enumerate(areas) :
    print("room " + str(index)+ ': ' +str(a))
##

# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
for x in house:
    print("the "+str (x[0])+ " is "+ str(x[1])+" sqm")
##

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for val,cap in europe.items() :
    print("the capital of "+ val+ " is "+str(cap))
##

# Import numpy as np
import numpy as np

# For loop over np_height
for val in np_height:
    print(str(val)+" inches")

# For loop over np_baseball
for val in np.nditer(np_baseball):
    print(str(val))
##

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for lab,row in cars.iterrows():
    print(lab)
    print(row)
##

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Adapt for loop
for lab, row in cars.iterrows() :

    print(lab+': ' + str(row['cars_per_cap']))
##

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for lab,row in cars.iterrows():

    cars.loc[lab,"COUNTRY"]= cars.loc[lab,'country'].upper()


# Print cars
print(cars)
##

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Use .apply(str.upper)
cars["COUNTRY"] =cars["country"].apply(str.upper)
print(cars)

##########################################
