data = {
	"Name": {
		"FirstName": "Sachin",
		"LastName": "Tendulkar"
	}
}

import json
wfobj = open("data_file.json", "w")
json.dump(data, wfobj)