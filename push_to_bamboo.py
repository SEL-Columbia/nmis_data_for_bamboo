import simplejson as json
import sys
from pybamboo.dataset import Dataset
from pybamboo.exceptions import PyBambooException


BAMBOO_HASH_FILE = 'bamboo_hash.json'
DATA_FILE_FORMAT = 'csv'

bamboo_hash = None
try:
    with open(BAMBOO_HASH_FILE) as f:
        try:
            bamboo_hash = json.loads(f.read())
        except:
            print '%s does not contain a valid JSON document.' %\
                BAMBOO_HASH_FILE
            sys.exit(1)
except IOError:
    print 'Error reading file: %s' % BAMBOO_HASH_FILE
    sys.exit(1)
if bamboo_hash is None:
    print 'Could not load %s' % BAMBOO_HASH_FILE
    sys.exit(1)

hash_updates = dict()
for data_file, bamboo_id in bamboo_hash.iteritems():
    filename = data_file + '.' + DATA_FILE_FORMAT
    #print '%s -> %s' % (filename, bamboo_id)
    if bamboo_id:
        print '%s has bamboo id: %s' % (data_file, bamboo_id)
    else:
        print '%s has no bamboo id. Adding file to bamboo.' % data_file
        try:
            dataset = Dataset(path=filename)
            # save dataset id for file?
        except PyBambooException:
            print 'Error creating dataset for file: %s' % filename
