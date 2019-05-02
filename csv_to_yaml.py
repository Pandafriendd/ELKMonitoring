import csv
import yaml
with open('export-two-cols.csv') as f:
    d = dict(filter(None, csv.reader(f)))
	
with open('output2.yaml', 'w') as newf:
    yaml.dump(d, newf, default_flow_style=False, default_style='"')
