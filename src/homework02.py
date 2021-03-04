import os
import csv

path = os.path.dirname(os.path.abspath(__file__))
full_path_in = os.path.join(path, 'who_suicide_statistics.csv')

#reading the dataset and converting it to a list
with open("who_suicide_statistics.csv") as input_file:
    reader = csv.reader(input_file)
    data = list(reader)

#removing the first row
data.remove(data[0])

#creating 2 lists of all the numeric values in the suicide_no and population columns
suicide_no_list = []
population_no_list = []
year_list = []

for value in data:
    if value[4] != '':
        suicide_no_list.append(int(value[4]))

    if value[5] != '':
        population_no_list.append(int(value[5]))

    if value[1] != '':
        year_list.append(int(value[1]))

#calculating the maximum and the minimum values for the number of suicides, population and year
max_suicide_no = max(suicide_no_list)
min_suicide_no = min(suicide_no_list)
print("Maximum number of suicides: ", max_suicide_no)
print("Minimum number of suicides: ", min_suicide_no)

max_population_no = max(population_no_list)
min_population_no = min(population_no_list)
print("Maximum number of population: ", max_population_no)
print("Minimum number of population: ", min_population_no)

max_year = max(year_list)
min_year = min(year_list)
print("Maximum year: ", max_year)
print("Minimum year: ", min_year)

#calculating the mean for the suicides and the population
totalsuicides = 0
totalpopulation = 0
scountries = 0
pcountries = 0
for value in data:
    if value[4] != '':
        totalsuicides += int(value[4])
        scountries += 1

    if value[5].isdigit() == True:
        totalpopulation += int(value[5])
        pcountries += 1

suicidemean = totalsuicides/scountries
populationmean = totalpopulation / pcountries

print("Mean suicides: ", int(suicidemean))
print("Mean population: ", int(populationmean))

#calculating the range for the suicides and the population
suiciderange = int(max_suicide_no) - int(min_suicide_no)
populationrange = int(max_population_no) - int(min_population_no)
print("Range of suicides: ", suiciderange)
print("Range of suicides: ", populationrange)

#calculating the variation of suicide and population
sdeviations = []
pdeviations = []
scountries = 0
pcountries = 0
for value in data:
    if value[4] != '':
        scountries += 1
        sdeviations.append((int(value[4]) - suicidemean)**2)

    if value[5] != '':
        pcountries += 1
        pdeviations.append((int(value[5]) - populationmean)**2)

svariance = sum(sdeviations)/(scountries-1)
pvariance = sum(pdeviations)/pcountries

print("Variation of the suicides", svariance)
print("Variation of the population", int(pvariance))

#calculating the number of males and females who committed suicide
male = 0
female = 0
for value in data:
    if value[4] != '':
        if value[2] == "male":
            male += int(value[4])
        else:
            female += int(value[4])

print("Number of males who committed suicide: ", male)
print("Number of females who committed suicide: ", female)


