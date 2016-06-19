f = open('dq_unisex_names.csv', 'r') #opens file
data = f.read() #reads in the csv

data_list = data.split('\n') #splits data on line break
string_data = [] #creates a new list of lists
for line in data_list:
    comma_list = line.split(',')
    string_data.append(comma_list)
print(string_data[0:5]) 

numerical_data = [] #convert numerical values to floats
for line in string_data:
    name = line[0]
    count = float(line[1])
    new_list = [name,count]
    numerical_data.append(new_list)
print(numerical_data[0:5])

numerical_data[len(numerical_data)-1] #Filter the list to get a list of names with 1000 or more people share
thousand_or_greater = []
for line in numerical_data:
    name = line[0]
    population = line[1]
    if population >= 1000:
        thousand_or_greater.append(name)
print(thousand_or_greater[0:10])
