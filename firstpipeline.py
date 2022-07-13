#first pipeline

import json
import yaml
import sys

def is_yaml(filename):
	return 'yaml' in filename

def do_yaml_to_json(filename):
	print("do yaml to json")
	f = open(filename, "r")
	data = yaml.safe_load(f.read())

	##print(type(data), data)

	output_filename = filename.replace('.yaml', '.json')

	##print('output:', output_filename)

	outputfile = open(output_filename, "w")
	outputfile.write(json.dumps(data))

	# cleanup
	f.close()
	outputfile.close()

def do_json_to_yaml(filename):

	print("do json to yaml")
	f = open(filename, "r")
	data = json.loads(f.read())

	##print(type(data), data)

	output_filename = filename.replace('.json', '.yaml')

	##print('output:', output_filename)

	outputfile = open(output_filename, "w")
	outputfile.write(yaml.dump(data))

	#cleanup
	f.close()
	outputfile.close()


if __name__ == '__main__':

	if len(sys.argv) != 2:
		print("you forgot the filename!")
		exit()
	print('args: ', sys.argv)
	filename = sys.argv[1]
	if is_yaml(filename):
		do_yaml_to_json(filename)
	else:
		do_json_to_yaml(filename)
