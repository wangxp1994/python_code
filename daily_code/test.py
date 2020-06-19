

i = [8, 3, 8, 3]
j = ["/", "-", "/"]
compute_str = "a{}(b{}c{}d)"
sum = eval(compute_str.format(*j), {"a":i[0],"b":i[1],"c":i[2],"d":i[3]})

print(sum == 24)