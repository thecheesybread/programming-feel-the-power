
import csv

#input_file = open('cu.data.1.AllItems.txt', 'r')
#input_file = open('cu.data.0.Current.txt', 'r')
input_file = open('cu.data.Education.txt', 'r')
print input_file.readline()
data = {}
for line in input_file:
    line_split = line.split('\t')
    series_id = line_split[0].strip()
    year = line_split[1].strip()
    period = line_split[2].strip()
    value = line_split[3].strip()
    if series_id not in data:
        data[series_id] = {}
    if year not in data[series_id]:
        data[series_id][year] = []
    data[series_id][year].append(float(value))            
input_file.close()
#data_dumped = json.dumps(data)
#output_file = open('cleaned_cpi_data.txt', 'w')




#Converts the series_id to the item_code
series_file = open('cu.series.txt', 'r')
print series_file.readline()
series_id_to_item_code = {}
for line in series_file:
    line_split = line.split('\t')
    series_id = line_split[0].strip()
    item_code = line_split[2].strip()
    series_id_to_item_code[series_id] = item_code
series_file.close()


#Converts the item_code to the item_name
item_file = open('cu.item.txt', 'r')
print item_file.readline()
item_code_to_item_name = {}
for line in item_file:
    line_split = line.split('\t')
    item_code = line_split[0].strip()
    item_name = line_split[1].strip()
    item_code_to_item_name[item_code] = item_name
item_file.close()


#creates series_id to item_name
series_id_to_item_name = {}
for series_id, item_code in series_id_to_item_code.items():
    series_id_to_item_name[series_id] = item_code_to_item_name[item_code]



l = [1,2,3,4]
sum(l) / float(len(l))
#creates data with name and values averaged over each year and writes it to a file
data_output = open('clean_cpi_data.csv', 'w')
csv_writer = csv.writer(data_output)
csv_writer.writerow(('Item name', 'Year', 'Average Value'))
for series_id, year_dict in data.items():
    for year, cpis in year_dict.items():
        csv_writer.writerow((series_id_to_item_name[series_id], year, sum(cpis)/float(len(cpis)) ))



#output_file.write(data_dumped)
#output_file.close()


