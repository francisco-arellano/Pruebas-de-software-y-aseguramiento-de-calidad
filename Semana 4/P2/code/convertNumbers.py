"""Module providing a function printing python version."""
import sys
import time

st = time.time()
end_list = []

def get_binary(actual_number):
    "Input a number and return the binary result"
    return "{0:b}".format(int(actual_number))


def get_hexadecimal(actual_number):
    "Input a number and return the hexadecimal result"
    h = []

    if actual_number < 0:
        actual_number = actual_number * -1
    elif actual_number == 0:
        return "NA"

    while actual_number>0:

        #print(d)
        R = actual_number%16
        x = R
        if R==10:
            x='A'
        elif R==11:
            x='B'
        elif R ==12:
            x='C'
        elif R ==13:
            x='D'
        elif R==14:
            x='E'
        elif R==15:
            x='F'
        h.insert(0,str(x))
        actual_number = actual_number//16
        hstr = ''
        for i in h:
            hstr = hstr + str(i)

    return hstr

try:
    file_location = sys.argv[1]

    with open(file_location, "r", encoding="utf-8") as data_file:
        data_list = data_file.readlines()
except  IndexError:
    print("Please also add the file while invoking the script.")
    sys.exit()

#for index in range(len(DATA_LIST)):
for index in range(len(data_list)):
    try:
        number = float(data_list[index].strip())

        bin_result = get_binary(number)
        print(f"The binary value of {number} is: {bin_result}")
        end_list.append(f"The binary value of {number} is: {bin_result}\n")

        hex_result = get_hexadecimal(number)
        print(f"The Hex value of {number} is: {hex_result}")
        end_list.append(f"The Hex value of {number} is: {hex_result}\n")

    except  ValueError:
        print(f"The value {data_list[index].strip()} is invalid and will be skipped.")

# get the end time
et = time.time()
# get the execution time
elapsed_time = et - st

end_list.append(f"Execution time:{elapsed_time} seconds")

with open("ConvertionResults.txt", "w", encoding="utf-8") as data_file:
    data_file.writelines(end_list)

print(f"Execution time:{elapsed_time} seconds")
