import csv
import os


with open(os.path.join('SKU', '3e49ae3c-1acf-41b7-b184-7c463c4bf7de.csv'), newline='') as csvfile:
    reader = csv.DictReader(csvfile)  # , delimiter=' ', quotechar='|')
    # reader[0] - это не список, это подвид генератора
    one_column = list()
    for row in reader:
        if 'Z' in row['sku']:
            one_column.append(row['sku'])
    print(one_column)

with open(os.path.join('SKU', '3e49ae3c-1acf-41b7-b184-7c463c4bf7de.csv'), newline='') as csvfile:
    reader = csv.DictReader(csvfile)  # , delimiter=' ', quotechar='|')
    # [1, 2, 3, 4, 5]
    # синтаксический сахар
    one_column_compr = [row['sku'] for row in reader if 'Z' in row['sku']]
    print(one_column_compr)