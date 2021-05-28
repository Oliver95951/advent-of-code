import math
from numpy.core.numeric import True_, full_like
import pandas
from re import split

raw_input= """118505
138608
125418
146131
136211
98802
95533
65338
50826
118071
54328
108176
60708
99108
64556
103726
87778
108165
78648
68391
79748
94421
137497
138264
125872
127901
116850
93683
68526
134908
102609
69769
106181
89986
127197
74669
109912
51328
125824
105763
70648
66476
117452
50181
70915
92821
94381
130405
128627
65090
125594
148506
95193
143595
71834
147624
142247
112838
149474
139785
134850
92177
110591
102115
141224
117174
68695
65212
54709
51982
53791
68079
120439
76513
132952
132959
142650
135186
59593
83982
56889
141751
87634
148232
50803
63222
97836
103121
106561
88348
69735
75400
74045
56715
101561
124401
106296
144550
134903
113838"""

# Part 1

mass_fuel_dict= {'Mass':[], 'Fuel Required':[]}
def fuelCalculation(mass: int):
    x = math.floor((mass / 3)) - 2
    return x

split_input = raw_input.split("\n")

for x in split_input:
    mass_fuel_dict['Mass'].append(int(x))

for x in mass_fuel_dict['Mass']:
    mass_fuel_dict['Fuel Required'].append(fuelCalculation(x))

df = pandas.DataFrame(data=mass_fuel_dict)

sum = 0
for fuel in mass_fuel_dict['Fuel Required']:
    sum += fuel

print(sum)

# Part 2

def fuelRequired(mass: int):
    starting_fuel = math.floor((mass / 3)) - 2  
    return starting_fuel 

def fuelCalculationiterated(startingFuel: int):
    again = True
    fuel_sum = 0
    while again:
        fuel_sum += startingFuel
        if fuelRequired(startingFuel) <= 0:
            again = False
        else:
            again = True
        startingFuel = fuelRequired(startingFuel)
    
    return fuel_sum

mass_fuel_dict= {'Mass':[], 'Starting Fuel':[], 'Fuel Required':[]}

split_input = raw_input.split("\n")

for x in split_input:
    mass_fuel_dict['Mass'].append(int(x))

for x in mass_fuel_dict['Mass']:
    mass_fuel_dict['Starting Fuel'].append(fuelCalculation(x))

for x in mass_fuel_dict['Mass']:
    mass_fuel_dict['Fuel Required'].append(fuelCalculationiterated(fuelRequired(x)))

df = pandas.DataFrame(data=mass_fuel_dict)

print(df)
sum = 0
for fuel in mass_fuel_dict['Fuel Required']:
    sum += fuel

print(sum)