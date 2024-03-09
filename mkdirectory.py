import os
import json
dir_path = '%s\\Contractor\\' % os.environ['APPDATA']
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
file_name = 'config.json'
dict = {'First run': 'True'}
js_object = json.dumps(dict, indent=4)

with open(os.path.join(dir_path, file_name), 'w') as f:
    f.write(js_object)