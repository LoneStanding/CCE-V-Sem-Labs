import random

user_dict = {}

nums_vals = int(input("number of key-value pairs in the dictionary"))

for _ in range(nums_vals) :
    random_key = random.randint(1,100)
    val = input(f"the value at {random_key} is:")
    try:
        val = int(val)
    except ValueError:
        try:
            val = float(val)
        except ValueError:
            pass  
    user_dict[random_key] = val


for key, value in user_dict.items() :
    print(f"{key} : {value}")

total_count = 0
total_sum = 0
conc_str = ""

for key, value in user_dict.items() :
    if isinstance(value, int) :
        total_sum += value
        total_count += 1
    elif isinstance(value, str) :
        conc_str += value

if total_count>0 :
    average = total_sum/total_count
    print("average is:", average)

print("concatenated string is:", conc_str)