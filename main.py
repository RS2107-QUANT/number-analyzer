nums = input("Enter numbers separated by commas: ")

num_list = [int(x) for x in nums.split(",")]

total = sum(num_list)
avg = total / len(num_list)

print("Sum:", total)
print("Average:", avg)
print("Max:", max(num_list))
print("Min:", min(num_list))
