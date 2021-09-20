import json

def save_json(dict1):
	try:
		out_file = open("log.json", "r+")
	except Exception as e:
		print('ERROR',e,'SUPPOSED NONE EXISTING FILE CREATING...')
		out_file = open("log.json", "w")
	  
	json.dump(dict1, out_file, indent = 6)
	  
	out_file.close()


def load_json():
    try:
        f = open('log.json')
        
        data = json.load(f)

        f.close()	
    except Exception as e:
        print('ERROR',e,'log.json DOSEN"T EXISTING SKIPING READING')
        data = {'done':[]}

	
    return data


