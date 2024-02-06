"""Systema access module"""
import sys
import time

st = time.time()
numbers_list, end_list = [], []
DATA_LIST = ""
TOTAL_SUM_NUMBERS = 0

def get_mean(number_list):
    "Input a list and return the mean"
    #sort_list = sorted(list)
    list_count = len(number_list)
    mean = TOTAL_SUM_NUMBERS / list_count
    return mean

def get_median(number_list):
    "Input a list and return the median"
    sorted_numbers = sorted(number_list)
    list_count = len(number_list)

    if list_count % 2 == 0:
        half_1 = sorted_numbers[list_count//2]
        half_2 = sorted_numbers[list_count//2 - 1]
        median = (half_1 + half_2) / 2
    else:
        median = sorted_numbers[list_count//2]
    return median

def get_mode(number_list):
    "Input a list and return the mode"
    max_value = 0

    sorted_numbers = sorted(number_list)
    list_count = len(number_list)
    counts = dict()
    for i in sorted_numbers:
        counts[i] = counts.get(i, 0) + 1

    for value, key in counts.items():
        if key >= max_value:
            max_value = key
            mode = value

    #mode = [k for k, v in counts.items() if v == max(list(counts.values()))]

    if len(counts) == list_count:
        return "NA"
    else:
        return  mode


def get_variance(number_list):
    "Input a list and return the variance"
    sum_num = 0
    list_count = len(number_list)
    mean = get_mean(number_list)

    for n in number_list:
        num = (n - mean)**2
        sum_num += num

        variance = sum_num/list_count

    return variance

def get_standard_deviation(number_list):
    "Input a list and return the standard deviation"
    sd = (get_variance(number_list)) ** 0.5

    return sd

try:
    file_location = sys.argv[1]

    with open(file_location, "r", encoding="utf-8") as data_file:
        DATA_LIST = data_file.readlines()
except  IndexError:
    print("Please also add the file whi le invoking the script.")
    sys.exit()

#for index in range(len(DATA_LIST)):
for index in range(len(DATA_LIST)):
    try:
        number = float(DATA_LIST[index].strip())

        numbers_list.append(number)
        TOTAL_SUM_NUMBERS += number

    except  ValueError:
        print(f"The value {DATA_LIST[index].strip()} is invalid and will be skipped.")


mean_result = get_mean(numbers_list)
median_result = get_median(numbers_list)
mode_result = get_mode(numbers_list)
variance_result = get_variance(numbers_list)
sd_result = get_standard_deviation(numbers_list)

print("\n")
print(f"The mean is: {mean_result}")
print(f"The median is: {median_result}")
print(f"The mode is: {mode_result}")
print(f"The variance is: {variance_result}")
print(f"The SD is: {sd_result}")

# get the end time
et = time.time()
# get the execution time
elapsed_time = et - st

end_list.append(f"The mean is: {mean_result}\n")
end_list.append(f"The median is: {median_result}\n")
end_list.append(f"The mode is: {mode_result}\n")
end_list.append(f"The variance is: {variance_result}\n")
end_list.append(f"The SD is: {sd_result}\n")
end_list.append(f"Execution time:{elapsed_time} seconds")

with open("StatisticsResults.txt", "w", encoding="utf-8") as data_file:
    data_file.writelines(end_list)

print(f"Execution time:{elapsed_time} seconds")
