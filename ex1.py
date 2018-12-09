def sub_string_num(string, sub_string):
	sum = 0
	for i in range(len(string)):
		if string[i:i+2] == sub_string:
			sum+=1
	return sum

print(sub_string_num('1212121121111121212','12'))