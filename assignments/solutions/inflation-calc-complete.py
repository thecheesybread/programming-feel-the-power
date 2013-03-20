import csv
import sys
import math
all_items_file = open('all-items.csv', 'r')
all_items_file.readline()
csv_reader = csv.reader(all_items_file)
#Format of this csv file is:
#['Item name', 'Year', 'Average Value']
all_items_cpi = []
for row in csv_reader:
    row[1] = int(row[1])
    row[2] = float(row[2])
    all_items_cpi.append(row)
all_items_file.close()

#Given a year, this function returns the inflation rate for that year.
#cpi_a is the cpi for the previous year
#cpi_b is the cpi for the year
#row[1] is the year, row[2] is the cpi for that year
def get_inflation_rate(year):
    for row in all_items_cpi:
        if row[1] == year - 1:
            cpi_a = row[2]
        if row[1] == year:
            cpi_b = row[2]
    return get_total_change(cpi_a, cpi_b)
    
#Given cpi_a, the cpi for the initial year, and cpi_b, the cpi for the final year, this function returns the total change in price level.
def get_total_change(cpi_a, cpi_b):
    return (cpi_b - cpi_a) / cpi_a * 100

#Given cpi_a, the cpi at year_a, and cpi_b, the cpi at year_b, this function returns the average change in price level per year.
def get_change_per_year(year_a, year_b, cpi_a, cpi_b):
    return (math.pow(cpi_b/cpi_a, 1.0/(year_b - year_a)) - 1) * 100


#has data from 1913 - 2012
def get_maximum_inflation_year():
    max_inflation_rate_so_far = 0
    max_inflation_year = 0
    for year in range(1914, 2013):
        inflation_rate = get_inflation_rate(year)
        #replace this with your solution
        #feel free to modify/delete anything! This is only just a skeleton


        

    return max_inflation_year #replace this with the correct answer






all_data_file = open('all-data.csv', 'r')
all_data_file.readline()
csv_reader = csv.reader(all_data_file)
all_data_cpi = []
items_set = set()
for row in csv_reader:
    row[1] = int(row[1])
    row[2] = float(row[2])
    all_data_cpi.append(row)
    items_set.add(row[0])
all_data_file.close()
items_list = list(items_set)


#row[0] is the name of the item
#row[1] is the year of the entry
#row[2] is the price level of the item at that year
def get_avg_deviation_from_inflation(item):
    previous_year_price_level = -1
    deviations = []
    for row in all_data_cpi:
        item_name = row[0]
        year = row[1]
        price_level = row[2]
        if item_name == item:
            if previous_year_price_level != -1:
                inflation_rate = get_inflation_rate(year)
                item_change = get_total_change(previous_year_price_level, price_level)
                deviations.append(math.fabs(inflation_rate - item_change))
            previous_year_price_level = price_level
    return sum(deviations)/len(deviations)


            
#how could you modify this function to get all deviations at any level
def get_items_with_high_deviation_from_inflation():
    items = []
    for item in items_list:
        if get_avg_deviation_from_inflation(item) > 8:
            items.append(item)
    return items














#_______________________________________TESTING CODE____________________________________________
#_______________________________________THIS PRINTS THINGS OUT TO TEST YOUR CODE'S CORRECTNESS _______________


def print_inflation_rates(year_a, year_b):
    for row in all_items_cpi:
        if row[1] == year_a:
            cpi_a = row[2]
        if row[1] == year_b:
            cpi_b = row[2]
    print 'Total inflation from ' + str(year_a) + ' to ' + str(year_b) + ' is ' + str(get_total_change(cpi_a, cpi_b)) + ' percent.'
    print 'Average inflation per year from ' + str(year_a) + ' to ' + str(year_b) + ' is ' + str(get_change_per_year(year_a, year_b, cpi_a, cpi_b)) + ' percent.'




print "The year with the most inflation should be 1917. You got " + str(get_maximum_inflation_year())
print "The average deviation between the change in the price levels of apples and inflation is " + str(get_avg_deviation_from_inflation("Apples"))
print "The items from the CPI that deviate a significant amount from the inflation should be ['Gasoline (all types)', 'Telephone hardware, calculators, and other consumer information items', 'Butter', 'Computer software and accessories', 'Propane, kerosene, and firewood', 'Gasoline, unleaded regular', 'Fuel oil and other fuels', 'Gasoline, unleaded midgrade', 'Personal computers and peripheral equipment', 'Gasoline, unleaded premium', 'Photographic equipment', 'Other video equipment', 'Fuel oil', 'Information technology commodities', 'Televisions', 'Information technology, hardware and services', 'Video and audio products', 'Other motor fuels', 'Oranges, including tangerines']" + "\n Your results are" + str(get_items_with_high_deviation_from_inflation())
