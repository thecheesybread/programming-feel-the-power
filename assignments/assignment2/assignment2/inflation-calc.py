import csv
import math


#READS IN EACH ROW FROM ALL-ITEMS.CSV AND PUTS IT INTO ALL_ITEMS_CPI AS A LIST
all_items_file = open('all-items.csv', 'r')
all_items_file.readline()
csv_reader = csv.reader(all_items_file)
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

#***********************FILL THIS OUT********************
def get_total_change(cpi_a, cpi_b):
    return 0 #fill this out Remember the equation for total change from x to y is (y - x) / x * 100. Apply this same formula to cpi_a and cpi_b and return the result.


#*****************FILL THIS OUT********************
def get_maximum_inflation_year():
    max_inflation_rate_seen_so_far = 0
    max_inflation_year = 0
    for year in range(1914, 2013):
        inflation_rate = get_inflation_rate(year)

        #replace this with your solution
        #feel free to modify/delete anything! This is only just a skeleton
        #you have to figure out max_inflation_year inside here
        

    return max_inflation_year





#READS IN EACH ROW FROM SPECIFIC-ITEMS.CSV AND PUTS IT INTO SPECIFIC_ITEMS AS A LIST
specific_items_file = open('specific-items.csv', 'r')
specific_items_file.readline()
csv_reader = csv.reader(specific_items_file)
specific_items = []
items_set = set()
for row in csv_reader:
    row[1] = int(row[1])
    row[2] = float(row[2])
    specific_items.append(row)
    items_set.add(row[0])
specific_items_file.close()
items_list = list(items_set)





#row[0] is the name of the item
#row[1] is the year of the entry
#row[2] is the price level of the item at that year
def get_avg_deviation_from_inflation(item):
    previous_year_price_level = -1
    deviations = []
    for row in specific_items:
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


            
#Returns a list of items whose price levels deviate from inflation by more than 8%
#*****************FILL THIS OUT********************
def get_items_with_high_deviation_from_inflation():

    #HINT: Use items_list (a list of all the items inside specific_items) and get_avg_deviation_from_inflation
    #fill in stuff here
    #fill in stuff here
    #fill in stuff here
    #fill in stuff here


    return [] #fixme









#_______________________________________TESTING CODE____________________________________________
#_______________________________________THIS PRINTS THINGS OUT TO TEST YOUR CODE'S CORRECTNESS _______________





print "The total change between 10 to 15 should be 50%. You got " + str(get_total_change(10, 15))
print
print "The year with the most inflation should be 1917. You got " + str(get_maximum_inflation_year())
print
print "The average deviation between the change in the price levels of apples and inflation is " + str(get_avg_deviation_from_inflation("Apples"))
print
print "The items from the CPI that deviate a significant amount from the inflation should be ['Gasoline (all types)', 'Telephone hardware, calculators, and other consumer information items', 'Butter', 'Computer software and accessories', 'Propane, kerosene, and firewood', 'Gasoline, unleaded regular', 'Fuel oil and other fuels', 'Gasoline, unleaded midgrade', 'Personal computers and peripheral equipment', 'Gasoline, unleaded premium', 'Photographic equipment', 'Other video equipment', 'Fuel oil', 'Information technology commodities', 'Televisions', 'Information technology, hardware and services', 'Video and audio products', 'Other motor fuels', 'Oranges, including tangerines']" + "\n Your results are" + str(get_items_with_high_deviation_from_inflation())
