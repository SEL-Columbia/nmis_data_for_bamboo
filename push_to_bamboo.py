import simplejson as json
import sys
from pybamboo.dataset import Dataset
from pybamboo.exceptions import PyBambooException

BAMBOO_HASH_FILE = 'bamboo_hash.json'

# get the current bamboo hash
bamboo_hash = None
try:
    with open(BAMBOO_HASH_FILE) as f:
        try:
            bamboo_hash = json.loads(f.read())
        except JSONDecodeError:
            print '%s does not contain a valid JSON document.' %\
                BAMBOO_HASH_FILE
            sys.exit(1)
except IOError:
    print 'Error reading file: %s' % BAMBOO_HASH_FILE
    sys.exit(1)
if bamboo_hash is None:
    print 'Could not load %s' % BAMBOO_HASH_FILE
    sys.exit(1)

# update the datasets
hash_updates = dict()
for name, content in bamboo_hash.iteritems():
    filename = content['filename']
    bamboo_id = content['bamboo_id']
    file_path = 'data/' + filename
    print '%s -> %s' % (filename, bamboo_id)
    if bamboo_id:
        print '%s has bamboo id: %s. Updating bamboo dataset.' %\
            (name, bamboo_id)
        try:
            dataset = Dataset(dataset_id=bamboo_id)
            dataset.reset(path=file_path)
        except PyBambooException:
            print 'Error creating dataset for file: %s' % filename
    else:
        print '%s has no bamboo id. Adding file to bamboo.' % name
        try:
            dataset = Dataset(path=file_path)
            hash_updates[name] = {
                'filename': filename,
                'bamboo_id': dataset.id,
            }
        except PyBambooException:
            print 'Error creating dataset for file: %s' % filename

# update the hash file
bamboo_hash.update(hash_updates)
try:
    with open(BAMBOO_HASH_FILE, 'wb') as f:
        f.write(json.dumps(bamboo_hash))
except IOError:
    print 'Error writing file: %s' % BAMBOO_HASH_FILE
    sys.exit(1)
