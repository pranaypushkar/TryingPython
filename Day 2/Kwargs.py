def fn(**kwargs):
	for key in kwargs.keys():
		print(key, ":", kwargs[key])
		

fn(a = 10, b = 20, c = 200, name = "India", capital = "New Delhi", temp = 30)