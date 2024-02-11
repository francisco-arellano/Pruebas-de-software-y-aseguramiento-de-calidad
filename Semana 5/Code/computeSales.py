"""System module access"""
import sys
import json
import time

st = time.time()
prouct_sales_dictionary_list, end_list = [], []
sums = {}

# We open both of our files as Json format
try:
    first_file_location = sys.argv[1]
    second_file_location = sys.argv[2]

    with open(first_file_location, "r", encoding="utf-8") as data_file1:
        PRICE_CATALOGUE = json.load(data_file1)

    with open(second_file_location, "r", encoding="utf-8") as data_file2:
        SALES_RECORD = json.load(data_file2)
except IndexError:
    print("Please also add two files while invoking the script.")
    print("Eg. python computeSales.py priceCatalogue.json salesRecord.json")
    sys.exit()

# Creating a loop to get the total Quantity for each sale record
for d in SALES_RECORD:
    try:
        sums[d['Product']] = sums.get(d['Product'], 0) + int(d['Quantity'])
    except ValueError:
        print(f"The value {d['Quantity']} is invalid and will be skipped")

# This loop gets the total quantity and matches both files
# Then creates a dictionary with the needed values
for p in PRICE_CATALOGUE:
    for s in sums.items():
        if p["title"] == s[0]:
            try:
                prouct_sales_dictionary_list.append({
                    "Product": str(s[0]),
                    "Quantity": s[1],
                    "Price": float(p['price'])
                    })
            except ValueError:
                print(f"The value:{p['price']} is invalid and will be skipped")

# Finally there is a final loop to print and append the values for the txt
FINAL_TOTAL = 0
for index, d in enumerate(prouct_sales_dictionary_list):
    total = d["Quantity"] * d["Price"]
    print(f"Product: {d["Product"]}")
    end_list.append(f"Product: {d["Product"]}")
    print(f"Qty: {d["Quantity"]} - Price: {d["Price"]}$ - Subtot: {total}$\n")
    end_list.append(
        f" - Qty: {d["Quantity"]} - Price: {d["Price"]}$ - Subtot: {total}$\n")
    FINAL_TOTAL += total
print(f"Total: {FINAL_TOTAL}$")
end_list.append(f"Total: {FINAL_TOTAL}$\n")

# get the end time
et = time.time()
# get the execution time
elapsed_time = et - st

# Print ellapsed time
print(f"Execution time: {elapsed_time} seconds")
end_list.append(f"Execution time: {elapsed_time} seconds")

# Save data in a txt
with open("SalesResults.txt", "w", encoding="utf-8") as data_file:
    data_file.writelines(end_list)
