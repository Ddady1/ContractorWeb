import os
dir_path = '%s\\Contractor\\' % os.environ['APPDATA']
if not os.path.exists(dir_path):
    os.makedirs(dir_path)

with open(os.path.join(dir_path, 'firsttime.txt'), 'w') as f:
    f.write('Already run once')