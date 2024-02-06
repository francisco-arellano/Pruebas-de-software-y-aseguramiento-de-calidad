"""Module providing a function printing python version."""
import sys
import time

st = time.time()
word_count_list = []
end_list = []

def count_word(current_list):
    "Input a list of words and returns dictionary with each counted word"
    counts = {}
    for i in current_list:
        counts[i] = counts.get(i, 0) + 1

    return counts

try:
    file_location = sys.argv[1]

    with open(file_location, "r", encoding="utf-8") as data_file:
        data_list = data_file.readlines()
except  IndexError:
    print("Please also add the file while invoking the script.")
    sys.exit()

for index in range(len(data_list)):
#for index in enumerate(data_list):
    try:
        word = str(data_list[index].strip())

        word_count_list.append(word)

    except  ValueError:
        print(f"The value {data_list[index].strip()} is invalid and will be skipped.")

counted_word_dict = count_word(word_count_list)
sorted_footballers_by_goals = sorted(counted_word_dict.items(), key=lambda x:x[1], reverse=True) 

for w in sorted_footballers_by_goals:
    print(f"{w[0]} - {w[1]}")
    end_list.append(f"{w[0]} - {w[1]}\n")

# get the end time
et = time.time()
# get the execution time
elapsed_time = et - st

end_list.append(f"Execution time:{elapsed_time} seconds")

with open("WordCountResults.txt", "w", encoding="utf-8") as data_file:
    data_file.writelines(end_list)

print(f"Execution time:{elapsed_time} seconds")
