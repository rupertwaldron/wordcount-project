
mynum = '2345;6684392 	4553454, 324325, erwrew,342432'

print(mynum)


numlist = iter(str(mynum))

gen_comp = (item for item in numlist if item.isdigit())

print(mynum)

num_dict = {}


for i in gen_comp:
	if i in num_dict:
		num_dict[i] += 1
	else:
		num_dict[i] = 1

print(num_dict)

