def maximum(num):
	ret = num[0]
	for i in range(1, len(num)):
		if ret < num[i]:
			ret = num[i]
	return ret

import random
arr = [int(random.uniform(100, -100)) for _ in range(10)]
print(arr)
print("max:", maximum(arr))
